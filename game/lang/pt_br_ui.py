STRINGS: dict = {
    # UI
    "subtitle": "Um RPG de Fantasia por Turnos",
    "press_enter": "Pressione Enter para continuar...",
    "press_enter_short": "Pressione Enter...",
    "invalid": "[red]Inválido.[/red]",
    "invalid_choice": "[red]Escolha inválida.[/red]",

    # Language selection
    "lang_prompt": "Select language / Selecione o idioma:\n  1. English\n  2. Português (BR)\n> ",
    "enter_name": "Digite o nome do seu herói: ",
    "default_name": "Herói",

    # Class selection
    "choose_class": "Escolha sua classe:",
    "class_warrior_desc": "Alto HP e Defesa. Habilidade [red]Grito de Guerra[/red].",
    "class_mage_desc": "Alta Magia e MP. [blue]Bola de Fogo e Shard de Gelo[/blue].",
    "class_rogue_desc": "Alta Velocidade e Crítico. Habilidade [green]Golpe nas Sombras[/green].",
    "enter_class_prompt": "Digite 1, 2 ou 3: ",

    # Combat menu
    "actions_header": "── Ações ──",
    "action_attack": "Atacar",
    "action_use_item": "Usar Item",
    "action_run": "Fugir",
    "action_prompt": "Ação (1-{n}): ",

    # Inventory
    "no_items": "[yellow]Sem itens![/yellow]",
    "inventory_header": "\n[bold]Inventário:[/bold]",
    "cancel_option": "  [dim]0. Cancelar[/dim]",
    "use_item_prompt": "Usar item: ",

    # Floor
    "floor_label": "  Andar {floor} de {max}  ",
    "floor_subtitle": "O calabouço se aprofunda...",
    "floor_final_subtitle": "A câmara final aguarda...",

    # Story
    "story_choice_prompt": "Sua escolha (1-{n}): ",

    # End screens
    "game_over": "FIM DE JOGO",
    "player_fallen": "{name} caiu no calabouço.",
    "reached_level": "Nível alcançado",
    "gold_collected": "Ouro coletado:",
    "defeated_title": "☠  Derrotado  ☠",
    "dungeon_cleared": "CALABOUÇO LIMPO",
    "victory": "★  VITÓRIA!  ★",
    "slain_dragon": "{name} derrotou o Dragão!",
    "final_level": "Nível Final:",
    "gold_label": "Ouro:",

    # Dungeon messages
    "welcome": "Bem-vindo, {name} o(a) {cls}!",
    "dungeon_intro": "Você desce ao calabouço em busca de glória e tesouro...",
    "floor_explore": "Andar {floor} — Pressione Enter para explorar...",
    "enemy_appears": "Um(a) [bold]{name}[/bold] selvagem aparece!",
    "boss_rumble": "Um tremor enorme sacode as paredes...",
    "prepare_dragon": "Prepare-se — Pressione Enter para enfrentar o Dragão...",
    "floor_cleared": "Você limpou o Andar {floor}!",
    "story_event_hint": "Algo chama sua atenção — Pressione Enter...",
    "shop_hint": "Um mercador bloqueia a passagem — Pressione Enter para visitar...",
    "descend": "Desça mais fundo — Pressione Enter...",

    # Combat log
    "player_stunned": "Você está atordoado — perde seu turno!",
    "player_attack": "Você ataca causando {dmg} de dano!",
    "critical_hit": "GOLPE CRÍTICO!",
    "player_cast": "Você lança {name} causando {dmg} de dano!",
    "fled": "Você fugiu da batalha!",
    "escape_failed": "Você falhou em escapar!",
    "enemy_stunned": "{name} está atordoado — perde seu turno!",
    "dark_spirits": "Espíritos das trevas atacam {name} causando {dmg}!",
    "revive": "Os espíritos te revivem pela última vez!",
    "enemy_defeated": "{name} derrotado!",
    "xp_gold": "+{xp} XP  +{gold} Ouro",
    "level_up": "★  SUBIU DE NÍVEL! Agora Nível {level}!  ★",
    "item_drop": "Caiu: {name}!",

    # Rest events
    "rest_hp": "Você encontra um recanto tranquilo para descansar.",
    "rest_gold": "Você descobre um pequeno baú!",
    "rest_mp": "Você medita brevemente.",
    "rest_potion": "Você encontra uma poção empoeirada.",
    "rest_none": "Você segue em frente pela escuridão.",
    "gained_hp": "+{n} HP",
    "gained_gold": "+{n} Ouro",
    "gained_mp": "+{n} MP",
    "found_potion": "Encontrou {name}!",

    # Combat (combat.py)
    "not_enough_mp": "MP insuficiente!",
    "frost_armor_fx": "Você ergue uma barreira arcana! [blue]Escudado[/blue] por {dur} turnos.",
    "enemy_is_stunned": " O inimigo está [yellow]atordoado[/yellow]!",
    "enemy_affected": " O inimigo está [red]{etype}[/red]!",
    "take_damage": "Você recebe {dmg} de dano!",
    "damage_absorbed": "[{n} absorvido]",

    # Enemy abilities
    "ability_heavy_strike": "{name} usa Golpe Pesado! {dmg}",
    "ability_bone_throw": "{name} arremessa um osso! {dmg}",
    "ability_fireball": "{name} lança Bola de Fogo! Você está [red]em chamas[/red]! {dmg}",
    "ability_fire_breath": "{name} cospe fogo! Você está [red]em chamas[/red]! {dmg}",
    "ability_tail_swipe": "{name} balança sua cauda! {dmg}",
    "ability_regenerate": "{name} regenera {heal} HP!",
    "ability_venom": "{name} injeta veneno! Você está [green]envenenado[/green]! {dmg}",
    "ability_sting": "{name} ferrou! {dmg}",
    "ability_curse": "{name} lança uma maldição! Você está [dim]enfraquecido[/dim]!",
    "ability_stun_bash": "{name} te golpeia! Você está [yellow]atordoado[/yellow]! {dmg}",
    "ability_toxic_breath": "{name} sopra fumaça tóxica! Você está [green]envenenado[/green]! {dmg}",
    "ability_wing_stun": "{name} bate as asas, te [yellow]desorientando[/yellow]!",
    # Wraith — added by enemy-designer
    "ability_drain_mana": "[magenta]{name}[/magenta] drena sua [cyan]mana[/cyan]! Perdeu {drained} MP, {name} cura {heal} HP!",
    "ability_life_steal": "[magenta]{name}[/magenta] ataca e drena sua [red]força vital[/red]! {dmg} e cura {heal} HP!",
    # Cultist — added by enemy-designer
    "ability_dark_ritual": "[magenta]{name}[/magenta] realiza um ritual obscuro! Cura {heal} HP e ganha força!",
    "ability_shadow_bolt": "[magenta]{name}[/magenta] arremessa magia das sombras! {dmg} Você está [dim]enfraquecido[/dim]!",
    "enemy_basic_attack": "{name} ataca! {dmg}",

    # Status effects (status.py)
    "status_poison": "Veneno",
    "status_burn": "Queimadura",
    "status_stun": "Atordoamento",
    "status_weakened": "Enfraquecido",
    "status_shielded": "Escudado",
    "deals_damage": "causa {n} de dano!",
    "status_fades": "{name} desaparece.",

    # Player (player.py)
    "equipped": "Equipado [bold]{name}[/bold]!",
    "invalid_item": "Item inválido.",
    "item_used_hp": "Usou {name}! Restaurou {val} HP.",
    "item_used_mp": "Usou {name}! Restaurou {val} MP.",
    "item_used_elixir": "Usou {name}! Restaurou {val} HP e 30 MP.",
    "item_used_cure": "Usou {name}! Curou veneno e queimadura.",
    "item_used_generic": "Usou {name}.",

    # Shop (shop.py)
    "shop_leave_cmd": "s",
    "shop_prompt": "\nComprar (número) ou [bold]S[/bold] para sair: ",
    "not_enough_gold": "Ouro insuficiente! Você tem {gold} de ouro.",
    "bought_item": "Comprou {name}!",
    "press_enter_shopping": "Pressione Enter para continuar comprando...",
    "no_change": "sem alteração",
    "merchant_title": "⚔  Mercador Viajante  ⚔",
    "shop_footer": "Arma: {weapon}   Armadura: {armor}   Ouro: [yellow]{gold}[/yellow]",
    "stat_atk": "ATQ",
    "stat_def": "DEF",
    "stat_mag": "MAG",
    "stat_hp": "HP",
}
