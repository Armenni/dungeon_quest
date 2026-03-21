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
    "rest_hp": "Você encontra um recanto tranquilo para descansar. HP restaurado.",
    "rest_gold": "Você descobre um pequeno baú!",
    "rest_mp": "Você medita brevemente, restaurando MP.",
    "rest_potion": "Você encontra uma poção empoeirada.",
    "rest_none": "Você segue em frente...",
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

    # Story events
    "event1_title": "O Prisioneiro Moribundo",
    "event1_narrative": (
        "Ao pé da segunda escada você encontra um homem encostado na parede.\n"
        "Armadura real — destruída. Sua respiração é superficial. Ele abre um olho para você.\n"
        "\"Cultistas do Dragão,\" ele rosna. \"Me arrastaram para cá há dias.\n"
        "Eu sei coisas... sobre o Dragão... por favor...\""
    ),
    "event1_choice1_text": "Cuide de seus ferimentos e ouça.",
    "event1_choice1_outcome": (
        "Você usa o que tem. Sua respiração estabiliza. \"O Dragão,\" ele sussurra,\n"
        "\"nem sempre foi um monstro. Há textos antigos — a sábia no terceiro andar\n"
        "os tem. Confie nela.\" Ele pressiona seu anel de sinete em sua mão. +15 ouro, +10 HP máx."
    ),
    "event1_choice2_text": "Pergunte o que ele sabe e o deixe para trás.",
    "event1_choice2_outcome": (
        "Ele lhe conta o que pode entre respirações difíceis. Você memoriza\n"
        "e segue em frente. O destino dele é dele. Suas palavras aguçam sua determinação. +2 ATQ, +2 DEF."
    ),
    "event1_choice3_text": "Encerre seu sofrimento. Pegue seus pertences.",
    "event1_choice3_outcome": (
        "É uma misericórdia, você se diz. Você encontra algumas moedas e uma faca de caça\n"
        "na mochila dele. O calabouço não julga. +25 ouro, +3 ATQ."
    ),

    "event2_title": "Os Sobreviventes",
    "event2_narrative": (
        "Uma passagem lateral abre para um nicho apertado. Dentro: quatro aldeões — um fazendeiro,\n"
        "duas crianças, uma velha — agrupados ao redor de uma tocha quase apagada. Fugiram daqui\n"
        "quando o culto do Dragão queimou seus lares três dias atrás.\n"
        "\"Não nos resta nada,\" diz o fazendeiro. \"Mas tudo que pudermos dar — é seu.\""
    ),
    "event2_choice1_text": "Compartilhe suas poções e ofereça o que puder.",
    "event2_choice1_outcome": (
        "A velha pressiona cada moeda que têm em suas mãos.\n"
        "\"Deus te abençoe.\" O fazendeiro te dá seu amuleto da sorte — gasto mas ainda quente.\n"
        "Sua gratidão parece uma armadura. +20 ouro, +10 HP máx."
    ),
    "event2_choice2_text": "Deixe-os. Você tem sua própria missão.",
    "event2_choice2_outcome": (
        "Você passa sem uma palavra. Seus olhos te seguem no escuro.\n"
        "A culpa se endurece em algo útil. +4 ATQ."
    ),
    "event2_choice3_text": "Pegue os suprimentos deles. Eles não vão sair daqui mesmo.",
    "event2_choice3_outcome": (
        "Eles não resistem. Você encontra uma poção de cura e 35 de ouro escondidos\n"
        "no xale da velha. As crianças olham em silêncio. +35 ouro, +1 Poção de Cura."
    ),

    "event3_title": "O Acordo da Sábia",
    "event3_narrative": (
        "Uma figura encapuzada senta de pernas cruzadas no corredor, indiferente aos horrores do calabouço.\n"
        "Ela olha para você antes de falar. \"Eu estava esperando,\" ela diz simplesmente.\n"
        "\"Posso te dar poder suficiente para matar o que aguarda abaixo. Todo pacto tem um preço.\n"
        "Energia sombria flui por este lugar — ela quer um hospedeiro. Estou te oferecendo a escolha.\""
    ),
    "event3_choice1_text": "Recuse. Você não negocia com as trevas.",
    "event3_choice1_outcome": (
        "Ela acena lentamente. \"Bom. O Dragão sente a corrupção — teria\n"
        "só dificultado as coisas.\" Ela coloca a mão no seu peito e você sente\n"
        "algo quente se instalar dentro de você. +20 HP máx, +3 DEF."
    ),
    "event3_choice2_text": "Aceite o pacto sombrio.",
    "event3_choice2_outcome": (
        "Luz carmesim inunda suas veias. O poder é inebriante — e imediato.\n"
        "Algo que você não consegue nomear está faltando agora. Você sente no escuro.\n"
        "+10 ATQ, +8 Magia. HP máx -15."
    ),
    "event3_choice3_text": "Negocie — poder sem rendição total.",
    "event3_choice3_outcome": (
        "Ela ergue uma sobrancelha e ri. \"Pragmático.\" Você negocia\n"
        "um canal parcial — menos poder, menos custo. Uma troca justa.\n"
        "+4 ATQ, +4 Magia, +5 HP máx."
    ),

    "event4_title": "O Tomo Antigo",
    "event4_narrative": (
        "Antes da escada final, um púlpito de ferro fica sozinho em um círculo de\n"
        "tochas apagadas — mas de alguma forma acesas. Sobre ele: um tomo encadernado em couro de dragão.\n"
        "Suas páginas brilham levemente. Três passagens estão marcadas:\n"
        "uma sobre conhecimento, uma sobre sacrifício, uma sobre deixar as coisas como são."
    ),
    "event4_choice1_text": "Estude os segredos do tomo. Conhecimento é poder.",
    "event4_choice1_outcome": (
        "Horas parecem minutos. Você aprende o nome verdadeiro do Dragão,\n"
        "a frequência de suas escamas, a forma de sua alma.\n"
        "Você fecha o tomo uma pessoa diferente. +8 Magia, +10 HP máx."
    ),
    "event4_choice2_text": "Derrame sua vitalidade no tomo. Deixe-o amplificá-lo.",
    "event4_choice2_outcome": (
        "O tomo bebe de você. Você sente anos saírem do seu corpo —\n"
        "mas em troca, uma clareza terrível. Cada golpe vai contar.\n"
        "HP máx -30. +15 ATQ, +15 Magia."
    ),
    "event4_choice3_text": "Sele o tomo. Algum poder não deve ser tocado.",
    "event4_choice3_outcome": (
        "Você o fecha com força. O brilho some. O que estava dentro fica dentro.\n"
        "Você se sente mais firme por não ter olhado. +15 HP máx, +5 DEF."
    ),

    # Endings
    "ending_true_hero_title": "O Verdadeiro Herói",
    "ending_true_hero_desc": (
        "O Dragão hesita quando você desfere o golpe final — e algo muda em seus olhos.\n"
        "Não raiva. Reconhecimento.\n\n"
        "Ele abaixa a cabeça. A maldição se estilhaça como vidro. A besta à sua frente\n"
        "nunca foi um monstro — apenas um prisioneiro, como o homem que você salvou no primeiro andar.\n"
        "Ele se curva uma vez, então sobe pelo teto do calabouço ao céu aberto.\n\n"
        "O reino não entende o que você fez. Tudo bem.\n"
        "Você entende."
    ),
    "ending_true_hero_bonus": "O Dragão recua, sentindo sua alma pura. Sua virtude te protege. +10 DEF!",

    "ending_dark_conqueror_title": "O Conquistador das Sombras",
    "ending_dark_conqueror_desc": (
        "O Dragão cai. O pacto sombrio pulsa em suas veias — mais faminto agora.\n"
        "Você está no silêncio da câmara final, o Cristal da Luz em sua mão,\n"
        "e sente-o começar a escurecer.\n\n"
        "O reino tinha medo do Dragão.\n"
        "Eles aprenderão um novo medo.\n\n"
        "Você reivindica o calabouço como seu domínio. Os velhos estandartes queimam lindamente."
    ),
    "ending_dark_conqueror_bonus": "Espíritos das trevas surgem em você, atacando o Dragão!",

    "ending_scholar_king_title": "O Rei Erudito",
    "ending_scholar_king_desc": (
        "Você sussurra o nome verdadeiro do Dragão enquanto luta. Ele vacila.\n"
        "Você recita a frequência de suas escamas. Seu fogo diminui.\n"
        "Você pronuncia a forma de sua alma — e ele desmorona.\n\n"
        "Conhecimento sempre foi a arma mais afiada.\n\n"
        "Você emerge do calabouço carregando o tomo e o Cristal.\n"
        "Reinos são reconstruídos na verdade. Você pretende construir um."
    ),
    "ending_scholar_king_bonus": "Conhecimento antigo ressoa — sua magia acerta em cheio!",

    "ending_martyred_saint_title": "O Santo Mártir",
    "ending_martyred_saint_desc": (
        "Seu corpo falha uma vez durante a luta. Então os espíritos vêm —\n"
        "o prisioneiro, os aldeões, todos que o culto do Dragão já machucou.\n"
        "Eles fluem de volta para você. Mais uma vez.\n\n"
        "Quando termina, você mal está de pé. O Cristal se estilhaça sozinho.\n"
        "O calabouço fica silencioso pela primeira vez em um século.\n\n"
        "Eles vão construir uma estátua. Você não estará vivo para ver.\n"
        "Assim sempre seria."
    ),
    "ending_martyred_saint_bonus": "Espíritos dos caídos estão com você — uma última luta!",

    "ending_reluctant_hero_title": "O Herói Relutante",
    "ending_reluctant_hero_desc": (
        "O Dragão está morto. O reino está seguro. Você não sente nada em particular.\n\n"
        "Você não veio aqui por glória, ou vingança, ou justiça.\n"
        "Você veio porque alguém precisava.\n\n"
        "Você deixa o Cristal onde caiu e volta para a luz do dia.\n"
        "Ninguém sabe por que você fez isso. Você mal sabe.\n\n"
        "Isso basta."
    ),
}
