from dataclasses import dataclass
from typing import Optional


@dataclass
class Choice:
    text: str
    flag: str
    outcome: str
    effect: dict   # keys: atk, defense, magic, max_hp, hp, gold, item, weapon


@dataclass
class StoryEvent:
    floor_after: int
    title: str
    narrative: str
    choices: list[Choice]


EVENTS: list[StoryEvent] = [
    StoryEvent(
        floor_after=1,
        title="event1_title",
        narrative="event1_narrative",
        choices=[
            Choice(
                text="event1_choice1_text",
                flag="spared_prisoner",
                outcome="event1_choice1_outcome",
                effect={"gold": 15, "max_hp": 10, "cost_item": "health_potion"},
            ),
            Choice(
                text="event1_choice2_text",
                flag="ignored_prisoner",
                outcome="event1_choice2_outcome",
                effect={"atk": 2, "defense": 2},
            ),
            Choice(
                text="event1_choice3_text",
                flag="executed_prisoner",
                outcome="event1_choice3_outcome",
                effect={"gold": 25, "atk": 3},
            ),
        ],
    ),

    StoryEvent(
        floor_after=2,
        title="event2_title",
        narrative="event2_narrative",
        choices=[
            Choice(
                text="event2_choice1_text",
                flag="aided_village",
                outcome="event2_choice1_outcome",
                effect={"gold": 20, "max_hp": 10, "cost_item": "health_potion"},
            ),
            Choice(
                text="event2_choice2_text",
                flag="ignored_village",
                outcome="event2_choice2_outcome",
                effect={"atk": 4},
            ),
            Choice(
                text="event2_choice3_text",
                flag="looted_village",
                outcome="event2_choice3_outcome",
                effect={"gold": 35, "item": "health_potion"},
            ),
        ],
    ),

    StoryEvent(
        floor_after=3,
        title="event3_title",
        narrative="event3_narrative",
        choices=[
            Choice(
                text="event3_choice1_text",
                flag="refused_dark_pact",
                outcome="event3_choice1_outcome",
                effect={"max_hp": 20, "defense": 3},
            ),
            Choice(
                text="event3_choice2_text",
                flag="dark_pact",
                outcome="event3_choice2_outcome",
                effect={"atk": 10, "magic": 8, "max_hp": -15},
            ),
            Choice(
                text="event3_choice3_text",
                flag="bargained_sage",
                outcome="event3_choice3_outcome",
                effect={"atk": 4, "magic": 4, "max_hp": 5},
            ),
        ],
    ),

    StoryEvent(
        floor_after=4,
        title="event4_title",
        narrative="event4_narrative",
        choices=[
            Choice(
                text="event4_choice1_text",
                flag="deciphered_tome",
                outcome="event4_choice1_outcome",
                effect={"magic": 8, "max_hp": 10},
            ),
            Choice(
                text="event4_choice2_text",
                flag="sacrificed_self",
                outcome="event4_choice2_outcome",
                effect={"max_hp": -30, "atk": 15, "magic": 15},
            ),
            Choice(
                text="event4_choice3_text",
                flag="kept_secrets",
                outcome="event4_choice3_outcome",
                effect={"max_hp": 15, "defense": 5},
            ),
        ],
    ),
]


# ── Endings ───────────────────────────────────────────────────────────────────

ENDINGS: dict[str, dict] = {
    "true_hero": {
        "title": "ending_true_hero_title",
        "description": "ending_true_hero_desc",
        "dragon_modifier": {"dragon_hp_mult": 0.85, "dragon_atk_mult": 0.90,
                            "player_def_bonus": 10,
                            "bonus_msg": "ending_true_hero_bonus"},
    },
    "dark_conqueror": {
        "title": "ending_dark_conqueror_title",
        "description": "ending_dark_conqueror_desc",
        "dragon_modifier": {"dragon_hp_mult": 1.0, "dragon_atk_mult": 0.80,
                            "ally_dmg_per_turn": 8,
                            "bonus_msg": "ending_dark_conqueror_bonus"},
    },
    "scholar_king": {
        "title": "ending_scholar_king_title",
        "description": "ending_scholar_king_desc",
        "dragon_modifier": {"dragon_hp_mult": 0.90, "player_magic_mult": 1.35,
                            "bonus_msg": "ending_scholar_king_bonus"},
    },
    "martyred_saint": {
        "title": "ending_martyred_saint_title",
        "description": "ending_martyred_saint_desc",
        "dragon_modifier": {"dragon_hp_mult": 0.75, "dragon_atk_mult": 1.15,
                            "revive_once": True,
                            "bonus_msg": "ending_martyred_saint_bonus"},
    },
    "reluctant_hero": {
        "title": "ending_reluctant_hero_title",
        "description": "ending_reluctant_hero_desc",
        "dragon_modifier": {},
    },
}


# ── Scoring table ─────────────────────────────────────────────────────────────

_SCORES: dict[str, dict[str, int]] = {
    "true_hero":      {"spared_prisoner": 2, "executed_prisoner": -1, "aided_village": 2,
                       "looted_village": -2, "refused_dark_pact": 2, "dark_pact": -2,
                       "bargained_sage": 0},
    "dark_conqueror": {"executed_prisoner": 2, "looted_village": 2, "dark_pact": 2,
                       "spared_prisoner": -1, "aided_village": -1, "refused_dark_pact": -2,
                       "kept_secrets": 1},
    "scholar_king":   {"bargained_sage": 2, "deciphered_tome": 3, "dark_pact": -1,
                       "kept_secrets": 1},
    "martyred_saint": {"sacrificed_self": 5, "spared_prisoner": 1, "aided_village": 1,
                       "dark_pact": -2, "looted_village": -2},
    "reluctant_hero": {"ignored_prisoner": 2, "ignored_village": 2},
}


def resolve_ending(flags: dict[str, bool]) -> dict:
    best, best_score = "reluctant_hero", -99
    for eid, weights in _SCORES.items():
        score = sum(w for f, w in weights.items() if flags.get(f))
        if score > best_score:
            best_score = score
            best = eid
    return ENDINGS[best]


def get_event(floor_after: int) -> Optional[StoryEvent]:
    for e in EVENTS:
        if e.floor_after == floor_after:
            return e
    return None


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
