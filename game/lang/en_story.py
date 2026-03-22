STRINGS: dict = {
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

    # Event 5 — The Corrupted Knight (floor 5)
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

    # Event 6 — The Dragon's Tear (floor 6)
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

    # ── Alternate Events (added by storyteller) ────────────────────────────────

    # Event 1 Alternate — The Dark Merchant
    "event1alt_title": "The Dark Merchant",
    "event1alt_narrative": (
        "A figure in black sits alone in a side passage, surrounded by strange wares.\n"
        "Vials of murky liquid. Weapons that shouldn't exist. Books that hurt to look at.\n"
        "'Don't mind me,' the merchant says without looking up. 'I serve those\n"
        "who can afford what they truly need.'\n"
        "You can smell old power on the merchandise. None of it is clean."
    ),
    "event1alt_choice1_text": "Bargain with the merchant.",
    "event1alt_choice1_outcome": (
        "The merchant smiles. 'I thought you might.' You trade gold for something\n"
        "you don't fully understand. It settles into your inventory like a stone.\n"
        "The merchant nods: 'Use it only when you're certain.'"
    ),
    "event1alt_choice2_text": "Refuse. You don't need cursed goods.",
    "event1alt_choice2_outcome": (
        "The merchant laughs without warmth. 'Your loss. Most don't have the strength\n"
        "to refuse me.' As you leave, you feel lighter. Cleaner. Sometimes that's worth more."
    ),
    "event1alt_choice3_text": "Take what you can and run.",
    "event1alt_choice3_outcome": (
        "You grab a handful of vials and move fast. The merchant doesn't follow —\n"
        "they never do. These merchants exist outside the dungeon's rules.\n"
        "Inside your pack, the stolen goods pulse with dull weight."
    ),
    "event1alt_warrior_text": "Demand to know what lies beneath the goods.",
    "event1alt_warrior_outcome": (
        "'A warrior's directness.' The merchant sets down a curved blade.\n"
        "'This one hungers. Feed it blood and it feeds you back. Fair trade.'\n"
        "You take it. Power feels honest when it's this clear."
    ),
    "event1alt_mage_text": "Sense the magic in their wares.",
    "event1alt_mage_outcome": (
        "You close your eyes. The magic here is old — not good or evil, just ancient.\n"
        "The merchant whispers: 'Ah, one who understands. Take the vial at the back.\n"
        "It remembers things you'll need to know.'"
    ),
    "event1alt_rogue_text": "Talk your way into a deal you shouldn't get.",
    "event1alt_rogue_outcome": (
        "'I like you,' the merchant says. 'Most people don't talk. They just take.'\n"
        "You negotiate something better than either of you intended.\n"
        "As you leave, the merchant calls: 'You'll do.'"
    ),

    # Event 2 Alternate — The Ruins of House Valdris
    "event2alt_title": "The Ruins of House Valdris",
    "event2alt_narrative": (
        "A crumbling noble's gallery, choked with dust and dark tapestries.\n"
        "Crests of House Valdris line the walls — a family name you've heard whispered.\n"
        "Stone markers describe a lineage, all leading to one name: 'Lord Theron,\n"
        "sent forth to slay the Dragon, Year 246.'\n"
        "He never came back. Whatever happened in these ruins, it was buried."
    ),
    "event2alt_choice1_text": "Study the inscriptions carefully.",
    "event2alt_choice1_outcome": (
        "Hours of reading in the dim light. The inscriptions tell a story:\n"
        "not of failure, but of something worse. Theron succeeded. He bound the Dragon.\n"
        "But the cost... 'His soul was the payment,' one final carving reads.\n"
        "Knowledge is power. Also, sometimes it's a curse."
    ),
    "event2alt_choice2_text": "Pay respects and leave quickly.",
    "event2alt_choice2_outcome": (
        "You kneel briefly before the Valdris crest. Some spaces demand silence.\n"
        "You don't understand what happened here, and maybe that's for the best.\n"
        "The dungeon respects those who respect its dead. You feel that respect."
    ),
    "event2alt_choice3_text": "Tear down the banners and take what's valuable.",
    "event2alt_choice3_outcome": (
        "The tapestries crumble at your touch — silk that's been dead for a century.\n"
        "Hidden beneath one: a cache of coins. Grave robbery has never felt quite so clean.\n"
        "The House of Valdris won't mind. They stopped existing long ago."
    ),
    "event2alt_warrior_text": "Stand guard over the tomb, honoring the fallen.",
    "event2alt_warrior_outcome": (
        "You take a position before the Valdris crest and simply stand.\n"
        "The weight of history settles on your shoulders.\n"
        "When you finally turn to leave, you feel like you've been knighted."
    ),
    "event2alt_mage_text": "Decipher the runic warnings carved into the stone.",
    "event2alt_mage_outcome": (
        "The runes glow faintly under your touch. 'Danger. Sacrifice. Binding.'\n"
        "They're warnings that came too late. But you understand now:\n"
        "the Dragon isn't simply evil. It's trapped. It's suffering."
    ),
    "event2alt_rogue_text": "Find the hidden cache the house left for desperate heirs.",
    "event2alt_rogue_outcome": (
        "Your fingers find the loose stone. Inside: enough gold for three floors,\n"
        "and a letter addressed to anyone brave enough to continue the Valdris work.\n"
        "Some families take their responsibilities seriously."
    ),

    # Event 3 Alternate — The Captured Knight
    "event3alt_title": "The Captured Knight",
    "event3alt_narrative": (
        "A scream — human, desperate — echoes from a side chamber.\n"
        "You find a woman in military dress, chained to a pillar.\n"
        "Fresh wounds. Cultist markings chalked on the walls around her.\n"
        "'Please,' she gasps. 'They're coming back soon. If you're going to—\n"
        "if you're going to do something, it has to be now.'"
    ),
    "event3alt_choice1_text": "Free her and give her a weapon.",
    "event3alt_choice1_outcome": (
        "The chains snap. She stumbles, then steadies herself with a clarity\n"
        "that tells you she was trained for this. 'I'll take a back passage out.\n"
        "You go forward. Kill them.' She's gone before you can respond."
    ),
    "event3alt_choice2_text": "You can't risk the distraction. Leave her.",
    "event3alt_choice2_outcome": (
        "You turn away from her pleas. Your mission is ahead. Your mission matters more.\n"
        "As you walk, you don't hear her scream. Maybe they came quickly.\n"
        "Or maybe she's still there, hoping someone braver will return."
    ),
    "event3alt_choice3_text": "Use her as leverage if the cultists find you.",
    "event3alt_choice3_outcome": (
        "'I'll keep you alive,' you tell her, 'but you're insurance.'\n"
        "She nods grimly. She's a soldier. She understands sacrifice.\n"
        "Whether you actually use her is a decision you haven't made yet."
    ),
    "event3alt_warrior_text": "Offer her a place fighting at your side.",
    "event3alt_warrior_outcome": (
        "She breaks the chains herself — years of training translated to pure fury.\n"
        "'I'm with you,' she says. Together you feel stronger.\n"
        "For the rest of the dungeon, you're not alone."
    ),
    "event3alt_mage_text": "Break the magical seal binding her.",
    "event3alt_mage_outcome": (
        "The rune-work is sophisticated — she's been held by more than iron.\n"
        "You unravel it carefully. As the last sigil breaks, she gasps:\n"
        "'You're skilled. The Dragon is going to regret this.'"
    ),
    "event3alt_rogue_text": "Pick the locks and slip her past the guards.",
    "event3alt_rogue_outcome": (
        "Your hands work. The chains fall silent. She moves like a ghost\n"
        "— you taught her the way through the dark. Two thieves, one moment.\n"
        "She reaches the exit without a sound."
    ),

    # Event 4 Alternate — The Shrine's Demand
    "event4alt_title": "The Shrine's Demand",
    "event4alt_narrative": (
        "A shrine carved directly into the dungeon wall. Symbols of binding and protection.\n"
        "At its center: a stone basin, empty. But something waits in that emptiness.\n"
        "A presence. Ancient and aware. It doesn't speak with words.\n"
        "It asks: 'What will you offer to proceed?'"
    ),
    "event4alt_choice1_text": "Make a genuine offering.",
    "event4alt_choice1_outcome": (
        "You leave something precious in the basin. Gold. A memory. A small piece of yourself.\n"
        "The shrine accepts. The presence recedes — not gone, but satisfied.\n"
        "The staircase ahead glows faintly. You've earned passage."
    ),
    "event4alt_choice2_text": "Refuse and press forward.",
    "event4alt_choice2_outcome": (
        "You ignore the shrine's demand. The presence doesn't like this.\n"
        "The path ahead is harder — marked with obstacles and tests —\n"
        "but you make it through. Some gods respect defiance."
    ),
    "event4alt_choice3_text": "Destroy the shrine.",
    "event4alt_choice3_outcome": (
        "Your weapon shatters the stone. The presence screams silently\n"
        "— a sound that exists only in your mind. It fades, banished or freed.\n"
        "The dungeon feels smaller now. Less watched. Is that better or worse?"
    ),
    "event4alt_warrior_text": "Claim the shrine as your own.",
    "event4alt_warrior_outcome": (
        "You stand in the basin and declare: 'I offer blood and will.'\n"
        "The presence recognizes a warrior's oath. It binds with you, not against you.\n"
        "You feel it in your bones: power aligned with purpose."
    ),
    "event4alt_mage_text": "Absorb the shrine's ancient magic.",
    "event4alt_mage_outcome": (
        "You place both hands on the stone. The magic pours through you\n"
        "— old, structured, and incredibly refined. It settles into your core.\n"
        "You understand now why mages come to places like this."
    ),
    "event4alt_rogue_text": "Steal from the shrine's hidden treasure chamber.",
    "event4alt_rogue_outcome": (
        "Your fingers find the hidden mechanism. The basin isn't a shrine —\n"
        "it's a lock. Behind it: wealth beyond measure, forgotten by everyone.\n"
        "You don't take it all. Just enough to matter."
    ),

    # Event 5 Alternate — The Rival Adventurer
    "event5alt_title": "The Rival Adventurer",
    "event5alt_narrative": (
        "Another adventurer blocks the corridor ahead. Scarred. Hungry. Dangerous.\n"
        "'The Dragon,' they say, 'only dies once. And I was here first.'\n"
        "This isn't a cultist or a guardian. This is someone like you.\n"
        "Someone who wants what you want. There can only be one hero."
    ),
    "event5alt_choice1_text": "Fight for the glory.",
    "event5alt_choice1_outcome": (
        "Steel meets steel. They're good — better than you expected.\n"
        "But you're faster, smarter, or just more desperate. When they fall,\n"
        "they nod once in respect. Some competitors understand defeat."
    ),
    "event5alt_choice2_text": "Propose an alliance.",
    "event5alt_choice2_outcome": (
        "'Two heroes are stronger than one,' you offer. They consider it.\n"
        "'Fair. But only until we reach the Dragon. After that, we're enemies.'\n"
        "You shake on it. Fragile truces are better than pointless deaths."
    ),
    "event5alt_choice3_text": "Let them pass. You take a different route.",
    "event5alt_choice3_outcome": (
        "You step aside. 'Take the direct path. I'll find another way.'\n"
        "They look surprised, then respectful. 'That's the move of someone\n"
        "who knows they're going to win.' Maybe you agree."
    ),
    "event5alt_warrior_text": "Challenge them to single combat.",
    "event5alt_warrior_outcome": (
        "They accept immediately. Warrior to warrior. The fight is fierce and clean.\n"
        "When you win, you both understand something about honor.\n"
        "'Go,' they say. 'Make it count.'"
    ),
    "event5alt_mage_text": "Duel with magic instead of steel.",
    "event5alt_mage_outcome": (
        "Spells clash. Neither of you has faced magic this sophisticated.\n"
        "When you emerge victorious, they're on their knees, but alive.\n"
        "'You understand real power,' they admit. 'The Dragon won't.'"
    ),
    "event5alt_rogue_text": "Outmaneuver them with cunning.",
    "event5alt_rogue_outcome": (
        "You feint, dodge, and slip past before they realize you've moved.\n"
        "By the time they turn, you're already ahead. From behind, you hear\n"
        "laughter: 'Clever. I like you. Good luck.'"
    ),

    # Event 6 Alternate — The Ghostly Vision
    "event6alt_title": "The Ghostly Vision",
    "event6alt_narrative": (
        "A figure appears before you — translucent, ancient, radiating sorrow.\n"
        "A ghost. A real one, not illusion or trick.\n"
        "'I was the Dragon once,' it says. 'Not its name. Its keeper. Before the binding.\n"
        "It wants to die. Every moment is agony. When you face it,\n"
        "remember: you're not slaying a monster. You're answering a plea for mercy.'"
    ),
    "event6alt_choice1_text": "Heed the warning. Show the Dragon mercy.",
    "event6alt_choice1_outcome": (
        "You'll carry this knowledge to the final fight. Mercy in victory.\n"
        "The path ahead feels clearer — you know what you have to do.\n"
        "The ghost fades, and somehow, that feels like forgiveness."
    ),
    "event6alt_choice2_text": "Ignore the warning. Focus only on victory.",
    "event6alt_choice2_outcome": (
        "The ghost looks sad. 'Most do,' it whispers, then vanishes.\n"
        "You push forward, unburdened by mercy or sorrow.\n"
        "Whether that's strength or weakness, you'll find out soon enough."
    ),
    "event6alt_choice3_text": "Ask the ghost more about the Dragon's nature.",
    "event6alt_choice3_outcome": (
        "'It was beautiful once,' the ghost says. 'Wise. The binding broke that.\n"
        "Now it's rage wrapped around a brilliant mind. Neither of you chose this.'\n"
        "You understand, finally. The Dragon is a tragedy, not an enemy."
    ),
    "event6alt_warrior_text": "Demand that the Dragon face you with honor.",
    "event6alt_warrior_outcome": (
        "The ghost smiles. 'A warrior's wish. I'll carry that to it.'\n"
        "In the final fight, the Dragon matches you with respect, not cruelty.\n"
        "Your clash becomes a duel worthy of legend."
    ),
    "event6alt_mage_text": "Commune with the spirit, learning its magic.",
    "event6alt_mage_outcome": (
        "The ghost teaches you in moments what would take years to learn.\n"
        "Ancient magic. The kind that shaped dungeons and bound dragons.\n"
        "You ascend the stairs more powerful than you were."
    ),
    "event6alt_rogue_text": "Accept a secret the ghost has kept for a century.",
    "event6alt_rogue_outcome": (
        "'The Dragon has a weakness,' the ghost whispers. 'Not in strength, but in will.\n"
        "It wants to surrender to the right opponent. Be worthy.'\n"
        "You carry that secret like a key."
    ),

    # Shadow Broker Ending (Rogue-dominant)
    "ending_shadow_broker_title": "The Shadow Broker",
    "ending_shadow_broker_desc": (
        "The Dragon falls, and you slip into the space where it breathed.\n"
        "Power, secrets, ancient knowledge — all of it becomes inventory.\n\n"
        "You don't rule the dungeon. Rulers are too visible, too vulnerable.\n"
        "Instead, you become the price others pay for passage.\n"
        "Information, favors, small corruptions that add up to control.\n\n"
        "In the shadows where kingdoms pretend not to look,\n"
        "your word becomes law."
    ),
    "ending_shadow_broker_bonus": "Dark shortcuts open before you — stealth reigns supreme!",
}
