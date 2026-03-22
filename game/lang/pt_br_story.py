STRINGS: dict = {
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

    # Event 1 — escolhas específicas de classe
    "event1_warrior_text": "Faça a guarda dele até que ajuda possa encontrá-lo.",
    "event1_warrior_outcome": (
        "Você dobra um joelho e ergue seu escudo. Horas passam sem movimento.\n"
        "Quando você finalmente se levanta, ele ainda respira — mais estável agora.\n"
        "A vigília também te estabilizou. +4 DEF, +10 HP máx."
    ),
    "event1_mage_text": "Cure seus ferimentos com um feitiço de cura.",
    "event1_mage_outcome": (
        "O feitiço custa mais do que o esperado — seus ferimentos são profundos.\n"
        "Mas a cor volta ao rosto dele. Ele agarra sua manga: 'A sábia à frente. Encontre-a.\n"
        "Ela sabe de coisas.' +3 Magia. HP máx -5."
    ),
    "event1_rogue_text": "Revire seus pertences em silêncio enquanto ele vai e vem da consciência.",
    "event1_rogue_outcome": (
        "Ele não nota — ou finge não notar.\n"
        "Escondido dentro da bota: uma bolsa de moedas e uma faca de arremesso gasta.\n"
        "Você vai embora sem uma palavra. +25 ouro, +2 ATQ."
    ),

    # Event 2 — escolhas específicas de classe
    "event2_warrior_text": "Jure pela sua espada que voltará por eles.",
    "event2_warrior_outcome": (
        "O fazendeiro segura seu antebraço. 'Cumpra isso.'\n"
        "As crianças olham para você como algo em que vale a pena acreditar.\n"
        "O peso se instala como uma segunda camada de armadura. +15 HP máx, +2 ATQ."
    ),
    "event2_mage_text": "Proteja o recanto com runas. Monstros não os notarão.",
    "event2_mage_outcome": (
        "As runas selam ao redor da porta. A velha as traça com um dedo.\n"
        "'São reais.' Você vai embora sabendo que pelo menos isso vai segurar.\n"
        "+5 Magia, +5 HP máx."
    ),
    "event2_rogue_text": "Deixe um frasco de fumaça e algumas moedas. O suficiente para uma chance.",
    "event2_rogue_outcome": (
        "Você não demora. O fazendeiro acena uma vez — gratidão sem dívida.\n"
        "No escuro depois, você se move mais levemente. Mais rápido. +4 ATQ, +2 DEF."
    ),

    # Event 3 — escolhas específicas de classe
    "event3_warrior_text": "Proponha um teste de vontade. Poder pela resistência, não por pactos.",
    "event3_warrior_outcome": (
        "Ela aceita, sombriamente. Você supera algo que despedaçaria uma mente mais fraca.\n"
        "Quando termina, ela olha para você de forma diferente. 'Bem. Esse era o verdadeiro teste.'\n"
        "+7 ATQ, +3 DEF, +5 HP máx."
    ),
    "event3_mage_text": "Debata a teoria. Pode haver uma formulação melhor.",
    "event3_mage_outcome": (
        "Duas horas de debate arcano. Ela concede três de seus pontos.\n"
        "O que você leva não é o que ela ofereceu — é mais preciso.\n"
        "+9 Magia, +2 ATQ."
    ),
    "event3_rogue_text": "Ouça com atenção. Pegue alguns reagentes enquanto ela fala.",
    "event3_rogue_outcome": (
        "Ela sabe. Ela deixa acontecer — um teste que você não sabia que estava fazendo.\n"
        "'Pragmático,' ela diz, com algo próximo de aprovação.\n"
        "Os reagentes brilham intensamente depois. +20 ouro, +3 ATQ, +3 Magia."
    ),

    # Event 4 — escolhas específicas de classe
    "event4_warrior_text": "Arranque as páginas principais. Inteligência de batalha prática.",
    "event4_warrior_outcome": (
        "Você enrola as páginas com firmeza e as guarda na armadura.\n"
        "Padrões de ataque. Pontos fracos. Você não vai entender a teoria — não precisa.\n"
        "+9 ATQ, +4 DEF."
    ),
    "event4_mage_text": "Canalize a ressonância do tomo diretamente. Pule a leitura.",
    "event4_mage_outcome": (
        "Luz branca. Segundos passam. Quando você olha, sabe coisas que não sabia antes —\n"
        "não como palavras, mas como formas. As formas do poder. +13 Magia."
    ),
    "event4_rogue_text": "Copie as runas principais na sua lâmina à luz da tocha.",
    "event4_rogue_outcome": (
        "As runas se instalam no metal como se sempre estivessem lá.\n"
        "Você não sabe o que significam. Elas sabem. +7 ATQ, +4 Magia."
    ),

    # Event 5 — O Cavaleiro Corrompido
    "event5_title": "O Cavaleiro Corrompido",
    "event5_narrative": (
        "Um cavaleiro em armadura de obsidiana rachada está entre você e a escada.\n"
        "Sua espada está erguida — mas seus olhos estão vazios. Insígnia real no ombral:\n"
        "Casa Valdris. A família que mandou seu herdeiro matar o Dragão\n"
        "vinte anos atrás. Ele nunca voltou.\n"
        "\"...recue... recue...\" ele range. Ele não abaixa a espada."
    ),
    "event5_choice1_text": "Abra caminho pela força.",
    "event5_choice1_outcome": (
        "Vocês colidem duas vezes. Ele é mais forte do que parece — você leva um golpe antes de avançar.\n"
        "A espada dele cai. Ele não segue. +5 ATQ. -15 HP."
    ),
    "event5_choice2_text": "Fale com o que resta dele.",
    "event5_choice2_outcome": (
        "Você abaixa a arma e diz o nome dele — Casa Valdris. Algo vacila.\n"
        "A mão da espada treme. Ele desaba sobre um joelho.\n"
        "'Não... deixe terminar da mesma forma.' Você passa em silêncio. +15 HP máx, +3 DEF."
    ),
    "event5_choice3_text": "Termine logo. É uma misericórdia.",
    "event5_choice3_outcome": (
        "Um golpe. Limpo. Ele exala — não de dor, mas de alívio.\n"
        "No cinto: uma bolsa de moedas e uma faca ainda afiada. +30 ouro, +4 ATQ."
    ),
    "event5_warrior_text": "Reconheça a postura de um soldado. Desafie-o para um último duelo honroso.",
    "event5_warrior_outcome": (
        "Ele aceita — o último reflexo de um lutador treinado.\n"
        "Você o enfrenta golpe por golpe, honrando a luta mesmo ao encerrá-la.\n"
        "Algo se instala em vocês dois. +6 ATQ, +4 DEF, +10 HP máx."
    ),
    "event5_mage_text": "Tente um ritual de purificação. Qualquer maldição que o tomou, nomeie-a.",
    "event5_mage_outcome": (
        "A corrupção resiste — então racha. Ele arqueja. O olhar vazio desvanece.\n"
        "'Obrigado,' ele diz. É o suficiente. +8 Magia, +10 HP máx."
    ),
    "event5_rogue_text": "Deslize pelas sombras. Ele não pode lutar contra o que não pode ver.",
    "event5_rogue_outcome": (
        "Você está três passos à frente antes que ele se vire. Ele não segue.\n"
        "Fácil. Limpo. Vale a pena. +4 ATQ, +20 ouro, +10 HP."
    ),

    # Event 6 — A Lágrima do Dragão
    "event6_title": "A Lágrima do Dragão",
    "event6_narrative": (
        "No último degrau antes da porta final, uma única gota cristalina repousa sobre a pedra.\n"
        "Morna ao toque. Ela brilha suavemente — não com magia, mas com algo mais antigo.\n"
        "O Dragão a derramou aqui. Não de raiva. Não de dor.\n"
        "Cem anos de cativeiro podem quebrar qualquer coisa, dado tempo suficiente.\n"
        "Você a pega. O que fazer com ela é sua decisão."
    ),
    "event6_choice1_text": "Estilhace-a contra sua lâmina. Uma arma é uma arma.",
    "event6_choice1_outcome": (
        "A gota se fragmenta no metal com um sibilo de luz.\n"
        "Poder sem sentimento. Você vai aceitar. +6 ATQ, +6 Magia."
    ),
    "event6_choice2_text": "Guarde-a consigo. Algumas coisas deveriam permanecer inteiras.",
    "event6_choice2_outcome": (
        "Ela aquece sua palma durante todo o caminho até a porta.\n"
        "Você se sente mais estável do que em qualquer momento desde o primeiro andar.\n"
        "Seja o que for que espera dentro, você o enfrentará como você mesmo. +25 HP máx, +4 DEF."
    ),
    "event6_choice3_text": "Beba-a. Deixe a dor do Dragão se tornar sua força.",
    "event6_choice3_outcome": (
        "Queima ao descer — não como fogo, mas como memória.\n"
        "Algo vasto, antigo e triste. Você entende o Dragão agora.\n"
        "Ainda assim vai matá-lo. +8 ATQ, +8 Magia. HP máx -10."
    ),
    "event6_warrior_text": "Pressione-a na empunhadura da sua arma. Deixe-a te ancorar.",
    "event6_warrior_outcome": (
        "Ela se funde no metal com um som baixo que você sente mais do que ouve.\n"
        "Seu aperto está mais firme do que nunca. +10 ATQ, +5 DEF."
    ),
    "event6_mage_text": "Absorva-a lentamente em seu núcleo mágico. Um conduíte perfeito.",
    "event6_mage_outcome": (
        "A magia nela reconhece a sua e flui para encontrá-la.\n"
        "Você nunca sentiu seu poder tão claramente. +14 Magia, +5 HP máx."
    ),
    "event6_rogue_text": "Embolse-a. Uma lágrima do Dragão — isso vale alguma coisa.",
    "event6_rogue_outcome": (
        "Talvez para um estudioso. Talvez apenas como lembrança. De qualquer forma, é seu.\n"
        "+35 ouro, +5 ATQ, +3 Magia."
    ),

    # Retorno do prisioneiro (andar 3)
    "prisoner_returns": (
        "O homem que você salvou no primeiro andar emerge de uma passagem lateral.\n"
        "Ele está melhor. Não bem — mas melhor.\n"
        "'Encontrei um atalho,' ele diz. 'Mais lento, mas vivo.'\n"
        "Ele pressiona algo frio em sua mão — um frasco selado e uma bolsa de moedas.\n"
        "'Você merece.' Então ele se foi."
    ),
    "prisoner_gift": "+10 Ouro  +5 HP máx  +poção Lágrimas do Dragão",

    # Armas bloqueadas na loja
    "shop_weapons_locked": (
        "A expressão do mercador endurece enquanto você se aproxima da prateleira de armas.\n"
        "\"Notícias viajam em calabouços. Eu conhecia o povo daquela aldeia.\"\n"
        "Ele se coloca na frente das armas.\n"
        "\"Não para você. Pegue suas poções e vá embora.\""
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

    # ── Eventos Alternativos (adicionado por storyteller) ────────────────────────

    # Evento 1 Alternativo — O Negociante das Sombras
    "event1alt_title": "O Negociante das Sombras",
    "event1alt_narrative": (
        "Uma figura de preto está sentada sozinha numa passagem lateral, cercada por mercadorias estranhas.\n"
        "Frascos de líquido turvo. Armas que não deveriam existir. Livros que machucam de olhar.\n"
        "'Não se importa comigo,' o negociante diz sem olhar para cima. 'Sirvo aqueles\n"
        "que podem pagar o que realmente precisam.'\n"
        "Você sente poder antigo na mercadoria. Nada aqui é limpo."
    ),
    "event1alt_choice1_text": "Faça um negócio com o negociante.",
    "event1alt_choice1_outcome": (
        "O negociante sorri. 'Eu sabia que você viria.' Você troca ouro por algo\n"
        "que não compreende completamente. Senta-se em seu inventário como uma pedra.\n"
        "O negociante acena: 'Use apenas quando tiver certeza.'"
    ),
    "event1alt_choice2_text": "Recuse. Você não precisa de bens amaldiçoados.",
    "event1alt_choice2_outcome": (
        "O negociante ri sem calor. 'Sua perda. Poucos têm força para me recusar.'\n"
        "Ao partir, você se sente mais leve. Mais limpo. Às vezes, isso vale mais."
    ),
    "event1alt_choice3_text": "Pegue o que puder e corra.",
    "event1alt_choice3_outcome": (
        "Você agarra uma mão cheia de frascos e se move rápido. O negociante não o segue —\n"
        "nunca seguem. Esses negociantes existem fora das regras do calabouço.\n"
        "Na mochila, a mercadoria roubada pulsa com peso opaco."
    ),
    "event1alt_warrior_text": "Exija saber o que se esconde sob a mercadoria.",
    "event1alt_warrior_outcome": (
        "'Uma franqueza guerreira.' O negociante pousa uma lâmina curva.\n"
        "'Esta aqui tem fome. Alimente-a com sangue e ela o alimenta de volta. Comércio justo.'\n"
        "Você a toma. O poder sente-se honesto quando é tão claro."
    ),
    "event1alt_mage_text": "Sinta a magia em suas mercadorias.",
    "event1alt_mage_outcome": (
        "Você fecha os olhos. A magia aqui é antiga — nem boa nem má, apenas antiga.\n"
        "O negociante sussurra: 'Ah, alguém que entende. Pegue o frasco do fundo.\n"
        "Ele se lembra de coisas que você precisará saber.'"
    ),
    "event1alt_rogue_text": "Converse seu caminho para um negócio melhor do que deveria.",
    "event1alt_rogue_outcome": (
        "'Eu gosto de você,' diz o negociante. 'A maioria não fala. Apenas toma.'\n"
        "Você negocia algo melhor do que qualquer um de vocês pretendia.\n"
        "Ao partir, o negociante chama: 'Você vai bem.'"
    ),

    # Evento 2 Alternativo — As Ruínas da Casa Valdris
    "event2alt_title": "As Ruínas da Casa Valdris",
    "event2alt_narrative": (
        "Uma galeria nobre em ruínas, coberta de pó e tapeçarias escuras.\n"
        "Brasões da Casa Valdris forram as paredes — um nome de família que você ouviu sussurrar.\n"
        "Marcadores de pedra descrevem uma linhagem, tudo levando a um nome: 'Senhor Theron,\n"
        "enviado para abater o Dragão, Ano 246.'\n"
        "Ele nunca voltou. O que quer que tenha acontecido aqui, foi enterrado."
    ),
    "event2alt_choice1_text": "Estude as inscrições com cuidado.",
    "event2alt_choice1_outcome": (
        "Horas de leitura na luz fraca. As inscrições contam uma história:\n"
        "não de fracasso, mas de algo pior. Theron conseguiu. Ele acorrentou o Dragão.\n"
        "Mas o custo... 'Sua alma foi o pagamento,' lê-se em um último entalho.\n"
        "Conhecimento é poder. Às vezes, é também uma maldição."
    ),
    "event2alt_choice2_text": "Preste respeitos e saia rápido.",
    "event2alt_choice2_outcome": (
        "Você se ajoelha brevemente diante do brasão Valdris. Alguns espaços exigem silêncio.\n"
        "Você não entende o que aconteceu aqui, e talvez seja melhor assim.\n"
        "O calabouço respeita quem respeita seus mortos. Você sente esse respeito."
    ),
    "event2alt_choice3_text": "Arranque os estandartes e pegue o que tiver valor.",
    "event2alt_choice3_outcome": (
        "As tapeçarias desintegram ao seu toque — seda morta há um século.\n"
        "Escondido sob uma: um esconderijo de moedas. Profanação de túmulo nunca pareceu tão limpa.\n"
        "A Casa Valdris não se importará. Deixaram de existir há muito tempo."
    ),
    "event2alt_warrior_text": "Guarde o túmulo, honrando os caídos.",
    "event2alt_warrior_outcome": (
        "Você se posiciona diante do brasão Valdris e simplesmente fica de pé.\n"
        "O peso da história cai sobre seus ombros.\n"
        "Ao finalmente partir, sente-se como se tivesse sido armado cavaleiro."
    ),
    "event2alt_mage_text": "Decifre os avisos rúnicos entalados na pedra.",
    "event2alt_mage_outcome": (
        "As runas brilham fracamente sob seu toque. 'Perigo. Sacrifício. Prisão.'\n"
        "São avisos que chegaram muito tarde. Mas agora você entende:\n"
        "o Dragão não é simplesmente maligno. Está aprisionado. Está sofrendo."
    ),
    "event2alt_rogue_text": "Encontre o esconderijo secreto deixado pela casa para herdeiros desesperados.",
    "event2alt_rogue_outcome": (
        "Seus dedos encontram a pedra solta. Dentro: ouro para três andares,\n"
        "e uma carta dirigida a quem quer que seja valente o suficiente para continuar o trabalho Valdris.\n"
        "Algumas famílias levam suas responsabilidades a sério."
    ),

    # Evento 3 Alternativo — A Cavaleira Capturada
    "event3alt_title": "A Cavaleira Capturada",
    "event3alt_narrative": (
        "Um grito — humano, desesperado — ecoa de uma câmara lateral.\n"
        "Você encontra uma mulher em veste militar, acorrentada a um pilar.\n"
        "Ferimentos frescos. Marcas cultistas riscadas nas paredes ao seu redor.\n"
        "'Por favor,' ela ofega. 'Eles voltam logo. Se você vai fazer algo —\n"
        "se você vai fazer algo, tem de ser agora.'"
    ),
    "event3alt_choice1_text": "Liberte-a e dê-lhe uma arma.",
    "event3alt_choice1_outcome": (
        "As correntes caem. Ela tropeça, depois se estabiliza com uma clareza\n"
        "que lhe diz que foi treinada para isso. 'Vou pela passagem de trás.\n"
        "Você vai à frente. Mate-os.' Ela se foi antes que você pudesse responder."
    ),
    "event3alt_choice2_text": "Você não pode arriscar a distração. Deixe-a.",
    "event3alt_choice2_outcome": (
        "Você se afasta de seus apelos. Sua missão está à frente. Sua missão importa mais.\n"
        "Conforme você caminha, você não ouve o grito dela. Talvez tenham vindo rápido.\n"
        "Ou talvez ela ainda esteja lá, esperando por alguém mais corajoso."
    ),
    "event3alt_choice3_text": "Use-a como alavanca se os cultistas o encontrarem.",
    "event3alt_choice3_outcome": (
        "'Vou mantê-la viva,' você lhe diz, 'mas você é um seguro.'\n"
        "Ela acena grimacemente. Ela é uma soldada. Ela entende sacrifício.\n"
        "Se você realmente a usará é uma decisão que ainda não tomou."
    ),
    "event3alt_warrior_text": "Ofereça-lhe um lugar lutando ao seu lado.",
    "event3alt_warrior_outcome": (
        "Ela quebra as correntes sozinha — anos de treinamento traduzidos em pura fúria.\n"
        "'Estou com você,' diz ela. Juntos, vocês se sentem mais fortes.\n"
        "Pelo resto do calabouço, você não está sozinho."
    ),
    "event3alt_mage_text": "Quebra o selo mágico que a prende.",
    "event3alt_mage_outcome": (
        "O trabalho de runa é sofisticado — ela é mantida por mais que ferro.\n"
        "Você o desenrola cuidadosamente. Conforme o último sigilo se quebra, ela ofega:\n"
        "'Você é habilidoso. O Dragão vai lamentar isso.'"
    ),
    "event3alt_rogue_text": "Abra as fechaduras e a passe pelos guardas.",
    "event3alt_rogue_outcome": (
        "Suas mãos trabalham. As correntes caem em silêncio. Ela se move como um fantasma\n"
        "— você a ensinou o caminho através do escuro. Duas ladras, um momento.\n"
        "Ela alcança a saída sem um som."
    ),

    # Evento 4 Alternativo — A Demanda do Santuário
    "event4alt_title": "A Demanda do Santuário",
    "event4alt_narrative": (
        "Um santuário esculpido direto na parede do calabouço. Símbolos de prisão e proteção.\n"
        "Em seu centro: uma bacia de pedra, vazia. Mas algo espera naquele vazio.\n"
        "Uma presença. Antiga e ciente. Não fala com palavras.\n"
        "Pergunta: 'O que você oferecerá para prosseguir?'"
    ),
    "event4alt_choice1_text": "Faça uma oferta genuína.",
    "event4alt_choice1_outcome": (
        "Você deixa algo precioso na bacia. Ouro. Uma memória. Um pequeno pedaço de si mesmo.\n"
        "O santuário aceita. A presença recua — não se foi, mas satisfeita.\n"
        "A escada à frente brilha fracamente. Você ganhou passagem."
    ),
    "event4alt_choice2_text": "Recuse e prossiga à força.",
    "event4alt_choice2_outcome": (
        "Você ignora a demanda do santuário. A presença não gosta disso.\n"
        "O caminho à frente é mais duro — marcado com obstáculos e testes —\n"
        "mas você consegue passar. Alguns deuses respeitam desafio."
    ),
    "event4alt_choice3_text": "Destrua o santuário.",
    "event4alt_choice3_outcome": (
        "Sua arma despedaça a pedra. A presença grita silenciosamente\n"
        "— um som que existe apenas em sua mente. Desaparece, banida ou libertada.\n"
        "O calabouço sente-se menor agora. Menos observado. Isso é melhor ou pior?"
    ),
    "event4alt_warrior_text": "Reclame o santuário como seu.",
    "event4alt_warrior_outcome": (
        "Você fica na bacia e declara: 'Ofereço sangue e vontade.'\n"
        "A presença reconhece um juramento guerreiro. Se liga com você, não contra você.\n"
        "Sente-a nos ossos: poder alinhado com propósito."
    ),
    "event4alt_mage_text": "Absorva a magia antiga do santuário.",
    "event4alt_mage_outcome": (
        "Você coloca ambas as mãos na pedra. A magia flui através de você\n"
        "— antiga, estruturada, e incrivelmente refinada. Cai em seu núcleo.\n"
        "Agora você entende por que magos vêm a lugares assim."
    ),
    "event4alt_rogue_text": "Roube da câmara de tesouro escondida do santuário.",
    "event4alt_rogue_outcome": (
        "Seus dedos encontram o mecanismo escondido. A bacia não é um santuário —\n"
        "é uma fechadura. Atrás dela: riqueza além da medida, esquecida por todos.\n"
        "Você não leva tudo. Apenas o bastante para importar."
    ),

    # Evento 5 Alternativo — O Aventureiro Rival
    "event5alt_title": "O Aventureiro Rival",
    "event5alt_narrative": (
        "Outro aventureiro bloqueia o corredor à frente. Cicatrizado. Faminto. Perigoso.\n"
        "'O Dragão,' eles dizem, 'morre apenas uma vez. E eu estava aqui primeiro.'\n"
        "Não é um cultista ou um guardião. É alguém como você.\n"
        "Alguém que quer o que você quer. Só pode haver um herói."
    ),
    "event5alt_choice1_text": "Lute pela glória.",
    "event5alt_choice1_outcome": (
        "Aço contra aço. Eles são bons — melhores do que você esperava.\n"
        "Mas você é mais rápido, mais esperto, ou apenas mais desesperado. Quando caem,\n"
        "eles acenam uma vez com respeito. Alguns competidores entendem derrota."
    ),
    "event5alt_choice2_text": "Proponha uma aliança.",
    "event5alt_choice2_outcome": (
        "'Dois heróis são mais fortes que um,' você oferece. Eles consideram.\n"
        "'Justo. Mas apenas até chegarmos ao Dragão. Depois, somos inimigos.'\n"
        "Vocês selam. Tréguas frágeis são melhores que mortes inúteis."
    ),
    "event5alt_choice3_text": "Deixe-os passar. Você toma outro caminho.",
    "event5alt_choice3_outcome": (
        "Você se afasta. 'Pegue o caminho direto. Vou encontrar outra forma.'\n"
        "Eles parecem surpresos, depois respeitosos. 'Esse é o movimento de alguém\n"
        "que sabe que vai vencer.' Talvez você concorde."
    ),
    "event5alt_warrior_text": "Desafie-os para combate singular.",
    "event5alt_warrior_outcome": (
        "Eles aceitam imediatamente. Guerreiro a guerreiro. O combate é feroz e limpo.\n"
        "Quando você vence, ambos entendem algo sobre honra.\n"
        "'Vá,' eles dizem. 'Faça isso contar.'"
    ),
    "event5alt_mage_text": "Duele com magia em vez de aço.",
    "event5alt_mage_outcome": (
        "Feitiços colidem. Nenhum de vocês enfrentou magia tão sofisticada.\n"
        "Quando você emerge vitoriosa, eles estão de joelhos, mas vivos.\n"
        "'Você entende poder real,' admitem. 'O Dragão não entenderá.'"
    ),
    "event5alt_rogue_text": "Ultrapasse-os com engenhosidade.",
    "event5alt_rogue_outcome": (
        "Você finta, desvia, e passa antes que percebam que se moveu.\n"
        "Quando finalmente se viram, você já está à frente. Vindo de trás, você ouve\n"
        "gargalhada: 'Engenhoso. Eu gosto de você. Boa sorte.'"
    ),

    # Evento 6 Alternativo — A Visão Espectral
    "event6alt_title": "A Visão Espectral",
    "event6alt_narrative": (
        "Uma figura aparece diante de você — translúcida, antiga, irradiando tristeza.\n"
        "Um fantasma. Um real, não ilusão ou truque.\n"
        "'Eu era o Dragão uma vez,' diz. 'Não seu nome. Seu guardião. Antes da prisão.\n"
        "Ele quer morrer. Cada momento é agonia. Quando o enfrentar,\n"
        "lembre-se: você não está matando um monstro. Você está respondendo a um pedido de misericórdia.'"
    ),
    "event6alt_choice1_text": "Ouça o aviso. Mostre misericórdia ao Dragão.",
    "event6alt_choice1_outcome": (
        "Você carregará esse conhecimento para o combate final. Misericórdia em vitória.\n"
        "O caminho à frente parece mais claro — você sabe o que precisa fazer.\n"
        "O fantasma desaparece, e de algum modo, isso parece perdão."
    ),
    "event6alt_choice2_text": "Ignore o aviso. Foque apenas na vitória.",
    "event6alt_choice2_outcome": (
        "O fantasma parece triste. 'A maioria faz,' sussurra, então desaparece.\n"
        "Você segue adiante, desincumbido de misericórdia ou tristeza.\n"
        "Se isso é força ou fraqueza, você descobrirá em breve."
    ),
    "event6alt_choice3_text": "Pergunte ao fantasma mais sobre a natureza do Dragão.",
    "event6alt_choice3_outcome": (
        "'Ele era bonito uma vez,' diz o fantasma. 'Sábio. A prisão quebrou isso.\n"
        "Agora é fúria enrolada em uma mente brilhante. Nenhum de vocês escolheu isso.'\n"
        "Você finalmente entende. O Dragão é uma tragédia, não um inimigo."
    ),
    "event6alt_warrior_text": "Exija que o Dragão o enfrente com honra.",
    "event6alt_warrior_outcome": (
        "O fantasma sorri. 'Um desejo guerreiro. Vou levar isso até ele.'\n"
        "No combate final, o Dragão o encontra com respeito, não crueldade.\n"
        "Seu choque se torna um duelo digno de legenda."
    ),
    "event6alt_mage_text": "Comunique-se com o espírito, aprendendo sua magia.",
    "event6alt_mage_outcome": (
        "O fantasma lhe ensina em momentos o que levaria anos para aprender.\n"
        "Magia antiga. Do tipo que molda calabouços e aprisiona dragões.\n"
        "Você sobe as escadas mais poderosa do que era."
    ),
    "event6alt_rogue_text": "Aceite um segredo que o fantasma guardou por um século.",
    "event6alt_rogue_outcome": (
        "'O Dragão tem uma fraqueza,' sussurra o fantasma. 'Não em força, mas em vontade.\n"
        "Ele quer se render ao oponente certo. Seja digna.'\n"
        "Você carrega aquele segredo como uma chave."
    ),

    # Shadow Broker Ending (Rogue-dominante)
    "ending_shadow_broker_title": "A Corretora das Sombras",
    "ending_shadow_broker_desc": (
        "O Dragão cai, e você escorrega para o espaço onde ele respirava.\n"
        "Poder, segredos, conhecimento antigo — tudo se torna inventário.\n\n"
        "Você não governa o calabouço. Governantes são demasiado visíveis, muito vulneráveis.\n"
        "Em vez disso, você se torna o preço que outros pagam por passagem.\n"
        "Informação, favores, pequenas corrupções que se acumulam em controle.\n\n"
        "Nas sombras onde os reinos fingem não olhar,\n"
        "sua palavra se torna lei."
    ),
    "ending_shadow_broker_bonus": "Atalhos escuros se abrem diante de você — o sigilo reina supremo!",
}
