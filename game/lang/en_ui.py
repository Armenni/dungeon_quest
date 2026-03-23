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
    "class_warrior_desc": "High HP & Defense. [red]Battlecry[/red] — weakens enemies.",
    "class_mage_desc": "High Magic & MP. [blue]Fireball & Ice Shard[/blue].",
    "class_rogue_desc": "High Speed & Crit. [green]Backstab[/green] ability.",
    "enter_class_prompt": "Enter 1, 2, or 3: ",

    # Combat menu
    "actions_header": "── Actions ──",
    "action_attack": "Attack",
    "action_use_item": "Use Item",
    "action_help": "Help",
    "action_prompt": "Action (1-{n} or ?): ",
    "help_cmd": "?",

    # Combat help panel
    "help_title": "Combat Help",
    "help_actions_header": "── Your Actions ──",
    "help_attack_desc": "Strike with your weapon. Crit% = 5 + Luck×3. Dodge% = Agility×3.",
    "help_item_desc": "Use a potion or item from your inventory.",
    "help_status_header": "── Status Effects ──",
    "help_status_burn":     "Fire damage each turn until it expires.",
    "help_status_poison":   "Poison damage each turn until it expires.",
    "help_status_bleed":    "Bleeds for raw damage each turn, ignoring armor.",
    "help_status_stun":     "Lose your next turn entirely.",
    "help_status_weakened": "Your attacks deal reduced damage.",
    "help_status_shielded": "Absorbs 50% of the next hit you receive.",

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
    "player_dodged": "You dodge {name}'s attack!",
    "player_attack": "You attack for {dmg} damage!",
    "critical_hit": "CRITICAL HIT!",
    "player_cast": "You cast {name} for {dmg} damage!",
    "enemy_stunned": "{name} is stunned — loses its turn!",
    "dark_spirits": "Dark spirits strike {name} for {dmg}!",
    "revive": "The spirits revive you one last time!",
    "enemy_defeated": "{name} defeated!",
    "xp_gold": "+{xp} XP  +{gold} Gold",
    "level_up": "★  LEVEL UP! Now Level {level}!  ★",
    "item_drop": "Dropped: {name}!",

    # Rest events
    "rest_hp": "You find a quiet alcove to rest.",
    "rest_gold": "You discover a small chest!",
    "rest_mp": "You meditate briefly.",
    "rest_potion": "You find a dusty potion.",
    "rest_none": "You press onward through the dark.",
    "gained_hp": "+{n} HP",
    "gained_gold": "+{n} Gold",
    "gained_mp": "+{n} MP",
    "found_potion": "Found a {name}!",

    # Combat (combat.py)
    "not_enough_mp": "Not enough MP!",
    "battlecry_fx": "Your battle cry weakens the enemy! [dim]Weakened[/dim] for {dur} turns.",
    "frost_armor_fx": "You erect an arcane barrier! [blue]Shielded[/blue] for {dur} turns.",
    "enemy_is_stunned": " Enemy is [yellow]stunned[/yellow]!",
    "enemy_bleeding": " Enemy is [dark_red]bleeding[/dark_red]!",
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
    # Wraith — added by enemy-designer
    "ability_drain_mana": "[magenta]{name}[/magenta] drains your [cyan]mana[/cyan]! Lost {drained} MP, {name} heals {heal} HP!",
    "ability_life_steal": "[magenta]{name}[/magenta] strikes and drains your [red]life force[/red]! {dmg} and heals {heal} HP!",
    # Cultist — added by enemy-designer
    "ability_dark_ritual": "[magenta]{name}[/magenta] performs a dark ritual! Heals {heal} HP and gains strength!",
    "ability_shadow_bolt": "[magenta]{name}[/magenta] hurls shadow magic! {dmg} You are [dim]weakened[/dim]!",
    # Cave Spider — added by enemy-designer
    "ability_web_trap": "[bold]{name}[/bold] shoots sticky webs! You are [yellow]entangled[/yellow]!",
    # Stone Golem — added by enemy-designer
    "ability_rock_slam": "[bold]{name}[/bold] slams the ground! {dmg}",
    "ability_rock_slam_stun": "[bold]{name}[/bold] slams the ground! You are [yellow]stunned[/yellow]! {dmg}",
    "enemy_basic_attack": "{name} attacks! {dmg}",

    # Status effects (status.py)
    "status_poison": "Poison",
    "status_burn": "Burn",
    "status_bleed": "Bleed",
    "status_stun": "Stun",
    "status_weakened": "Weakened",
    "status_shielded": "Shielded",
    "deals_damage": "deals {n} damage!",
    "status_fades": "{name} fades.",

    # Level-up stat choice
    "level_up_choose_stat": "Choose a stat to raise (+1):",
    "level_up_stat_strength":     "1. Strength     (ATK +2)",
    "level_up_stat_intelligence": "2. Intelligence (MAGIC +4)",
    "level_up_stat_agility":      "3. Agility      (Dodge% +3)",
    "level_up_stat_luck":         "4. Luck         (Crit% +3)",
    "level_up_stat_charisma":     "5. Charisma     (Shop -5%)",
    "level_up_stat_prompt":       "Enter 1-5: ",
    "level_up_stat_raised":       "[bold]{stat}[/bold] raised to {val}!",

    # Primary stat names
    "stat_strength":     "Strength",
    "stat_intelligence": "Intelligence",
    "stat_agility":      "Agility",
    "stat_luck":         "Luck",
    "stat_charisma":     "Charisma",

    # Equip screen
    "equip_title": "⚔  Equipment  ⚔",
    "equip_slot_weapon": "Weapon",
    "equip_slot_armor":  "Armor",
    "equip_none": "[dim]none[/dim]",
    "equip_bag_header": "── Bag ──",
    "equip_bag_empty": "[dim]Empty[/dim]",
    "equip_prompt": "  [bold]e w/a <n>[/bold] Equip  [bold]u w/a[/bold] Unequip  [bold]d <n>[/bold] Drop  Enter=Done: ",
    "equip_done_cmd": "",
    "equip_invalid_cmd": "[red]Usage: e w/a <number>, u w/a, d <number>[/red]",
    "equip_no_item": "[red]No item at that slot.[/red]",
    "equip_wrong_slot": "[red]{name} cannot go in that slot.[/red]",
    "equip_dropped": "Dropped {name}.",
    "equip_unequipped": "Unequipped {name}.",

    # Shop bag
    "bought_to_bag": "Bought [bold]{name}[/bold] — added to bag. Equip it between floors.",

    # Save / Load
    "save_continue": "Continue",
    "save_new_game": "New Game",
    "save_prompt": "A save was found. [bold]C[/bold]ontinue or [bold]N[/bold]ew game? ",
    "save_continue_cmd": "c",
    "save_new_cmd": "n",
    "save_loaded": "Game loaded — welcome back, {name}!",
    "save_saved": "[dim]Game saved.[/dim]",

    # Player (player.py)
    "equipped": "Equipped [bold]{name}[/bold]!",
    "invalid_item": "Invalid item.",
    "item_used_hp": "Used {name}! Restored {val} HP.",
    "item_used_mp": "Used {name}! Restored {val} MP.",
    "item_used_elixir": "Used {name}! Restored {val} HP and 30 MP.",
    "item_used_cure": "Used {name}! Cured poison and burn.",
    "item_used_generic": "Used {name}.",

    # Shop (shop.py)
    "shop_leave_cmd": "l",
    "shop_sell_cmd":    "s",
    "shop_buy_cmd":     "b",
    "shop_prompt": "\nSelect a number to buy, [bold]S[/bold]ell, or [bold]L[/bold]eave: ",
    "shop_sell_prompt": "\nSelect a number to sell, [bold]B[/bold]uy, or [bold]L[/bold]eave: ",
    "not_enough_gold": "Not enough gold! You have {gold}g.",
    "bought_item": "Bought {name}!",
    "sell_mode_header": "── What will you sell? ──",
    "sell_item_line":   "{n}. {name}  →  {price}g",
    "sell_confirm":     "Sell {name} for {price}g? (y/n): ",
    "sell_confirm_cmd": "y",
    "sold_item":        "Sold {name} for {price}g.",
    "sell_nothing":     "Nothing to sell.",
    "sell_cancel":      "Kept your items.",
    "press_enter_shopping": "Press Enter to continue shopping...",
    "no_change": "no change",
    "merchant_title": "⚔  Travelling Merchant  ⚔",
    "shop_footer": "Weapon: {weapon}   Armor: {armor}   Gold: [yellow]{gold}g[/yellow]",
    "stat_atk": "ATK",
    "stat_def": "DEF",
    "stat_mag": "MAG",
    "stat_hp": "HP",
}
