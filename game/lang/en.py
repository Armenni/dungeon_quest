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

    # Event 1 — class-specific choices
    "event1_warrior_text": "Stand guard over him until help can find him.",
    "event1_warrior_outcome": (
        "You take a knee and draw your shield. Hours pass without movement.\n"
        "When you finally rise, he's still breathing — steadier now.\n"
        "The vigil steadied you too. +4 DEF, +10 max HP."
    ),
    "event1_mage_text": "Mend his wounds with a healing spell.",
    "event1_mage_outcome": (
        "The spell costs more than expected — his injuries run deep.\n"
        "But his colour returns. He clutches your sleeve: 'The sage ahead. Find her.\n"
        "She knows things.' +3 Magic. Max HP -5."
    ),
    "event1_rogue_text": "Check his belongings quietly while he drifts in and out.",
    "event1_rogue_outcome": (
        "He doesn't notice — or chooses not to.\n"
        "Hidden inside his boot: a coin purse and a worn throwing knife.\n"
        "You leave without a word. +25 gold, +2 ATK."
    ),

    # Event 2 — class-specific choices
    "event2_warrior_text": "Swear on your sword that you'll return for them.",
    "event2_warrior_outcome": (
        "The farmer grabs your forearm. 'Hold to that.'\n"
        "The children look at you like something worth believing in.\n"
        "The weight settles like a second layer of armour. +15 max HP, +2 ATK."
    ),
    "event2_mage_text": "Ward the alcove. Monsters won't notice them.",
    "event2_mage_outcome": (
        "The runes seal around the doorframe. The old woman traces them with one finger.\n"
        "'These are real.' You leave knowing at least this much will hold.\n"
        "+5 Magic, +5 max HP."
    ),
    "event2_rogue_text": "Leave a smoke vial and a few coins. Enough for a chance.",
    "event2_rogue_outcome": (
        "You don't linger. The farmer nods once — thanks without debt.\n"
        "In the dark after, you move lighter. Faster. +4 ATK, +2 DEF."
    ),

    # Event 3 — class-specific choices
    "event3_warrior_text": "Propose a test of will. Power through endurance, not pacts.",
    "event3_warrior_outcome": (
        "She obliges, grimly. You outlast something that would shatter a lesser mind.\n"
        "When it ends she looks at you differently. 'Good. That was the real test.'\n"
        "+7 ATK, +3 DEF, +5 max HP."
    ),
    "event3_mage_text": "Debate the theory. There may be a better formulation.",
    "event3_mage_outcome": (
        "Two hours of arcane argument. She concedes three of your points.\n"
        "What you walk away with is not what she offered — it's more precise.\n"
        "+9 Magic, +2 ATK."
    ),
    "event3_rogue_text": "Listen carefully. Help yourself to a few reagents while she talks.",
    "event3_rogue_outcome": (
        "She knows. She lets it happen — a test you didn't know you were taking.\n"
        "'Pragmatic,' she says, with something close to approval.\n"
        "The reagents burn bright later. +20 gold, +3 ATK, +3 Magic."
    ),

    # Event 4 — class-specific choices
    "event4_warrior_text": "Tear out the key pages. Practical battle intelligence.",
    "event4_warrior_outcome": (
        "You roll the pages tight and tuck them into your armour.\n"
        "Attack patterns. Weak points. You won't understand the theory — you don't need to.\n"
        "+9 ATK, +4 DEF."
    ),
    "event4_mage_text": "Channel the tome's resonance directly. Skip the reading.",
    "event4_mage_outcome": (
        "White light. Seconds pass. When you look up, you know things you didn't before —\n"
        "not as words, but as shapes. The shapes of power. +13 Magic."
    ),
    "event4_rogue_text": "Copy the key runes onto your blade by torchlight.",
    "event4_rogue_outcome": (
        "The runes settle into the metal like they were always there.\n"
        "You don't know what they mean. They do. +7 ATK, +4 Magic."
    ),

    # Event 5 — The Corrupted Knight (new, floor 5)
    "event5_title": "The Corrupted Knight",
    "event5_narrative": (
        "A knight in cracked obsidian armour stands between you and the staircase.\n"
        "His sword is raised — but his eyes are hollow. Royal insignia on the pauldron:\n"
        "House Valdris. The family that sent their heir to slay the Dragon\n"
        "twenty years ago. He never came back.\n"
        "\"...turn... back...\" he grinds out. He does not lower his sword."
    ),
    "event5_choice1_text": "Fight your way through him.",
    "event5_choice1_outcome": (
        "You clash twice. He's stronger than he looks — you take a hit before you break through.\n"
        "His sword drops. He doesn't follow. Whatever was left of him accepts it.\n"
        "+5 ATK. -15 HP."
    ),
    "event5_choice2_text": "Speak to what remains of him.",
    "event5_choice2_outcome": (
        "You lower your weapon and say his name — House Valdris. Something flickers.\n"
        "His sword hand shakes. He crumbles to one knee.\n"
        "'Don't... let it end the same way.' You pass in silence. +15 max HP, +3 DEF."
    ),
    "event5_choice3_text": "End it quickly. It's a mercy.",
    "event5_choice3_outcome": (
        "One stroke. Clean. He exhales — not in pain, but relief.\n"
        "In his belt: a coin purse and a knife still sharp. You take them and press on.\n"
        "+30 gold, +4 ATK."
    ),
    "event5_warrior_text": "Recognize a soldier's stance. Challenge him to one last honorable duel.",
    "event5_warrior_outcome": (
        "He accepts — the last reflex of a trained fighter.\n"
        "You meet him blow for blow, honouring the fight even as you end it.\n"
        "Something settles in you both. +6 ATK, +4 DEF, +10 max HP."
    ),
    "event5_mage_text": "Attempt a purification ritual. Whatever curse took him, name it.",
    "event5_mage_outcome": (
        "The corruption resists — then fractures. He gasps. The hollow look fades.\n"
        "He can't move, but he can see you clearly.\n"
        "'Thank you,' he says. That's enough. +8 Magic, +10 max HP."
    ),
    "event5_rogue_text": "Slip through the shadows. He can't fight what he can't see.",
    "event5_rogue_outcome": (
        "You're three steps past him before he turns.\n"
        "He doesn't follow — some instinct tells him the chase isn't worth it.\n"
        "Easy. Clean. Worth it. +4 ATK, +20 gold, +10 HP."
    ),

    # Event 6 — The Dragon's Tear (new, floor 6)
    "event6_title": "The Dragon's Tear",
    "event6_narrative": (
        "On the last step before the final door, a single crystalline drop rests on the stone.\n"
        "Warm to the touch. It glows softly — not with magic, but with something older.\n"
        "The Dragon shed this here. Not from rage. Not from pain.\n"
        "A hundred years of captivity can break anything, given enough time.\n"
        "You pick it up. What you do with it is yours to decide."
    ),
    "event6_choice1_text": "Shatter it against your blade. A weapon is a weapon.",
    "event6_choice1_outcome": (
        "The drop fractures into the metal with a hiss of light.\n"
        "Power without sentiment. You'll take it. +6 ATK, +6 Magic."
    ),
    "event6_choice2_text": "Hold it close. Some things should stay whole.",
    "event6_choice2_outcome": (
        "It warms your palm the entire walk to the door.\n"
        "You feel steadier than you have since the first floor.\n"
        "Whatever waits inside, you'll meet it as yourself. +25 max HP, +4 DEF."
    ),
    "event6_choice3_text": "Drink it. Let the Dragon's grief become your strength.",
    "event6_choice3_outcome": (
        "It burns going down — not like fire, but like memory.\n"
        "Something vast and old and sad. You understand the Dragon now.\n"
        "You'll still kill it. +8 ATK, +8 Magic. Max HP -10."
    ),
    "event6_warrior_text": "Press it into the grip of your weapon. Let it anchor you.",
    "event6_warrior_outcome": (
        "It melts into the metal with a low sound you feel more than hear.\n"
        "Your grip is steadier than it's ever been. +10 ATK, +5 DEF."
    ),
    "event6_mage_text": "Absorb it slowly into your magic core. A perfect conduit.",
    "event6_mage_outcome": (
        "The magic in it recognises yours and flows to meet it.\n"
        "You've never felt your power this clearly. This is what it's supposed to feel like.\n"
        "+14 Magic, +5 max HP."
    ),
    "event6_rogue_text": "Pocket it. A tear from the Dragon — that's worth something.",
    "event6_rogue_outcome": (
        "Maybe to a scholar. Maybe to a cult. Maybe just as a reminder.\n"
        "Either way, it's yours now. +35 gold, +5 ATK, +3 Magic."
    ),

    # Prisoner return bonus (floor 3, if spared on floor 1)
    "prisoner_returns": (
        "The man you saved on the first floor steps from a side passage.\n"
        "He looks better. Not good — but better.\n"
        "'I found a back route,' he says. 'Slower, but alive.'\n"
        "He presses something cold into your hand — a sealed vial and a coin purse.\n"
        "'You earned it.' Then he's gone."
    ),
    "prisoner_gift": "+10 Gold  +5 max HP  +Dragon Tears potion",

    # Shop weapons locked (looted_village consequence)
    "shop_weapons_locked": (
        "The merchant's expression hardens as you approach the weapon rack.\n"
        "\"Word travels in dungeons. I knew the folk from that village.\"\n"
        "He steps in front of the weapons.\n"
        "\"Not for you. Take your potions and go.\""
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
