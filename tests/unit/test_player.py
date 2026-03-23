"""
Unit tests for player mechanics.

Tests:
- Leveling and stat progression
- Equipment and stat recalculation
- Inventory management
- Healing and resource management
"""

import pytest
from game.player import Player
from game.equipment import EQUIPMENT
from game.items import ITEMS


@pytest.fixture
def warrior():
    """Create a test Warrior."""
    return Player("TestWarrior", "Warrior")


@pytest.fixture
def mage():
    """Create a test Mage."""
    return Player("TestMage", "Mage")


# ── Leveling Tests ──────────────────────────────────────────────────────────────

class TestPlayerLeveling:
    """Test player progression and leveling."""

    def test_player_starts_at_level_1(self, warrior):
        """New player should be level 1."""
        assert warrior.level == 1
        assert warrior.xp == 0

    def test_gain_xp_below_threshold_no_level_up(self, warrior):
        """Gaining XP below threshold should not trigger level-up."""
        leveled = warrior.gain_xp(30)
        assert not leveled
        assert warrior.level == 1
        assert warrior.xp == 30

    def test_gain_xp_meets_threshold_triggers_level_up(self, warrior):
        """Gaining XP to reach threshold should trigger level-up."""
        leveled = warrior.gain_xp(50)
        assert leveled
        assert warrior.level == 2

    def test_level_up_increases_stats(self, warrior):
        """Level-up should increase DEF, HP, and set pending stat choice."""
        initial_def = warrior.defense
        initial_hp = warrior.max_hp

        warrior.gain_xp(50)

        assert warrior.defense > initial_def
        assert warrior.max_hp > initial_hp
        # ATK/MAGIC require explicit stat choice (pending_stat_choice flag)
        assert warrior.pending_stat_choice is True

    def test_level_up_stat_growth_amounts(self, warrior):
        """Level-up should grow DEF and HP by expected amounts; pending stat choice for primaries."""
        warrior.gain_xp(50)

        # DEF +1, HP +10 per level-up (flat gains); ATK/MAGIC grow via stat choice
        assert warrior._base_defense == 12 + 1
        assert warrior._base_max_hp == 120 + 10
        assert warrior.pending_stat_choice is True

        # Applying a stat choice updates the derived ATK
        atk_before = warrior.atk
        warrior.apply_stat_up("strength")
        assert warrior.atk > atk_before
        assert warrior.pending_stat_choice is False

    def test_level_up_heals_player(self, warrior):
        """Level-up should restore HP to max."""
        warrior.hp = 10  # Take damage
        assert warrior.hp < warrior.max_hp

        warrior.gain_xp(50)

        assert warrior.hp == warrior.max_hp

    def test_xp_threshold_grows_per_level(self, warrior):
        """XP threshold should grow by 1.5x per level."""
        threshold_1 = warrior.xp_next
        warrior.gain_xp(50)
        threshold_2 = warrior.xp_next

        # xp_next multiplied by 1.5
        assert abs(threshold_2 - threshold_1 * 1.5) < 1  # Allow rounding


# ── Equipment Tests ────────────────────────────────────────────────────────────

class TestPlayerEquipment:
    """Test equipment equipping and stat recalculation."""

    def test_equip_weapon_increases_atk(self, warrior):
        """Equipping weapon should increase ATK."""
        initial_atk = warrior.atk
        sword = EQUIPMENT["iron_sword"]

        warrior.equip(sword)

        assert warrior.atk > initial_atk
        assert warrior.atk == initial_atk + sword.atk_bonus

    def test_equip_armor_increases_def(self, warrior):
        """Equipping armor should increase DEF."""
        initial_def = warrior.defense
        vest = EQUIPMENT["padded_vest"]

        warrior.equip(vest)

        assert warrior.defense > initial_def
        assert warrior.defense == initial_def + vest.def_bonus

    def test_equip_multiple_items_stack_bonuses(self, warrior):
        """Multiple equipped items should stack bonuses on top of derived base."""
        sword = EQUIPMENT["iron_sword"]
        vest = EQUIPMENT["padded_vest"]
        base_atk = warrior.atk  # capture before equipping
        base_def = warrior.defense

        warrior.equip(sword)
        warrior.equip(vest)

        assert warrior.atk == base_atk + sword.atk_bonus + vest.atk_bonus
        assert warrior.defense == base_def + sword.def_bonus + vest.def_bonus

    def test_equip_replaces_same_slot(self, warrior):
        """Equipping item in same slot should replace it."""
        sword1 = EQUIPMENT["iron_sword"]
        sword2 = EQUIPMENT["steel_sword"]

        msg1, old1 = warrior.equip(sword1)
        assert old1 is None  # First equip, no old equipment
        atk_with_sword1 = warrior.atk

        msg2, old2 = warrior.equip(sword2)
        atk_with_sword2 = warrior.atk

        # Sword2 is better (atk_bonus=8 vs 4)
        assert atk_with_sword2 > atk_with_sword1
        assert warrior.weapon == sword2
        assert old2 == sword1  # Old sword should be returned

    def test_equip_increases_max_hp(self, warrior):
        """Some equipment increases max HP."""
        chain_mail = EQUIPMENT["chain_mail"]
        initial_max_hp = warrior.max_hp

        warrior.equip(chain_mail)

        assert warrior.max_hp > initial_max_hp


# ── Inventory Tests ────────────────────────────────────────────────────────────

class TestPlayerInventory:
    """Test inventory and item usage."""

    def test_player_starts_with_potions(self, warrior):
        """New player should start with health potions."""
        assert len(warrior.inventory) == 2
        assert warrior.inventory[0].item_type == "potion"

    def test_use_potion_heals(self, warrior):
        """Using potion should heal player."""
        warrior.hp = 50
        initial_hp = warrior.hp

        msg = warrior.use_item(0)

        assert warrior.hp > initial_hp
        assert len(warrior.inventory) == 1  # Potion consumed

    def test_use_item_invalid_index_returns_error(self, warrior):
        """Using invalid item index should return error message."""
        msg = warrior.use_item(999)
        assert "invalid" in msg.lower()

    def test_use_elixir_heals_and_restores_mp(self, warrior):
        """Using elixir should heal HP and restore MP."""
        warrior.hp = 30
        warrior.mp = 5
        warrior.inventory = [ITEMS["elixir"]]

        msg = warrior.use_item(0)

        assert warrior.hp > 30
        assert warrior.mp > 5

    def test_use_antidote_removes_poison_and_burn(self, warrior):
        """Antidote should remove poison and burn status effects."""
        from game.status import apply_status

        apply_status(warrior, "poison", 3, 4)
        apply_status(warrior, "burn", 3, 5)
        assert len(warrior.status_effects) == 2

        warrior.inventory = [ITEMS["antidote"]]
        warrior.use_item(0)

        # Poison and burn should be removed
        assert not any(e.etype == "poison" for e in warrior.status_effects)
        assert not any(e.etype == "burn" for e in warrior.status_effects)


# ── Health & Mana Tests ────────────────────────────────────────────────────────

class TestPlayerResources:
    """Test health and mana mechanics."""

    def test_heal_respects_max_hp(self, warrior):
        """Heal should not exceed max HP."""
        warrior.hp = 100
        warrior.heal(100)

        assert warrior.hp == warrior.max_hp

    def test_take_damage_respects_min_1(self, warrior):
        """Damage should always deal at least 1 HP."""
        warrior.hp = 100
        actual = warrior.take_damage(0)

        assert actual >= 1
        assert warrior.hp < 100

    def test_restore_mp_respects_max_mp(self, mage):
        """Restore MP should not exceed max MP."""
        mage.mp = 50
        mage.restore_mp(100)

        assert mage.mp == mage.max_mp

    def test_apply_bonus_increases_stats(self, warrior):
        """apply_bonus should increase base stats permanently."""
        atk_before = warrior.atk
        def_before = warrior.defense
        magic_before = warrior.magic
        hp_before = warrior.max_hp

        warrior.apply_bonus(atk=5, defense=3, magic=2, max_hp=20)

        # Legacy atk/magic add to flat offsets (_base_atk/_base_magic)
        assert warrior._base_atk == 5       # starts at 0, +5
        assert warrior._base_magic == 2     # starts at 0, +2
        assert warrior._base_defense == 12 + 3
        assert warrior._base_max_hp == 120 + 20
        # Effective stats should have grown
        assert warrior.atk > atk_before
        assert warrior.defense > def_before
        assert warrior.magic > magic_before
        assert warrior.max_hp > hp_before
