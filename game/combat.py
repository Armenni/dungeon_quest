import random
from typing import Tuple, List
from game.player import Player
from game.enemy import Enemy
from game.status import apply_status, tick_statuses, consume_stun, weakened_penalty
from game.i18n import t


# Spells: class -> name -> {cost, dmg_mult, desc, side_effect?, targets_self?, debuff_only?}
# side_effect: (etype, duration, magnitude)
# targets_self: if True, the spell buffs/shields the player instead of damaging the enemy
# debuff_only: if True, no damage — applies side_effect directly to enemy
SPELLS: dict[str, dict] = {
    "Warrior": {
        "Battlecry": {"cost": 10, "dmg_mult": 0, "desc": "A war cry that weakens the enemy",
                      "side_effect": ("weakened", 3, 4), "debuff_only": True},
    },
    "Mage": {
        "Fireball":    {"cost": 15, "dmg_mult": 2.0, "desc": "A ball of roaring fire",
                        "side_effect": ("burn", 3, 5)},
        "Ice Shard":   {"cost": 10, "dmg_mult": 2.0, "desc": "A razor-sharp shard of ice",
                        "side_effect": ("stun", 1, 0)},
        "Frost Armor": {"cost": 20, "dmg_mult": 0,   "desc": "Erect an arcane barrier",
                        "side_effect": ("shielded", 2, 0), "targets_self": True},
    },
    "Rogue": {
        "Backstab": {"cost": 12, "dmg_mult": 2.2, "desc": "Strike from the shadows",
                     "side_effect": ("bleed", 3, 5)},
    },
}


def player_turn_start(player: Player) -> List[Tuple[str, int]]:
    """Tick DoT effects on the player. Call at start of player's turn."""
    return tick_statuses(player)


def enemy_turn_start(enemy: Enemy) -> List[Tuple[str, int]]:
    """Tick DoT effects on the enemy. Call before enemy acts."""
    return tick_statuses(enemy)


def player_attack(player: Player, enemy: Enemy) -> Tuple[int, bool]:
    crit = random.random() < player.crit_chance
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

    if spell.get("debuff_only"):
        fx_msg = ""
        if "side_effect" in spell:
            etype, dur, mag = spell["side_effect"]
            apply_status(enemy, etype, dur, mag)
            fx_msg = t("battlecry_fx", dur=dur)
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
        elif etype == "bleed":
            apply_status(enemy, etype, dur, mag)
            fx_msg = t("enemy_bleeding")
        else:
            apply_status(enemy, etype, dur, mag)
            fx_msg = t("enemy_affected", etype=etype)

    return actual, spell_name, fx_msg


def _hit(player: Player, raw: int) -> Tuple[int, str]:
    """Helper: applies damage and formats message with absorption info."""
    actual = player.take_damage(raw)
    absorbed = raw - actual
    block = f" {t('damage_absorbed', n=absorbed)}" if absorbed > 0 else ""
    return actual, t("take_damage", dmg=actual) + block


def _ability_heavy_strike(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.5) + random.randint(0, 5)
    actual, dmg_str = _hit(player, raw)
    return actual, t("ability_heavy_strike", name=enemy.name, dmg=dmg_str)


def _ability_bone_throw(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = enemy.atk + random.randint(2, 6)
    actual, dmg_str = _hit(player, raw)
    return actual, t("ability_bone_throw", name=enemy.name, dmg=dmg_str)


def _ability_fireball(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.8)
    actual, dmg_str = _hit(player, raw)
    apply_status(player, "burn", 3, 5)
    return actual, t("ability_fireball", name=enemy.name, dmg=dmg_str)


def _ability_fire_breath(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.6) + random.randint(5, 15)
    actual, dmg_str = _hit(player, raw)
    apply_status(player, "burn", 3, 8)
    return actual, t("ability_fire_breath", name=enemy.name, dmg=dmg_str)


def _ability_tail_swipe(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.3)
    actual, dmg_str = _hit(player, raw)
    return actual, t("ability_tail_swipe", name=enemy.name, dmg=dmg_str)


def _ability_regenerate(enemy: Enemy, player: Player) -> Tuple[int, str]:
    heal = random.randint(10, 20)
    enemy.hp = min(enemy.max_hp, enemy.hp + heal)
    return -heal, t("ability_regenerate", name=enemy.name, heal=heal)


def _ability_poison_sting(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = enemy.atk + random.randint(0, 3)
    actual, dmg_str = _hit(player, raw)
    if random.random() < 0.5:
        apply_status(player, "poison", 3, 4)
        return actual, t("ability_venom", name=enemy.name, dmg=dmg_str)
    return actual, t("ability_sting", name=enemy.name, dmg=dmg_str)


def _ability_curse(enemy: Enemy, player: Player) -> Tuple[int, str]:
    apply_status(player, "weakened", 2, 4)
    return 0, t("ability_curse", name=enemy.name)


def _ability_stun_bash(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 0.8)
    actual, dmg_str = _hit(player, raw)
    apply_status(player, "stun", 1, 0)
    return actual, t("ability_stun_bash", name=enemy.name, dmg=dmg_str)


def _ability_toxic_breath(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.5)
    actual, dmg_str = _hit(player, raw)
    apply_status(player, "poison", 4, 6)
    return actual, t("ability_toxic_breath", name=enemy.name, dmg=dmg_str)


def _ability_wing_stun(enemy: Enemy, player: Player) -> Tuple[int, str]:
    apply_status(player, "stun", 1, 0)
    return 0, t("ability_wing_stun", name=enemy.name)


def _ability_basic_attack(enemy: Enemy, player: Player) -> Tuple[int, str]:
    penalty = weakened_penalty(enemy)
    raw = max(1, enemy.atk - penalty) + random.randint(-2, 3)
    actual, dmg_str = _hit(player, raw)
    return actual, t("enemy_basic_attack", name=enemy.name, dmg=dmg_str)


def _ability_drain_mana(enemy: Enemy, player: Player) -> Tuple[int, str]:
    drained = min(player.mp, random.randint(8, 15))
    player.mp = max(0, player.mp - drained)
    heal_amount = drained // 2
    enemy.hp = min(enemy.max_hp, enemy.hp + heal_amount)
    return 0, t("ability_drain_mana", name=enemy.name, drained=drained, heal=heal_amount)


def _ability_life_steal(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.4) + random.randint(0, 4)
    actual, dmg_str = _hit(player, raw)
    heal_amount = actual // 2
    enemy.hp = min(enemy.max_hp, enemy.hp + heal_amount)
    return actual, t("ability_life_steal", name=enemy.name, dmg=dmg_str, heal=heal_amount)


def _ability_dark_ritual(enemy: Enemy, player: Player) -> Tuple[int, str]:
    bonus = int(enemy.max_hp * 0.15)
    enemy.hp = min(enemy.max_hp, enemy.hp + bonus)
    enemy.atk = int(enemy.atk * 1.2)
    return 0, t("ability_dark_ritual", name=enemy.name, heal=bonus)


def _ability_shadow_bolt(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.3) + random.randint(2, 6)
    actual, dmg_str = _hit(player, raw)
    apply_status(player, "weakened", 2, 3)
    return actual, t("ability_shadow_bolt", name=enemy.name, dmg=dmg_str)


def _ability_web_trap(enemy: Enemy, player: Player) -> Tuple[int, str]:
    apply_status(player, "stun", 1, 0)
    return 0, t("ability_web_trap", name=enemy.name)


def _ability_rock_slam(enemy: Enemy, player: Player) -> Tuple[int, str]:
    raw = int(enemy.atk * 1.6) + random.randint(0, 4)
    actual, dmg_str = _hit(player, raw)
    if random.random() < 0.5:
        apply_status(player, "stun", 1, 0)
        return actual, t("ability_rock_slam_stun", name=enemy.name, dmg=dmg_str)
    return actual, t("ability_rock_slam", name=enemy.name, dmg=dmg_str)


_ABILITY_HANDLERS: dict[str, callable] = {
    "heavy_strike": _ability_heavy_strike,
    "bone_throw": _ability_bone_throw,
    "fireball": _ability_fireball,
    "fire_breath": _ability_fire_breath,
    "tail_swipe": _ability_tail_swipe,
    "regenerate": _ability_regenerate,
    "poison_sting": _ability_poison_sting,
    "curse": _ability_curse,
    "stun_bash": _ability_stun_bash,
    "toxic_breath": _ability_toxic_breath,
    "wing_stun": _ability_wing_stun,
    "drain_mana": _ability_drain_mana,
    "life_steal": _ability_life_steal,
    "dark_ritual": _ability_dark_ritual,
    "shadow_bolt": _ability_shadow_bolt,
    "web_trap": _ability_web_trap,
    "rock_slam": _ability_rock_slam,
    "attack": _ability_basic_attack,
}


def enemy_turn(enemy: Enemy, player: Player,
               turn_count: int = 0, last_ability: str = "") -> Tuple[int, str, str]:
    """
    Returns (actual_damage, message, ability_used).
    Damage messages include DEF absorption info.
    wing_stun is suppressed on turn 0 (first action) — players deserve one free attack.
    The same ability cannot fire twice in a row.
    Agility gives a chance to dodge the entire attack.
    """
    available = list(enemy.abilities)
    if turn_count == 0 and "wing_stun" in available and len(available) > 1:
        available.remove("wing_stun")
    if last_ability in available and len(available) > 1:
        available.remove(last_ability)
    ability = random.choice(available)

    # Dodge check — regenerate/drain abilities cannot be dodged
    if ability not in ("regenerate", "dark_ritual", "drain_mana", "curse"):
        if random.random() < player.dodge_chance:
            return 0, t("player_dodged", name=enemy.name), ability

    handler = _ABILITY_HANDLERS.get(ability, _ability_basic_attack)
    actual, msg = handler(enemy, player)
    return actual, msg, ability
