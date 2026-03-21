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

    # Event 5 — The Corrupted Knight
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
        "His sword drops. He doesn't follow. +5 ATK. -15 HP."
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
        "In his belt: a coin purse and a knife still sharp. +30 gold, +4 ATK."
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
        "'Thank you,' he says. That's enough. +8 Magic, +10 max HP."
    ),
    "event5_rogue_text": "Slip through the shadows. He can't fight what he can't see.",
    "event5_rogue_outcome": (
        "You're three steps past him before he turns. He doesn't follow.\n"
        "Easy. Clean. Worth it. +4 ATK, +20 gold, +10 HP."
    ),

    # Event 6 — The Dragon's Tear
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
        "It warms your palm the entire walk to the door. You feel steadier than you have\n"
        "since the first floor. Whatever waits inside, you'll meet it as yourself.\n"
        "+25 max HP, +4 DEF."
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
        "You've never felt your power this clearly. +14 Magic, +5 max HP."
    ),
    "event6_rogue_text": "Pocket it. A tear from the Dragon — that's worth something.",
    "event6_rogue_outcome": (
        "Maybe to a scholar. Maybe just as a reminder. Either way, it's yours.\n"
        "+35 gold, +5 ATK, +3 Magic."
    ),

    # Prisoner return bonus
    "prisoner_returns": (
        "The man you saved on the first floor steps from a side passage.\n"
        "He looks better. Not good — but better.\n"
        "'I found a back route,' he says. 'Slower, but alive.'\n"
        "He presses something cold into your hand — a sealed vial and a coin purse.\n"
        "'You earned it.' Then he's gone."
    ),
    "prisoner_gift": "+10 Gold  +5 max HP  +Dragon Tears potion",

    # Shop weapons locked
    "shop_weapons_locked": (
        "The merchant's expression hardens as you approach the weapon rack.\n"
        "\"Word travels in dungeons. I knew the folk from that village.\"\n"
        "He steps in front of the weapons.\n"
        "\"Not for you. Take your potions and go.\""
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
