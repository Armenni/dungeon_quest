# GAMEDATA — Dungeon Quest Quick Reference

All values extracted directly from source. Update this file when source changes.

---

## 1. Player Classes

**Source:** `game/player.py` — `CLASS_STATS`

| Class   | HP  | MP | ATK | DEF | SPD | MAG | Gold | Inventory         |
|---------|-----|----|-----|-----|-----|-----|------|-------------------|
| Warrior | 120 | 20 | 15  | 12  | 8   | 5   | 10g  | 2× Health Potion  |
| Mage    | 70  | 80 | 8   | 6   | 9   | 20  | 10g  | 2× Health Potion  |
| Rogue   | 90  | 30 | 12  | 8   | 15  | 8   | 10g  | 2× Health Potion  |

**Level-up gains (per level):** +3 ATK, +2 DEF, +2 MAG, +15 max HP, +10 max MP, full heal on level-up.
**XP formula:** starts at 50, multiplied by ×1.5 each level. Excess XP carries over.

---

## 2. Player Spells / Abilities

**Source:** `game/combat.py` — `SPELLS`

**Damage formula:** `int(player.magic × magic_mult × dmg_mult) + random(−3, +5) − enemy.defense` (min 1)
**Physical attack:** `atk + random(−2, +4)`, crit ×1.5 (Rogue 20%, others 10%)

### Warrior
| Spell      | MP Cost | Dmg Mult | Side Effect              | Notes                         |
|------------|---------|----------|--------------------------|-------------------------------|
| Battlecry  | 10      | 0        | Weakened 3 turns, mag 4  | Pure debuff, no damage        |

### Mage
| Spell       | MP Cost | Dmg Mult | Side Effect                    |
|-------------|---------|----------|--------------------------------|
| Fireball    | 15      | ×2.0     | Burn 3 turns, mag 5            |
| Ice Shard   | 10      | ×2.0     | 50% chance Stun 1 turn         |
| Frost Armor | 20      | 0        | Shielded 2 turns (self-target) |

### Rogue
| Spell     | MP Cost | Dmg Mult | Side Effect            |
|-----------|---------|----------|------------------------|
| Backstab  | 12      | ×2.2     | Bleed 3 turns, mag 5   |

---

## 3. Status Effects

**Source:** `game/status.py`

| Effect   | Type    | Mechanics                                                        | How Applied          |
|----------|---------|------------------------------------------------------------------|----------------------|
| Burn     | DoT     | `magnitude` damage/turn (ticks at turn start), lasts `duration` | Fireball, enemy fireball/fire_breath |
| Poison   | DoT     | `magnitude` damage/turn (ticks at turn start), lasts `duration` | poison_sting, toxic_breath |
| Bleed    | DoT     | `magnitude` raw damage/turn, ignores defense (direct HP deduction) | Backstab |
| Stun     | CC      | Lose turn entirely; `consume_stun()` checks and removes it      | Ice Shard (50%), stun_bash, wing_stun, web_trap, rock_slam (50%) |
| Weakened | Debuff  | Reduces attacker's ATK by `magnitude` for `duration` turns      | Backstab, curse, shadow_bolt |
| Shielded | Buff    | Halves next incoming hit, then removes itself (one-time)        | Frost Armor          |

**apply_status():** if effect already exists, takes max(existing duration, new duration) and max(existing magnitude, new magnitude).

---

## 4. Enemy Roster

**Source:** `game/enemy.py`

**Scaling formula:** `s = 1 + (floor − 1) × 0.3` applied to HP, ATK, DEF, XP, Gold (Dragon capped at s=2.0).

| Enemy       | Base HP | Base ATK | Base DEF | SPD | Base XP | Base Gold | Abilities                                          |
|-------------|---------|----------|----------|-----|---------|-----------|----------------------------------------------------|
| Goblin      | 30      | 8        | 3        | 10  | 15      | 5         | attack, poison_sting                               |
| Skeleton    | 40      | 10       | 4        | 12  | 20      | 6         | attack, bone_throw                                 |
| Cave Spider | 28      | 9        | 2        | 13  | 18      | 5         | attack, poison_sting, web_trap                     |
| Orc         | 60      | 12       | 6        | 6   | 25      | 8         | attack, heavy_strike, curse                        |
| Dark Mage   | 35      | 15       | 2        | 11  | 30      | 10        | attack, fireball, curse                            |
| Wraith      | 45      | 13       | 4        | 10  | 28      | 9         | attack, drain_mana, life_steal                     |
| Stone Golem | 90      | 13       | 12       | 4   | 40      | 14        | attack, rock_slam, regenerate                      |
| Troll       | 80      | 14       | 8        | 5   | 35      | 12        | attack, regenerate, stun_bash                      |
| Cultist     | 50      | 11       | 5        | 11  | 32      | 11        | attack, dark_ritual, shadow_bolt                   |
| Dragon      | 220     | 24       | 18       | 8   | 200     | 50        | attack, fire_breath, tail_swipe, toxic_breath, wing_stun, regenerate |

**Floor enemy pools:**

| Floor | Available Enemies                                    |
|-------|------------------------------------------------------|
| 1     | Goblin, Skeleton, Cave Spider                        |
| 2     | Goblin, Orc, Skeleton, Cave Spider                   |
| 3     | Orc, Skeleton, Dark Mage, Wraith, Stone Golem        |
| 4     | Orc, Dark Mage, Troll, Wraith, Stone Golem           |
| 5     | Dark Mage, Troll, Wraith, Cultist                    |
| 6     | Troll, Dark Mage, Cultist                            |
| 7     | Dragon (boss only)                                   |

---

## 5. Enemy Abilities

**Source:** `game/combat.py` — `_ABILITY_HANDLERS`

| Ability       | Damage Formula                              | Side Effect                       |
|---------------|---------------------------------------------|-----------------------------------|
| attack        | `atk + random(−2, +3)` (respects weakened)  | —                                 |
| heavy_strike  | `atk × 1.5 + random(0, 5)`                 | —                                 |
| bone_throw    | `atk + random(2, 6)`                        | —                                 |
| fireball      | `atk × 1.8`                                | Burn 3 turns, mag 5               |
| fire_breath   | `atk × 1.6 + random(5, 15)`               | Burn 3 turns, mag 8               |
| tail_swipe    | `atk × 1.3`                                | —                                 |
| regenerate    | 0 (heal)                                   | Heals enemy 10–20 HP              |
| poison_sting  | `atk + random(0, 3)`                        | 50% chance Poison 3 turns, mag 4  |
| curse         | 0                                           | Weakened 2 turns, mag 4           |
| stun_bash     | `atk × 0.8`                                | Stun 1 turn                       |
| toxic_breath  | `atk × 1.5`                                | Poison 4 turns, mag 6             |
| wing_stun     | 0                                           | Stun 1 turn (suppressed turn 0)   |
| drain_mana    | 0                                           | Steal 8–15 MP; heal enemy by half |
| life_steal    | `atk × 1.4 + random(0, 4)`                | Heal enemy by 50% damage dealt    |
| dark_ritual   | 0 (heal + buff)                             | Heal 15% max HP; ATK ×1.2        |
| shadow_bolt   | `atk × 1.3 + random(2, 6)`                | Weakened 2 turns, mag 3           |
| web_trap      | 0                                           | Stun 1 turn                       |
| rock_slam     | `atk × 1.6 + random(0, 4)`                | 50% chance Stun 1 turn            |

**Dragon notes:** `wing_stun` suppressed on turn 0 and cannot repeat back-to-back.

---

## 6. Items

**Source:** `game/items.py` — `ITEMS`

| Key                   | Name                  | Effect              | Price |
|-----------------------|-----------------------|---------------------|-------|
| health_potion         | Health Potion         | Restore 30 HP       | 15g   |
| greater_health_potion | Greater Health Potion | Restore 60 HP       | 25g   |
| mana_potion           | Mana Potion           | Restore 20 MP       | 12g   |
| elixir                | Elixir                | Restore 80 HP+30 MP | 35g   |
| elixir_dragon         | Dragon Tears          | Restore 80 HP+30 MP | story drop only |
| antidote              | Antidote              | Cure poison & burn  | 20g   |

---

## 7. Equipment

**Source:** `game/equipment.py` — `EQUIPMENT`

### Weapons

| Key          | Name          | ATK | MAG | DEF | HP  | Price | Notes         |
|--------------|---------------|-----|-----|-----|-----|-------|---------------|
| iron_sword   | Iron Sword    | +4  | —   | —   | —   | 40g   |               |
| silver_dagger| Silver Dagger | +5  | —   | —   | —   | 45g   |               |
| wizard_staff | Wizard Staff  | —   | +6  | —   | —   | 45g   |               |
| steel_sword  | Steel Sword   | +8  | —   | —   | —   | 90g   |               |
| arcane_tome  | Arcane Tome   | —   | +12 | —   | —   | 100g  |               |
| shadow_blade | Shadow Blade  | +7  | +2  | —   | —   | —     | Story drop    |
| runic_blade  | Runic Blade   | +10 | +5  | —   | —   | 180g  |               |
| dragon_fang  | Dragon Fang   | +16 | +6  | —   | —   | —     | Story drop    |

### Armor

| Key          | Name         | ATK | MAG | DEF | HP  | Price | Notes      |
|--------------|--------------|-----|-----|-----|-----|-------|------------|
| padded_vest  | Padded Vest  | —   | —   | +3  | —   | 25g   |            |
| leather_armor| Leather Armor| —   | —   | +6  | —   | 45g   |            |
| chain_mail   | Chain Mail   | —   | —   | +10 | +10 | 80g   |            |
| mage_robes   | Mage Robes   | —   | +4  | +4  | —   | 50g   |            |
| dragon_scale | Dragon Scale | —   | —   | +14 | +20 | —     | Story drop |

### Shop Stock by Floor

| Floor | Weapons Available                         | Armor Available                    |
|-------|-------------------------------------------|------------------------------------|
| 1     | Iron Sword, Silver Dagger                 | Padded Vest                        |
| 2     | Iron Sword, Silver Dagger, Wizard Staff   | Padded Vest, Leather Armor         |
| 3     | Steel Sword, Wizard Staff, Arcane Tome    | Leather Armor, Chain Mail, Mage Robes |
| 4     | Steel Sword, Arcane Tome, Runic Blade     | Chain Mail, Mage Robes             |
| 5     | Runic Blade, Arcane Tome, Steel Sword     | Chain Mail, Mage Robes             |
| 6     | Runic Blade, Arcane Tome, Steel Sword     | Chain Mail, Mage Robes             |
| 7     | Runic Blade, Arcane Tome                  | Chain Mail, Mage Robes             |

**Potion Shop (all floors):** Health Potion 15g, Greater Health Potion 25g, Mana Potion 12g, Elixir 35g, Antidote 20g.

---

## 8. Floor Structure

**Source:** `game/engine.py`, `game/dungeon.py`

```
Floors 1–6:
  [2–3 random enemies from floor pool]
    → after each non-final enemy: rest event (20% HP / 5–20g / 30% MP / potion / nothing)
    → 35% chance: drop Health Potion or Mana Potion
  → floor cleared
  → prisoner bonus check (floor 3 only, if spared on floor 1): +10g, +5 max HP, Dragon Tears drop
  → story event (if available)
  → shop
  → descend

Floor 7:
  Dragon boss only → victory screen with ending
```

**Rest events (after non-final enemy):** restore 20% max HP / gain 5–20g / restore 30% max MP / gain Health Potion / nothing.

---

## 9. Story Events

**Source:** `game/story_data.py`

Each floor (1–6) has one main event. Alternate events exist per floor but require `get_event()` in `story_logic.py` to use `random.choice` to activate them (currently returns first match).

### Main Events

| Floor | Situation           | Universal Choices                        | Warrior Choice         | Mage Choice          | Rogue Choice           |
|-------|---------------------|------------------------------------------|------------------------|----------------------|------------------------|
| 1     | Prisoner in cage    | Spare / Ignore / Execute                 | Stood Guard (+4 DEF, +10 HP) | Healed (+3 MAG, −5 HP) | Looted (+25g, +2 ATK) |
| 2     | Burning village     | Aid / Ignore / Loot                      | Sworn Oath (+1 ATK, +4 DEF) | Warded (+3 MAG)     | Left Supplies (+2 ATK, +2 DEF) |
| 3     | Demon pact offer    | Refuse / Dark Pact / Bargain Sage        | Endured (+5 DEF, +10 HP) | Improved Pact (+4 MAG, −10 HP) | Stole Reagents (+3 ATK, +20g) |
| 4     | Ancient tome        | Decipher / Sacrifice Self / Keep Secrets | Tactical (+4 ATK, +3 DEF) | Channeled Tome (+6 MAG) | Runed Blade (shadow_blade drop) |
| 5     | Fallen knight       | Fight / Redeem / Execute                 | Duel (+5 ATK, +5 DEF) | Purified (+4 MAG, +2 DEF) | Sneaked (+3 ATK, +15g) |
| 6     | Dragon Tear relic   | Shatter / Keep / Drink                   | Crushed (+5 ATK, +5 DEF) | Absorbed (+6 MAG, +10 HP) | Pocketed (+40g, +3 ATK) |

### Alternate Events (per floor, activate via `random.choice` in `get_event()`)

| Floor | Situation     | Choices           |
|-------|---------------|-------------------|
| 1     | Trader        | Bargain / Refuse / Rob |
| 2     | Ruins         | Study / Ignore / Desecrate |
| 3     | Prisoner cell | Free / Leave / Use |
| 4     | Shrine        | Honor / Reject / Destroy |
| 5     | Rival         | Defeat / Ally / Spare |
| 6     | Vision        | Heed / Ignore / Question |

---

## 10. Story Endings

**Source:** `game/story_data.py` — `ENDINGS`, `_SCORES`

`resolve_ending()` scores all accumulated story flags, returns highest-scoring ending. Default: `reluctant_hero`.

| Ending Key      | Dragon HP Mult | Dragon ATK Mult | Player DEF Bonus | Ally Dmg/Turn | Revive Once | Player MAG Mult |
|-----------------|----------------|-----------------|-----------------|---------------|-------------|-----------------|
| true_hero       | ×0.85          | ×0.90           | +10             | —             | —           | —               |
| dark_conqueror  | ×1.0           | ×0.80           | —               | 8/turn        | —           | —               |
| scholar_king    | ×0.90          | ×1.0            | —               | —             | —           | ×1.35           |
| martyred_saint  | ×0.75          | ×1.15           | —               | —             | Yes         | —               |
| reluctant_hero  | ×1.0           | ×1.0            | —               | —             | —           | —               |
| shadow_broker   | ×1.0           | ×0.75           | +5              | —             | —           | —               |

### Key Scoring Flags

**true_hero** — heroic/merciful choices: `spared_prisoner` (+2), `aided_village` (+2), `refused_dark_pact` (+2), `redeemed_knight` (+3), `kept_tear` (+3). Penalised by: `dark_pact` (−2), `looted_village` (−2).

**dark_conqueror** — aggressive/ruthless: `executed_prisoner` (+2), `looted_village` (+2), `dark_pact` (+2), `executed_knight` (+2), `drank_tear` (+2). Penalised by: `refused_dark_pact` (−2), `spared_prisoner` (−1).

**scholar_king** — knowledge/magic: `deciphered_tome` (+3), `mage_channeled_tome` (+3), `mage_absorbed_tear` (+3), `bargained_sage` (+2), `mage_improved_pact` (+2). Penalised by: `dark_pact` (−1).

**martyred_saint** — self-sacrifice: `sacrificed_self` (+5), `spared_prisoner` (+1), `aided_village` (+1), `redeemed_knight` (+2), `kept_tear` (+2). Penalised by: `dark_pact` (−2), `looted_village` (−2).

**reluctant_hero** — avoidance/neutral: `ignored_prisoner` (+2), `ignored_village` (+2), `fought_knight` (+2), `rogue_sneaked` (+1).

**shadow_broker** (Rogue-dominant): `rogue_stole_reagents` (+3), `rogue_runed_blade` (+3), `rogue_pocketed_tear` (+3), `rogue_sneaked` (+2), `rogue_smooth_talk` (+2). Penalised by: `refused_dark_pact` (−2), `spared_prisoner` (−1).
