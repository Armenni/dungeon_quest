import random
from typing import Tuple, List
from game.player import Player
from game.enemy import Enemy
from game.status import apply_status, tick_statuses, consume_stun, weakened_penalty
from game.i18n import t


# Spells: class -> name -> {cost, dmg_mult, desc, side_effect?, targets_self?}
# side_effect: (etype, duration, magnitude)
# targets_self: if True, the spell buffs/shields the player instead of damaging the enemy
SPELLS: dict[str, dict] = {
    "Warrior": {
        "Battlecry": {"cost": 10, "dmg_mult": 1.8, "desc": "A mighty war cry strike"},
    },
    "Mage": {
        "Fireball":    {"cost": 15, "dmg_mult": 2.5, "desc": "A ball of roaring fire",
                        "side_effect": ("burn", 3, 5)},
        "Ice Shard":   {"cost": 10, "dmg_mult": 2.0, "desc": "A razor-sharp shard of ice",
                        "side_effect": ("stun", 1, 0)},
        "Frost Armor": {"cost": 20, "dmg_mult": 0,   "desc": "Erect an arcane barrier",
                        "side_effect": ("shielded", 2, 0), "targets_self": True},
    },
    "Rogue": {
        "Backstab": {"cost": 12, "dmg_mult": 2.2, "desc": "Strike from the shadows",
                     "side_effect": ("weakened", 2, 4)},
    },
}


def player_turn_start(player: Player) -> List[Tuple[str, int]]:
    """Tick DoT effects on the player. Call at start of player's turn."""
    return tick_statuses(player)


def enemy_turn_start(enemy: Enemy) -> List[Tuple[str, int]]:
    """Tick DoT effects on the enemy. Call before enemy acts."""
    return tick_statuses(enemy)


def player_attack(player: Player, enemy: Enemy) -> Tuple[int, bool]:
    crit = random.random() < (0.2 if player.player_class == "Rogue" else 0.1)
    penalty = weakened_penalty(player)
    effective_atk = max(1, player.atk - penalty)
    dmg = effective_atk + random.randint(-2, 4)
    if crit:
        dmg = int(dmg * 1.5)
    return enemy.take_damage(dmg), crit


def player_magic(player: Player, enemy: Enemy, spell_name: str,
                 magic_mult: float = 1.0) -> Tuple[int, str, str]:
    """
    Returns (damage, spell_name, side_effect_msg).
    side_effect_msg is empty if no effect was applied.
    For targets_self spells: applies effect to player, returns 0 damage.
    """
    spell = SPELLS[player.player_class][spell_name]
    if player.mp < spell["cost"]:
        return 0, spell_name, t("not_enough_mp")
    player.mp -= spell["cost"]

    if spell.get("targets_self"):
        fx_msg = ""
        if "side_effect" in spell:
            etype, dur, mag = spell["side_effect"]
            apply_status(player, etype, dur, mag)
            fx_msg = t("frost_armor_fx", dur=dur)
        return 0, spell_name, fx_msg

    dmg = int(player.magic * magic_mult * spell["dmg_mult"]) + random.randint(-3, 5)
    actual = enemy.take_damage(dmg)

    fx_msg = ""
    if "side_effect" in spell and actual > 0:
        etype, dur, mag = spell["side_effect"]
        if etype == "stun":
            if random.random() < 0.5:
                apply_status(enemy, etype, dur, mag)
                fx_msg = t("enemy_is_stunned")
        else:
            apply_status(enemy, etype, dur, mag)
            fx_msg = t("enemy_affected", etype=etype)

    return actual, spell_name, fx_msg


def enemy_turn(enemy: Enemy, player: Player,
               turn_count: int = 0, last_ability: str = "") -> Tuple[int, str, str]:
    """
    Returns (actual_damage, message, ability_used).
    Damage messages include DEF absorption info.
    wing_stun is suppressed on turn 0 (first action) — players deserve one free attack.
    The same ability cannot fire twice in a row.
    """
    available = list(enemy.abilities)
    if turn_count == 0 and "wing_stun" in available and len(available) > 1:
        available.remove("wing_stun")
    if last_ability in available and len(available) > 1:
        available.remove(last_ability)
    ability = random.choice(available)

    def hit(raw: int) -> Tuple[int, str]:
        actual = player.take_damage(raw)
        absorbed = raw - actual
        block = f" {t('damage_absorbed', n=absorbed)}" if absorbed > 0 else ""
        return actual, t("take_damage", dmg=actual) + block

    if ability == "heavy_strike":
        raw = int(enemy.atk * 1.5) + random.randint(0, 5)
        actual, dmg_str = hit(raw)
        return actual, t("ability_heavy_strike", name=enemy.name, dmg=dmg_str), ability

    if ability == "bone_throw":
        raw = enemy.atk + random.randint(2, 6)
        actual, dmg_str = hit(raw)
        return actual, t("ability_bone_throw", name=enemy.name, dmg=dmg_str), ability

    if ability == "fireball":
        raw = int(enemy.atk * 1.8)
        actual, dmg_str = hit(raw)
        apply_status(player, "burn", 3, 5)
        return actual, t("ability_fireball", name=enemy.name, dmg=dmg_str), ability

    if ability == "fire_breath":
        raw = int(enemy.atk * 1.6) + random.randint(5, 15)   # reduced from 2.0x
        actual, dmg_str = hit(raw)
        apply_status(player, "burn", 3, 8)
        return actual, t("ability_fire_breath", name=enemy.name, dmg=dmg_str), ability

    if ability == "tail_swipe":
        raw = int(enemy.atk * 1.3)
        actual, dmg_str = hit(raw)
        return actual, t("ability_tail_swipe", name=enemy.name, dmg=dmg_str), ability

    if ability == "regenerate":
        heal = random.randint(10, 20)
        enemy.hp = min(enemy.max_hp, enemy.hp + heal)
        return -heal, t("ability_regenerate", name=enemy.name, heal=heal), ability

    if ability == "poison_sting":
        raw = enemy.atk + random.randint(0, 3)
        actual, dmg_str = hit(raw)
        if random.random() < 0.5:
            apply_status(player, "poison", 3, 4)
            return actual, t("ability_venom", name=enemy.name, dmg=dmg_str), ability
        return actual, t("ability_sting", name=enemy.name, dmg=dmg_str), ability

    if ability == "curse":
        apply_status(player, "weakened", 2, 4)
        return 0, t("ability_curse", name=enemy.name), ability

    if ability == "stun_bash":
        raw = int(enemy.atk * 0.8)
        actual, dmg_str = hit(raw)
        apply_status(player, "stun", 1, 0)
        return actual, t("ability_stun_bash", name=enemy.name, dmg=dmg_str), ability

    if ability == "toxic_breath":
        raw = int(enemy.atk * 1.5)
        actual, dmg_str = hit(raw)
        apply_status(player, "poison", 4, 6)
        return actual, t("ability_toxic_breath", name=enemy.name, dmg=dmg_str), ability

    if ability == "wing_stun":
        apply_status(player, "stun", 1, 0)
        return 0, t("ability_wing_stun", name=enemy.name), ability

    # default: basic attack
    penalty = weakened_penalty(enemy)
    raw = max(1, enemy.atk - penalty) + random.randint(-2, 3)
    actual, dmg_str = hit(raw)
    return actual, t("enemy_basic_attack", name=enemy.name, dmg=dmg_str), ability
