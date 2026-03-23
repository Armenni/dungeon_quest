import random
from typing import Optional, Tuple
from game.story_data import StoryEvent, EVENTS, ENDINGS, _SCORES


def resolve_ending(flags: dict[str, bool]) -> dict:
    best, best_score = "reluctant_hero", -99
    for eid, weights in _SCORES.items():
        score = sum(w for f, w in weights.items() if flags.get(f))
        if score > best_score:
            best_score = score
            best = eid
    return ENDINGS[best]


def get_event(floor_after: int) -> Optional[StoryEvent]:
    matches = [e for e in EVENTS if e.floor_after == floor_after]
    return random.choice(matches) if matches else None


def apply_choice(player, choice) -> Tuple[bool, str, Optional[dict]]:
    """
    Apply a Choice, including stat check if defined.

    Returns (success, roll_info_str, effect_applied).
    roll_info_str is non-empty only when a stat check was rolled.
    """
    if choice.stat_check:
        stat = choice.stat_check["stat"]
        tn   = choice.stat_check["tn"]
        stat_val = getattr(player, stat, 0)
        roll = random.randint(1, 6)
        total = roll + stat_val
        roll_info = f"D6({roll}) + {stat.capitalize()}({stat_val}) = {total} vs TN {tn}"
        if total < tn:
            apply_effect(player, choice.fail_effect)
            return False, roll_info, choice.fail_effect
        apply_effect(player, choice.effect)
        return True, roll_info, choice.effect

    apply_effect(player, choice.effect)
    return True, "", choice.effect


def apply_effect(player, effect: dict):
    """Apply a story choice's mechanical effect to the player."""
    from game.items import ITEMS
    from game.equipment import EQUIPMENT

    # Consume a required item from inventory if the choice costs one
    cost_key = effect.get("cost_item")
    if cost_key and cost_key in ITEMS:
        target_name = ITEMS[cost_key].name
        for i, inv_item in enumerate(player.inventory):
            if inv_item.name == target_name:
                player.inventory.pop(i)
                break

    player.apply_bonus(
        atk=effect.get("atk", 0),
        defense=effect.get("defense", 0),
        magic=effect.get("magic", 0),
        max_hp=effect.get("max_hp", 0),
        hp=effect.get("hp", 0),
        strength=effect.get("strength", 0),
        intelligence=effect.get("intelligence", 0),
        agility=effect.get("agility", 0),
        luck=effect.get("luck", 0),
        charisma=effect.get("charisma", 0),
    )
    if "gold" in effect:
        player.gold += effect["gold"]
    if "item" in effect:
        key = effect["item"]
        if key in ITEMS:
            player.inventory.append(ITEMS[key])
    if "weapon" in effect:
        key = effect["weapon"]
        if key in EQUIPMENT:
            msg, old_eq = player.equip(EQUIPMENT[key])
            if old_eq:
                player.inventory.append(old_eq)
