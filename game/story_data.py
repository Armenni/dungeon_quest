from dataclasses import dataclass


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

    # Alternate events (added by storyteller)
    StoryEvent(
        floor_after=1,
        title="event1alt_title",
        narrative="event1alt_narrative",
        choices=[
            Choice(text="event1alt_choice1_text", flag="trader_bargained", outcome="event1alt_choice1_outcome", effect={"gold": 10, "atk": 3}),
            Choice(text="event1alt_choice2_text", flag="trader_refused", outcome="event1alt_choice2_outcome", effect={"max_hp": 15, "defense": 2}),
            Choice(text="event1alt_choice3_text", flag="trader_robbed", outcome="event1alt_choice3_outcome", effect={"gold": 30, "atk": 1}),
            Choice(text="event1alt_warrior_text", flag="warrior_bargained_grimly", outcome="event1alt_warrior_outcome", effect={"atk": 5, "defense": 2}, class_only="Warrior"),
            Choice(text="event1alt_mage_text", flag="mage_sensed_magic", outcome="event1alt_mage_outcome", effect={"magic": 5}, class_only="Mage"),
            Choice(text="event1alt_rogue_text", flag="rogue_smooth_talk", outcome="event1alt_rogue_outcome", effect={"gold": 15, "atk": 3}, class_only="Rogue"),
        ],
    ),

    StoryEvent(
        floor_after=2,
        title="event2alt_title",
        narrative="event2alt_narrative",
        choices=[
            Choice(text="event2alt_choice1_text", flag="ruins_studied", outcome="event2alt_choice1_outcome", effect={"magic": 4, "max_hp": 5}),
            Choice(text="event2alt_choice2_text", flag="ruins_ignored", outcome="event2alt_choice2_outcome", effect={"atk": 3}),
            Choice(text="event2alt_choice3_text", flag="ruins_desecrated", outcome="event2alt_choice3_outcome", effect={"gold": 20, "atk": 2}),
            Choice(text="event2alt_warrior_text", flag="warrior_protected_ruins", outcome="event2alt_warrior_outcome", effect={"defense": 5, "max_hp": 10}, class_only="Warrior"),
            Choice(text="event2alt_mage_text", flag="mage_deciphered_runes", outcome="event2alt_mage_outcome", effect={"magic": 8, "max_hp": 5}, class_only="Mage"),
            Choice(text="event2alt_rogue_text", flag="rogue_found_cache", outcome="event2alt_rogue_outcome", effect={"gold": 25, "atk": 2}, class_only="Rogue"),
        ],
    ),

    StoryEvent(
        floor_after=3,
        title="event3alt_title",
        narrative="event3alt_narrative",
        choices=[
            Choice(text="event3alt_choice1_text", flag="prisoner_freed", outcome="event3alt_choice1_outcome", effect={"max_hp": 10, "defense": 3}),
            Choice(text="event3alt_choice2_text", flag="prisoner_left", outcome="event3alt_choice2_outcome", effect={"atk": 4}),
            Choice(text="event3alt_choice3_text", flag="prisoner_used", outcome="event3alt_choice3_outcome", effect={"gold": 15, "atk": 3}),
            Choice(text="event3alt_warrior_text", flag="warrior_freed_honorably", outcome="event3alt_warrior_outcome", effect={"atk": 6, "defense": 3}, class_only="Warrior"),
            Choice(text="event3alt_mage_text", flag="mage_broke_chains", outcome="event3alt_mage_outcome", effect={"magic": 6, "max_hp": 8}, class_only="Mage"),
            Choice(text="event3alt_rogue_text", flag="rogue_picked_locks", outcome="event3alt_rogue_outcome", effect={"atk": 5, "gold": 10}, class_only="Rogue"),
        ],
    ),

    StoryEvent(
        floor_after=4,
        title="event4alt_title",
        narrative="event4alt_narrative",
        choices=[
            Choice(text="event4alt_choice1_text", flag="shrine_honored", outcome="event4alt_choice1_outcome", effect={"magic": 5, "max_hp": 10}),
            Choice(text="event4alt_choice2_text", flag="shrine_rejected", outcome="event4alt_choice2_outcome", effect={"atk": 5}),
            Choice(text="event4alt_choice3_text", flag="shrine_destroyed", outcome="event4alt_choice3_outcome", effect={"gold": 20, "atk": 3}),
            Choice(text="event4alt_warrior_text", flag="warrior_claimed_altar", outcome="event4alt_warrior_outcome", effect={"atk": 8, "defense": 3}, class_only="Warrior"),
            Choice(text="event4alt_mage_text", flag="mage_absorbed_shrine", outcome="event4alt_mage_outcome", effect={"magic": 10, "max_hp": -5}, class_only="Mage"),
            Choice(text="event4alt_rogue_text", flag="rogue_looted_shrine", outcome="event4alt_rogue_outcome", effect={"gold": 30, "atk": 2}, class_only="Rogue"),
        ],
    ),

    StoryEvent(
        floor_after=5,
        title="event5alt_title",
        narrative="event5alt_narrative",
        choices=[
            Choice(text="event5alt_choice1_text", flag="rival_defeated", outcome="event5alt_choice1_outcome", effect={"atk": 6, "gold": 25}),
            Choice(text="event5alt_choice2_text", flag="rival_allied", outcome="event5alt_choice2_outcome", effect={"max_hp": 15, "defense": 3}),
            Choice(text="event5alt_choice3_text", flag="rival_spared", outcome="event5alt_choice3_outcome", effect={"atk": 3, "magic": 3}),
            Choice(text="event5alt_warrior_text", flag="warrior_proved_strength", outcome="event5alt_warrior_outcome", effect={"atk": 9, "defense": 3}, class_only="Warrior"),
            Choice(text="event5alt_mage_text", flag="mage_outmatched_rival", outcome="event5alt_mage_outcome", effect={"magic": 7, "max_hp": 10}, class_only="Mage"),
            Choice(text="event5alt_rogue_text", flag="rogue_outsmarted_rival", outcome="event5alt_rogue_outcome", effect={"atk": 6, "gold": 20}, class_only="Rogue"),
        ],
    ),

    StoryEvent(
        floor_after=6,
        title="event6alt_title",
        narrative="event6alt_narrative",
        choices=[
            Choice(text="event6alt_choice1_text", flag="vision_heeded", outcome="event6alt_choice1_outcome", effect={"max_hp": 20, "defense": 3}),
            Choice(text="event6alt_choice2_text", flag="vision_ignored", outcome="event6alt_choice2_outcome", effect={"atk": 5}),
            Choice(text="event6alt_choice3_text", flag="vision_questioned", outcome="event6alt_choice3_outcome", effect={"magic": 5, "max_hp": 10}),
            Choice(text="event6alt_warrior_text", flag="warrior_demanded_answers", outcome="event6alt_warrior_outcome", effect={"atk": 8, "defense": 4}, class_only="Warrior"),
            Choice(text="event6alt_mage_text", flag="mage_communed_spirit", outcome="event6alt_mage_outcome", effect={"magic": 12, "max_hp": 5}, class_only="Mage"),
            Choice(text="event6alt_rogue_text", flag="rogue_sensed_truth", outcome="event6alt_rogue_outcome", effect={"atk": 5, "magic": 4}, class_only="Rogue"),
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
    "shadow_broker": {
        "title": "ending_shadow_broker_title",
        "description": "ending_shadow_broker_desc",
        "dragon_modifier": {"dragon_atk_mult": 0.75, "player_def_bonus": 5,
                            "bonus_msg": "ending_shadow_broker_bonus"},
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
        "trader_refused": 1, "rival_spared": 1, "vision_ignored": 1,
    },
}

# Add new alternate event flags to existing endings
_SCORES["true_hero"].update({
    "ruins_studied": 1, "prisoner_freed": 2, "shrine_honored": 1, "vision_heeded": 2,
    "mage_deciphered_runes": 1, "mage_broke_chains": 1, "mage_communed_spirit": 2,
})
_SCORES["dark_conqueror"].update({
    "trader_bargained": 1, "ruins_desecrated": 2, "prisoner_used": 1, "shrine_destroyed": 1, "rival_defeated": 2,
    "warrior_claimed_altar": 1, "rogue_looted_shrine": 2,
})
_SCORES["scholar_king"].update({
    "ruins_studied": 2, "shrine_honored": 1, "mage_deciphered_runes": 2, "mage_absorbed_shrine": 3, "mage_communed_spirit": 3,
    "vision_questioned": 1,
})
_SCORES["martyred_saint"].update({
    "prisoner_freed": 3, "shrine_honored": 2, "vision_heeded": 2,
    "warrior_freed_honorably": 2, "mage_broke_chains": 1,
})

_SCORES["shadow_broker"] = {
    "rogue_looted_prisoner": 2, "rogue_stole_reagents": 3, "rogue_runed_blade": 3,
    "rogue_pocketed_tear": 3, "rogue_sneaked": 2, "rogue_smooth_talk": 2,
    "rogue_found_cache": 2, "rogue_picked_locks": 1, "rogue_looted_shrine": 2,
    "rogue_outsmarted_rival": 2, "rogue_sensed_truth": 1,
    "trader_robbed": 1, "rival_defeated": 1, "vision_ignored": 1,
    "spared_prisoner": -1, "aided_village": -1, "refused_dark_pact": -2,
}
