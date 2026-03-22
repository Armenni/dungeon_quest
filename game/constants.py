"""
Game balance constants — centralized for easy tuning.

Change values here to rebalance the entire game without touching logic files.
"""

# ── Player Configuration ───────────────────────────────────────────────────────

class PlayerConfig:
    """Player stats, progression, and scaling."""

    # Base stats per class at level 1
    CLASS_STATS = {
        "Warrior": {"hp": 120, "mp": 20,  "atk": 15, "defense": 12, "spd": 8,  "magic": 5},
        "Mage":    {"hp": 70,  "mp": 80,  "atk": 8,  "defense": 6,  "spd": 9,  "magic": 20},
        "Rogue":   {"hp": 90,  "mp": 30,  "atk": 12, "defense": 8,  "spd": 15, "magic": 8},
    }

    # Level progression
    LEVEL_UP_MULTIPLIER = 1.5          # XP threshold grows by 1.5x per level
    STARTING_XP_THRESHOLD = 50         # XP needed to reach level 2

    # Stat growth per level
    ATK_PER_LEVEL = 3
    DEF_PER_LEVEL = 2
    MAGIC_PER_LEVEL = 2
    MAX_HP_PER_LEVEL = 15
    MAX_MP_PER_LEVEL = 10

    # HP healing on level-up
    HEAL_ON_LEVEL_UP = True            # Full heal on level-up

    # Inventory
    STARTING_INVENTORY = 2             # Health potions to start with
    STARTING_GOLD = 10

    # Rest events between floors
    REST_HP_HEAL_PCT = 0.2             # Heal 20% of max HP
    REST_MP_RESTORE_PCT = 0.3          # Restore 30% of max MP
    REST_GOLD_MIN = 5
    REST_GOLD_MAX = 20


# ── Enemy Configuration ────────────────────────────────────────────────────────

class EnemyConfig:
    """Enemy scaling, abilities, and progression."""

    # Floor scaling: enemies grow stronger per floor
    SCALE_PER_FLOOR = 0.3              # 30% stronger each floor

    # Dragon limits
    DRAGON_MAX_SCALE = 2.0             # Cap Dragon scaling at 7-floor version
    DRAGON_ABILITY_FIRE_BREATH_MULTIPLIER = 1.6   # Fire breath does 1.6x ATK

    # Enemy floor pools
    FLOOR_ENEMIES = {
        1: ["Goblin", "Goblin", "Skeleton"],
        2: ["Goblin", "Orc", "Skeleton"],
        3: ["Orc", "Skeleton", "Dark Mage"],
        4: ["Orc", "Dark Mage", "Troll"],
        5: ["Dark Mage", "Troll", "Orc"],
        6: ["Troll", "Dark Mage", "Troll"],
        7: ["Dragon"],
    }

    # Encounters per floor
    ENEMIES_PER_FLOOR_MIN = 2
    ENEMIES_PER_FLOOR_MAX = 3

    # Item drops
    ITEM_DROP_RATE = 0.35              # 35% chance after enemy defeat
    DROP_POOL = ["health_potion", "mana_potion"]


# ── Combat Configuration ───────────────────────────────────────────────────────

class CombatConfig:
    """Combat mechanics and balance."""

    # Critical hits
    CRIT_CHANCE_BASE = 0.1             # 10% for Warrior/Mage
    CRIT_CHANCE_ROGUE = 0.2            # 20% for Rogue (2x)
    CRIT_DAMAGE_MULTIPLIER = 1.5       # Crit does 1.5x damage

    # Damage formula
    ATTACK_VARIANCE_MIN = -2
    ATTACK_VARIANCE_MAX = 4
    SPELL_VARIANCE_MIN = -3
    SPELL_VARIANCE_MAX = 5

    # Defense
    DEFENSE_REDUCTION = 0.5            # Defense reduces damage by DEF//2

    # Shield status effect
    SHIELD_DAMAGE_REDUCTION = 0.5      # Shields halve incoming damage

    # Run away
    RUN_SUCCESS_RATE = 0.5             # 50% chance to flee combat

    # Status effects
    WEAKENED_PENALTY_MAGNITUDE = 4     # Reduces ATK by 4

    # Enemy abilities scaling
    HEAVY_STRIKE_MULTIPLIER = 1.5
    TAIL_SWIPE_MULTIPLIER = 1.3
    FIREBALL_MULTIPLIER = 1.8
    FIRE_BREATH_MULTIPLIER = 1.6       # Reduced from 2.0
    TOXIC_BREATH_MULTIPLIER = 1.5
    STUN_BASH_MULTIPLIER = 0.8

    # Regeneration
    REGENERATE_MIN = 10
    REGENERATE_MAX = 20


# ── Game Configuration ─────────────────────────────────────────────────────────

class GameConfig:
    """Overall game progression and balance."""

    # Dungeon structure
    MAX_FLOORS = 7
    BOSS_FLOOR = 7                     # Dragon is on floor 7

    # Story/Events
    PRISONER_RETURN_FLOOR = 3          # Prisoner returns on floor 3
    PRISONER_RETURN_BONUS_GOLD = 10
    PRISONER_RETURN_BONUS_MAX_HP = 5

    # Status effect durations
    BURN_DURATION = 3                  # Turns
    BURN_DAMAGE = 5                    # Damage per tick
    POISON_DURATION = 3
    POISON_DAMAGE = 4
    STUN_DURATION = 1                  # 1 turn (skips one action)
    WEAKENED_DURATION = 2
    SHIELDED_DURATION = 2

    # Boss modifiers from story endings
    DRAGON_MODIFIER_BASE = {}
    # Examples of modifiers applied by endings:
    # {
    #   "dragon_hp_mult": 0.7,         # Weak dragon (merciful path)
    #   "dragon_atk_mult": 1.0,
    #   "player_def_bonus": 0,
    #   "ally_dmg_per_turn": 0,
    #   "revive_once": False,
    #   "bonus_msg": "weak_dragon"
    # }


# ── Shop Configuration ─────────────────────────────────────────────────────────

class ShopConfig:
    """Shop prices and availability."""

    # Price adjustments by floor (optional future feature)
    PRICE_SCALE_BY_FLOOR = 1.0         # Prices don't scale yet

    # Shop leave command
    SHOP_LEAVE_CMD_EN = "l"
    SHOP_LEAVE_CMD_PT = "s"
