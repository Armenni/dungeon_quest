import random
from typing import Optional
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
            player.equip(EQUIPMENT[key])
