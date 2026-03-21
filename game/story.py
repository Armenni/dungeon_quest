from dataclasses import dataclass
from typing import Optional


@dataclass
class Choice:
    text: str
    flag: str
    outcome: str
    effect: dict   # keys: atk, defense, magic, max_hp, hp, gold, item, weapon
    class_only: str = ""  # if set, only shown to this player class


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
            Choice(
                text="event1_warrior_text",
                flag="warrior_stood_guard",
                outcome="event1_warrior_outcome",
                effect={"defense": 4, "max_hp": 10},
                class_only="Warrior",
            ),
            Choice(
                text="event1_mage_text",
                flag="mage_healed_prisoner",
                outcome="event1_mage_outcome",
                effect={"magic": 3, "max_hp": -5},
                class_only="Mage",
            ),
            Choice(
                text="event1_rogue_text",
                flag="rogue_looted_prisoner",
                outcome="event1_rogue_outcome",
                effect={"gold": 25, "atk": 2},
                class_only="Rogue",
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
            Choice(
                text="event2_warrior_text",
                flag="warrior_sworn_oath",
                outcome="event2_warrior_outcome",
                effect={"max_hp": 15, "atk": 2},
                class_only="Warrior",
            ),
            Choice(
                text="event2_mage_text",
                flag="mage_warded_alcove",
                outcome="event2_mage_outcome",
                effect={"magic": 5, "max_hp": 5},
                class_only="Mage",
            ),
            Choice(
                text="event2_rogue_text",
                flag="rogue_left_supplies",
                outcome="event2_rogue_outcome",
                effect={"atk": 4, "defense": 2},
                class_only="Rogue",
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
            Choice(
                text="event3_warrior_text",
                flag="warrior_endured",
                outcome="event3_warrior_outcome",
                effect={"atk": 7, "defense": 3, "max_hp": 5},
                class_only="Warrior",
            ),
            Choice(
                text="event3_mage_text",
                flag="mage_improved_pact",
                outcome="event3_mage_outcome",
                effect={"magic": 9, "atk": 2},
                class_only="Mage",
            ),
            Choice(
                text="event3_rogue_text",
                flag="rogue_stole_reagents",
                outcome="event3_rogue_outcome",
                effect={"gold": 20, "atk": 3, "magic": 3},
                class_only="Rogue",
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
            Choice(
                text="event4_warrior_text",
                flag="warrior_tactical",
                outcome="event4_warrior_outcome",
                effect={"atk": 9, "defense": 4},
                class_only="Warrior",
            ),
            Choice(
                text="event4_mage_text",
                flag="mage_channeled_tome",
                outcome="event4_mage_outcome",
                effect={"magic": 13},
                class_only="Mage",
            ),
            Choice(
                text="event4_rogue_text",
                flag="rogue_runed_blade",
                outcome="event4_rogue_outcome",
                effect={"atk": 7, "magic": 4},
                class_only="Rogue",
            ),
        ],
    ),

    StoryEvent(
        floor_after=5,
        title="event5_title",
        narrative="event5_narrative",
        choices=[
            Choice(
                text="event5_choice1_text",
                flag="fought_knight",
                outcome="event5_choice1_outcome",
                effect={"hp": -15, "atk": 5},
            ),
            Choice(
                text="event5_choice2_text",
                flag="redeemed_knight",
                outcome="event5_choice2_outcome",
                effect={"max_hp": 15, "defense": 3},
            ),
            Choice(
                text="event5_choice3_text",
                flag="executed_knight",
                outcome="event5_choice3_outcome",
                effect={"gold": 30, "atk": 4},
            ),
            Choice(
                text="event5_warrior_text",
                flag="warrior_duel",
                outcome="event5_warrior_outcome",
                effect={"atk": 6, "defense": 4, "max_hp": 10},
                class_only="Warrior",
            ),
            Choice(
                text="event5_mage_text",
                flag="mage_purified",
                outcome="event5_mage_outcome",
                effect={"magic": 8, "max_hp": 10},
                class_only="Mage",
            ),
            Choice(
                text="event5_rogue_text",
                flag="rogue_sneaked",
                outcome="event5_rogue_outcome",
                effect={"atk": 4, "gold": 20, "hp": 10},
                class_only="Rogue",
            ),
        ],
    ),

    StoryEvent(
        floor_after=6,
        title="event6_title",
        narrative="event6_narrative",
        choices=[
            Choice(
                text="event6_choice1_text",
                flag="shattered_tear",
                outcome="event6_choice1_outcome",
                effect={"atk": 6, "magic": 6},
            ),
            Choice(
                text="event6_choice2_text",
                flag="kept_tear",
                outcome="event6_choice2_outcome",
                effect={"max_hp": 25, "defense": 4},
            ),
            Choice(
                text="event6_choice3_text",
                flag="drank_tear",
                outcome="event6_choice3_outcome",
                effect={"max_hp": -10, "atk": 8, "magic": 8},
            ),
            Choice(
                text="event6_warrior_text",
                flag="warrior_crushed_tear",
                outcome="event6_warrior_outcome",
                effect={"atk": 10, "defense": 5},
                class_only="Warrior",
            ),
            Choice(
                text="event6_mage_text",
                flag="mage_absorbed_tear",
                outcome="event6_mage_outcome",
                effect={"magic": 14, "max_hp": 5},
                class_only="Mage",
            ),
            Choice(
                text="event6_rogue_text",
                flag="rogue_pocketed_tear",
                outcome="event6_rogue_outcome",
                effect={"gold": 35, "atk": 5, "magic": 3},
                class_only="Rogue",
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
    "true_hero": {
        "spared_prisoner": 2, "executed_prisoner": -1,
        "aided_village": 2, "looted_village": -2,
        "refused_dark_pact": 2, "dark_pact": -2,
        "redeemed_knight": 3, "executed_knight": -1,
        "kept_tear": 3, "shattered_tear": -1, "drank_tear": -1,
        "warrior_stood_guard": 1, "mage_healed_prisoner": 1,
        "warrior_sworn_oath": 1, "mage_warded_alcove": 1,
        "warrior_duel": 1, "mage_purified": 2,
    },
    "dark_conqueror": {
        "executed_prisoner": 2, "looted_village": 2, "dark_pact": 2,
        "spared_prisoner": -1, "aided_village": -1, "refused_dark_pact": -2,
        "kept_secrets": 1,
        "executed_knight": 2, "fought_knight": 1,
        "drank_tear": 2, "shattered_tear": 1,
        "rogue_looted_prisoner": 1, "rogue_stole_reagents": 1, "warrior_tactical": 1,
    },
    "scholar_king": {
        "bargained_sage": 2, "deciphered_tome": 3, "dark_pact": -1,
        "kept_secrets": 1,
        "mage_improved_pact": 2, "mage_channeled_tome": 3,
        "mage_purified": 2, "mage_absorbed_tear": 3,
        "kept_tear": 1, "redeemed_knight": 1,
        "mage_healed_prisoner": 1, "mage_warded_alcove": 1,
    },
    "martyred_saint": {
        "sacrificed_self": 5, "spared_prisoner": 1, "aided_village": 1,
        "dark_pact": -2, "looted_village": -2,
        "redeemed_knight": 2, "kept_tear": 2,
        "warrior_sworn_oath": 1, "mage_healed_prisoner": 1,
        "mage_warded_alcove": 1, "warrior_stood_guard": 1, "mage_purified": 1,
    },
    "reluctant_hero": {
        "ignored_prisoner": 2, "ignored_village": 2,
        "fought_knight": 2, "rogue_sneaked": 1, "rogue_left_supplies": 1,
    },
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
