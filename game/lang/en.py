STRINGS: dict = {
    # UI
    "subtitle": "A Turn-Based Fantasy RPG",
    "press_enter": "Press Enter to continue...",
    "press_enter_short": "Press Enter...",
    "invalid": "[red]Invalid.[/red]",
    "invalid_choice": "[red]Invalid choice.[/red]",

    # Language selection (in main.py — plain text, no Rich)
    "lang_prompt": "Select language / Selecione o idioma:\n  1. English\n  2. Português (BR)\n> ",
    "enter_name": "Enter your hero's name: ",
    "default_name": "Hero",

    # Class selection
    "choose_class": "Choose your class:",
    "class_warrior_desc": "High HP & Defense. [red]Battlecry[/red] ability.",
    "class_mage_desc": "High Magic & MP. [blue]Fireball & Ice Shard[/blue].",
    "class_rogue_desc": "High Speed & Crit. [green]Backstab[/green] ability.",
    "enter_class_prompt": "Enter 1, 2, or 3: ",

    # Combat menu
    "actions_header": "── Actions ──",
    "action_attack": "Attack",
    "action_use_item": "Use Item",
    "action_run": "Run",
    "action_prompt": "Action (1-{n}): ",

    # Inventory
    "no_items": "[yellow]No items![/yellow]",
    "inventory_header": "\n[bold]Inventory:[/bold]",
    "cancel_option": "  [dim]0. Cancel[/dim]",
    "use_item_prompt": "Use item: ",

    # Floor
    "floor_label": "  Floor {floor} of {max}  ",
    "floor_subtitle": "The dungeon deepens...",
    "floor_final_subtitle": "The final chamber awaits...",

    # Story
    "story_choice_prompt": "Your choice (1-{n}): ",

    # End screens
    "game_over": "GAME OVER",
    "player_fallen": "{name} has fallen in the dungeon.",
    "reached_level": "Reached Level",
    "gold_collected": "Gold collected:",
    "defeated_title": "☠  Defeated  ☠",
    "dungeon_cleared": "DUNGEON CLEARED",
    "victory": "★  VICTORY!  ★",
    "slain_dragon": "{name} has slain the Dragon!",
    "final_level": "Final Level:",
    "gold_label": "Gold:",

    # Dungeon messages
    "welcome": "Welcome, {name} the {cls}!",
    "dungeon_intro": "You descend into the dungeon seeking glory and treasure...",
    "floor_explore": "Floor {floor} — Press Enter to explore...",
    "enemy_appears": "A wild [bold]{name}[/bold] appears!",
    "boss_rumble": "A massive rumble shakes the walls...",
    "prepare_dragon": "Prepare yourself — Press Enter to face the Dragon...",
    "floor_cleared": "You cleared Floor {floor}!",
    "story_event_hint": "Something catches your eye — Press Enter...",
    "shop_hint": "A merchant blocks the passage — Press Enter to visit...",
    "descend": "Descend deeper — Press Enter...",

    # Combat log
    "player_stunned": "You are stunned — lose your turn!",
    "player_attack": "You attack for {dmg} damage!",
    "critical_hit": "CRITICAL HIT!",
    "player_cast": "You cast {name} for {dmg} damage!",
    "fled": "You fled from battle!",
    "escape_failed": "You failed to escape!",
    "enemy_stunned": "{name} is stunned — loses its turn!",
    "dark_spirits": "Dark spirits strike {name} for {dmg}!",
    "revive": "The spirits revive you one last time!",
    "enemy_defeated": "{name} defeated!",
    "xp_gold": "+{xp} XP  +{gold} Gold",
    "level_up": "★  LEVEL UP! Now Level {level}!  ★",
    "item_drop": "Dropped: {name}!",

    # Rest events
    "rest_hp": "You find a quiet alcove to rest. Restored some HP.",
    "rest_gold": "You discover a small chest!",
    "rest_mp": "You meditate briefly, restoring MP.",
    "rest_potion": "You find a dusty potion.",
    "rest_none": "You press onward...",
    "gained_hp": "+{n} HP",
    "gained_gold": "+{n} Gold",
    "gained_mp": "+{n} MP",
    "found_potion": "Found a {name}!",

    # Combat (combat.py)
    "not_enough_mp": "Not enough MP!",
    "frost_armor_fx": "You erect an arcane barrier! [blue]Shielded[/blue] for {dur} turns.",
    "enemy_is_stunned": " Enemy is [yellow]stunned[/yellow]!",
    "enemy_affected": " Enemy is [red]{etype}ed[/red]!",
    "take_damage": "You take {dmg} damage!",
    "damage_absorbed": "[{n} absorbed]",

    # Enemy abilities
    "ability_heavy_strike": "{name} uses Heavy Strike! {dmg}",
    "ability_bone_throw": "{name} throws a bone! {dmg}",
    "ability_fireball": "{name} casts Fireball! You are [red]burning[/red]! {dmg}",
    "ability_fire_breath": "{name} breathes fire! You are [red]burning[/red]! {dmg}",
    "ability_tail_swipe": "{name} swings its tail! {dmg}",
    "ability_regenerate": "{name} regenerates {heal} HP!",
    "ability_venom": "{name} injects venom! You are [green]poisoned[/green]! {dmg}",
    "ability_sting": "{name} stings! {dmg}",
    "ability_curse": "{name} casts a curse! You are [dim]weakened[/dim]!",
    "ability_stun_bash": "{name} slams you! You are [yellow]stunned[/yellow]! {dmg}",
    "ability_toxic_breath": "{name} breathes toxic fumes! You are [green]poisoned[/green]! {dmg}",
    "ability_wing_stun": "{name} beats its wings, [yellow]disorienting[/yellow] you!",
    "enemy_basic_attack": "{name} attacks! {dmg}",

    # Status effects (status.py)
    "status_poison": "Poison",
    "status_burn": "Burn",
    "status_stun": "Stun",
    "status_weakened": "Weakened",
    "status_shielded": "Shielded",
    "deals_damage": "deals {n} damage!",
    "status_fades": "{name} fades.",

    # Player (player.py)
    "equipped": "Equipped [bold]{name}[/bold]!",
    "invalid_item": "Invalid item.",
    "item_used_hp": "Used {name}! Restored {val} HP.",
    "item_used_mp": "Used {name}! Restored {val} MP.",
    "item_used_elixir": "Used {name}! Restored {val} HP and 30 MP.",
    "item_used_cure": "Used {name}! Cured poison and burn.",
    "item_used_generic": "Used {name}.",

    # Shop (shop.py)
    "shop_prompt": "\nBuy (number) or [bold]L[/bold] to leave: ",
    "not_enough_gold": "Not enough gold! You have {gold}g.",
    "bought_item": "Bought {name}!",
    "press_enter_shopping": "Press Enter to continue shopping...",
    "no_change": "no change",
    "merchant_title": "⚔  Travelling Merchant  ⚔",
    "shop_footer": "Weapon: {weapon}   Armor: {armor}   Gold: [yellow]{gold}g[/yellow]",
    "stat_atk": "ATK",
    "stat_def": "DEF",
    "stat_mag": "MAG",
    "stat_hp": "HP",

    # Story events
    "event1_title": "The Dying Prisoner",
    "event1_narrative": (
        "At the foot of the second staircase you find a man slumped against the wall.\n"
        "Royal armour — shredded. His breathing is shallow. He opens one eye at you.\n"
        "\"Dragon cultists,\" he rasps. \"They dragged me down here days ago.\n"
        "I know things... about the Dragon... please...\""
    ),
    "event1_choice1_text": "Tend to his wounds and listen.",
    "event1_choice1_outcome": (
        "You use what you have. His breathing steadies. \"The Dragon,\" he whispers,\n"
        "\"was not always a monster. There are old texts — the sage on floor three\n"
        "has them. Trust her.\" He presses his signet ring into your hand. +15 gold, +10 max HP."
    ),
    "event1_choice2_text": "Ask what he knows, then leave him.",
    "event1_choice2_outcome": (
        "He tells you what he can between ragged breaths. You memorise it\n"
        "and walk on. His fate is his own. His words sharpen your resolve. +2 ATK, +2 DEF."
    ),
    "event1_choice3_text": "End his suffering. Take his belongings.",
    "event1_choice3_outcome": (
        "It's a mercy, you tell yourself. You find a few coins and a hunting knife\n"
        "in his pack. The dungeon does not judge. +25 gold, +3 ATK."
    ),

    "event2_title": "The Survivors",
    "event2_narrative": (
        "A side passage opens into a cramped alcove. Inside: four villagers — a farmer,\n"
        "two children, an old woman — huddled around a dying torch. They fled here\n"
        "when the Dragon's cult burned their homes three days ago.\n"
        "\"We have nothing left,\" the farmer says. \"But anything we can give — it's yours.\""
    ),
    "event2_choice1_text": "Share your potions and offer them what you can.",
    "event2_choice1_outcome": (
        "The old woman presses every coin they have into your hands.\n"
        "\"Bless you.\" The farmer gives you his lucky charm — worn smooth\n"
        "but still warm. Their gratitude feels like armour. +20 gold, +10 max HP."
    ),
    "event2_choice2_text": "Leave them. You have your own mission.",
    "event2_choice2_outcome": (
        "You walk past without a word. Their eyes follow you into the dark.\n"
        "The guilt hardens into something useful. +4 ATK."
    ),
    "event2_choice3_text": "Take their supplies. They won't make it out anyway.",
    "event2_choice3_outcome": (
        "They don't resist. You find a health potion and 35 gold hidden\n"
        "in the old woman's shawl. The children stare in silence. +35 gold, +1 Health Potion."
    ),

    "event3_title": "The Sage's Bargain",
    "event3_narrative": (
        "A robed figure sits cross-legged in the corridor, unbothered by the dungeon's horrors.\n"
        "She looks up before you speak. \"I've been waiting,\" she says simply.\n"
        "\"I can give you power enough to kill what waits below. All pacts have a price.\n"
        "Dark energy flows through this place — it wants a host. I'm offering you the choice.\""
    ),
    "event3_choice1_text": "Refuse. You don't deal in darkness.",
    "event3_choice1_outcome": (
        "She nods slowly. \"Good. The Dragon senses corruption — it would have\n"
        "only made things harder.\" She places a hand on your chest and you feel\n"
        "something warm settle inside you. +20 max HP, +3 DEF."
    ),
    "event3_choice2_text": "Accept the dark pact.",
    "event3_choice2_outcome": (
        "Crimson light floods your veins. The power is intoxicating — and immediate.\n"
        "Something you can't name is missing now. You feel it in the dark.\n"
        "+10 ATK, +8 Magic. Max HP -15."
    ),
    "event3_choice3_text": "Bargain — power without full surrender.",
    "event3_choice3_outcome": (
        "She raises an eyebrow, then laughs. \"Pragmatic.\" You negotiate\n"
        "a partial conduit — less power, less cost. A fair trade.\n"
        "+4 ATK, +4 Magic, +5 max HP."
    ),

    "event4_title": "The Ancient Tome",
    "event4_narrative": (
        "Before the final staircase, an iron lectern stands alone in a circle of\n"
        "dead torches — somehow lit. On it: a tome bound in dragonhide.\n"
        "Its pages glow faintly. Three passages are bookmarked:\n"
        "one on knowledge, one on sacrifice, one on letting things be."
    ),
    "event4_choice1_text": "Study the tome's secrets. Knowledge is power.",
    "event4_choice1_outcome": (
        "Hours feel like minutes. You learn the Dragon's true name,\n"
        "the frequency of its scales, the shape of its soul.\n"
        "You close the tome a different person. +8 Magic, +10 max HP."
    ),
    "event4_choice2_text": "Pour your vitality into the tome. Let it amplify you.",
    "event4_choice2_outcome": (
        "The tome drinks from you. You feel years leave your body —\n"
        "but in exchange, a terrible clarity. Every strike will count.\n"
        "Max HP -30. +15 ATK, +15 Magic."
    ),
    "event4_choice3_text": "Seal the tome. Some power shouldn't be touched.",
    "event4_choice3_outcome": (
        "You slam it shut. The glow dies. Whatever was inside stays inside.\n"
        "You feel steadier for not having looked. +15 max HP, +5 DEF."
    ),

    # Endings
    "ending_true_hero_title": "The True Hero",
    "ending_true_hero_desc": (
        "The Dragon pauses as you deal the final blow — and something shifts in its eyes.\n"
        "Not rage. Recognition.\n\n"
        "It lowers its head. The curse shatters like glass. The beast before you\n"
        "was never a monster — just a prisoner, like the man you saved on the first floor.\n"
        "It bows once, then rises through the dungeon ceiling into open sky.\n\n"
        "The kingdom does not understand what you did. That's alright.\n"
        "You do."
    ),
    "ending_true_hero_bonus": "The Dragon recoils, sensing your uncorrupted soul. Your virtue shields you. +10 DEF!",

    "ending_dark_conqueror_title": "The Shadow Conqueror",
    "ending_dark_conqueror_desc": (
        "The Dragon falls. The dark pact pulses in your veins — hungrier now.\n"
        "You stand in the silence of the final chamber, the Crystal of Light in your hand,\n"
        "and feel it begin to darken.\n\n"
        "The kingdom was afraid of the Dragon.\n"
        "They will learn a new fear.\n\n"
        "You claim the dungeon as your domain. The old banners burn beautifully."
    ),
    "ending_dark_conqueror_bonus": "Dark spirits surge through you, striking the Dragon!",

    "ending_scholar_king_title": "The Scholar King",
    "ending_scholar_king_desc": (
        "You whisper the Dragon's true name as you fight. It falters.\n"
        "You recite the frequency of its scales. Its fire dims.\n"
        "You speak the shape of its soul — and it crumbles.\n\n"
        "Knowledge was always the sharpest weapon.\n\n"
        "You emerge from the dungeon carrying the tome and the Crystal.\n"
        "Kingdoms are rebuilt on truth. You intend to build one."
    ),
    "ending_scholar_king_bonus": "Ancient knowledge resonates — your magic strikes true!",

    "ending_martyred_saint_title": "The Martyred Saint",
    "ending_martyred_saint_desc": (
        "Your body gives out once during the fight. Then the spirits come —\n"
        "the prisoner, the villagers, everyone the Dragon's cult ever hurt.\n"
        "They pour back into you. One more time.\n\n"
        "When it ends, you are barely standing. The Crystal shatters on its own.\n"
        "The dungeon goes quiet for the first time in a century.\n\n"
        "They will build a statue. You will not be alive to see it.\n"
        "That's how it was always going to end."
    ),
    "ending_martyred_saint_bonus": "Spirits of the fallen stand with you — one last fight!",

    "ending_reluctant_hero_title": "The Reluctant Hero",
    "ending_reluctant_hero_desc": (
        "The Dragon is dead. The kingdom is safe. You feel nothing in particular.\n\n"
        "You didn't come here for glory, or vengeance, or righteousness.\n"
        "You came because someone had to.\n\n"
        "You leave the Crystal where it fell and walk back into daylight.\n"
        "Nobody knows why you did it. You barely do.\n\n"
        "That's enough."
    ),
}
