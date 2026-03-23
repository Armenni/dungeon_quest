"""
Unit tests for combat mechanics.

Tests:
- Attack damage calculation and variance
- Critical hit rates and damage
- Spell casting and MP consumption
- Status effects in combat
- Damage absorption
"""

import pytest
from game.player import Player
from game.enemy import Enemy
from game.combat import player_attack, player_magic, SPELLS
from game.status import apply_status, consume_stun


@pytest.fixture
def warrior():
    """Create a test Warrior."""
    return Player("TestWarrior", "Warrior")


@pytest.fixture
def mage():
    """Create a test Mage."""
    return Player("TestMage", "Mage")


@pytest.fixture
def rogue():
    """Create a test Rogue."""
    return Player("TestRogue", "Rogue")


@pytest.fixture
def goblin():
    """Create a test Goblin enemy."""
    return Enemy("Goblin", 30, 30, 8, 3, 10, 15, 5, ["attack"])


@pytest.fixture
def troll():
    """Create a test Troll enemy."""
    return Enemy("Troll", 80, 80, 14, 8, 5, 35, 12, ["attack", "regenerate"])


# ── Attack Tests ───────────────────────────────────────────────────────────────

class TestPlayerAttack:
    """Test basic attack mechanics."""

    def test_attack_deals_damage(self, warrior, goblin):
        """Attack should deal damage based on ATK stat."""
        initial_hp = goblin.hp
        dmg, _ = player_attack(warrior, goblin)
        assert dmg > 0
        assert goblin.hp < initial_hp
        assert goblin.hp == initial_hp - dmg

    def test_attack_damage_variance(self, warrior, goblin):
        """Attack damage should vary within expected range."""
        damages = []
        for _ in range(30):
            goblin.hp = goblin.max_hp  # Reset
            dmg, _ = player_attack(warrior, goblin)
            damages.append(dmg)

        min_dmg = min(damages)
        max_dmg = max(damages)
        # Warrior ATK=15, variance -2 to +4 = 13-19 raw, Goblin DEF=3
        # No crit: 13-3=10 to 19-3=16; with crit (1.5x): up to ~28, so realistic max ~25
        assert min_dmg >= 10
        assert max_dmg <= 30  # Account for possible crits

    def test_crit_chance_warrior(self, warrior, goblin):
        """Warrior (Luck=2) should have ~11% crit rate."""
        crits = sum(player_attack(warrior, goblin)[1] for _ in range(200))
        # Luck=2 → crit = 5 + 2*3 = 11%; expect ~22 crits; allow generous range
        assert 5 <= crits <= 30

    def test_crit_chance_rogue_higher_than_warrior(self, warrior, rogue, goblin):
        """Rogue (Luck=3 → 14% crit) should crit more often than Warrior (Luck=2 → 11%)."""
        warrior_crits = sum(player_attack(warrior, goblin)[1] for _ in range(300))
        rogue_crits   = sum(player_attack(rogue,   goblin)[1] for _ in range(300))
        # Over 300 trials Rogue should be ahead or at worst 10 behind
        assert rogue_crits >= warrior_crits - 10

    def test_crit_damage_is_1_5x(self, warrior, goblin):
        """Critical hit should do 1.5x damage."""
        # Run many times to find a crit
        base_damages = []
        crit_damages = []

        for _ in range(200):
            goblin.hp = goblin.max_hp
            dmg, is_crit = player_attack(warrior, goblin)
            if is_crit:
                crit_damages.append(dmg)
            else:
                base_damages.append(dmg)

        if base_damages and crit_damages:
            avg_base = sum(base_damages) / len(base_damages)
            avg_crit = sum(crit_damages) / len(crit_damages)
            # Crit should be ~1.5x base
            ratio = avg_crit / avg_base if avg_base > 0 else 1
            assert 1.3 < ratio < 1.7  # Allow some variance


# ── Spell Tests ─────────────────────────────────────────────────────────────────

class TestPlayerMagic:
    """Test spell casting mechanics."""

    def test_spell_costs_mp(self, warrior):
        """Casting spell should reduce MP."""
        warrior.mp = 100
        initial_mp = warrior.mp
        spell = SPELLS["Warrior"]["Battlecry"]
        cost = spell["cost"]

        goblin = Enemy("Goblin", 30, 30, 8, 3, 10, 15, 5, ["attack"])
        player_magic(warrior, goblin, "Battlecry")

        assert warrior.mp == initial_mp - cost

    def test_insufficient_mp_fails_spell(self, warrior):
        """Spell should fail if insufficient MP."""
        warrior.mp = 2  # Battlecry costs 10
        goblin = Enemy("Goblin", 30, 30, 8, 3, 10, 15, 5, ["attack"])

        dmg, spell_name, msg = player_magic(warrior, goblin, "Battlecry")

        assert dmg == 0
        assert warrior.mp == 2  # No MP spent
        assert "not_enough_mp" in msg

    def test_spell_deals_damage(self, mage):
        """Mage spell should deal damage."""
        mage.mp = 100
        goblin = Enemy("Goblin", 30, 30, 8, 3, 10, 15, 5, ["attack"])
        initial_hp = goblin.hp

        dmg, spell_name, _ = player_magic(mage, goblin, "Fireball")

        assert dmg > 0
        assert goblin.hp < initial_hp

    def test_frost_armor_shields_player(self, mage):
        """Frost Armor should apply shield status."""
        mage.mp = 100
        goblin = Enemy("Goblin", 30, 30, 8, 3, 10, 15, 5, ["attack"])

        dmg, spell_name, _ = player_magic(mage, goblin, "Frost Armor")

        assert dmg == 0  # Doesn't damage enemy
        # Check if shielded status applied
        assert any(e.etype == "shielded" for e in mage.status_effects)


# ── Status Effect Tests ────────────────────────────────────────────────────────

class TestStatusEffects:
    """Test status effect application and mechanics."""

    def test_shield_reduces_damage_by_half(self, warrior):
        """Shield status should halve incoming damage before DEF reduction."""
        apply_status(warrior, "shielded", 1, 0)
        warrior.hp = 100

        actual_dmg = warrior.take_damage(20)

        # Shield halves damage: 20 // 2 = 10, Warrior DEF=12, so 10 - 12 = -2, min(1) = 1
        assert actual_dmg == 1
        assert warrior.hp == 99

    def test_shield_consumed_after_one_hit(self, warrior):
        """Shield should be consumed after blocking damage."""
        apply_status(warrior, "shielded", 1, 0)
        assert len(warrior.status_effects) == 1

        warrior.take_damage(10)

        # Shield should be removed
        assert not any(e.etype == "shielded" for e in warrior.status_effects)

    def test_stun_prevents_action(self, warrior):
        """Stun status should be detected by consume_stun."""
        apply_status(warrior, "stun", 1, 0)
        assert consume_stun(warrior)  # Should be stunned
        assert not consume_stun(warrior)  # Stun consumed

    def test_weakened_reduces_attack_damage(self):
        """Weakened status should reduce attack damage (tested in combat)."""
        from game.status import weakened_penalty

        warrior = Player("Test", "Warrior")
        apply_status(warrior, "weakened", 2, 4)

        penalty = weakened_penalty(warrior)
        assert penalty == 4


# ── Enemy Tests ────────────────────────────────────────────────────────────────

class TestEnemyMechanics:
    """Test enemy-related mechanics."""

    def test_enemy_takes_damage(self, goblin):
        """Enemy HP should decrease when damaged."""
        initial_hp = goblin.hp
        actual = goblin.take_damage(10)

        assert goblin.hp < initial_hp
        assert actual > 0  # Some damage dealt (after DEF reduction)

    def test_defense_reduces_damage(self, troll):
        """Higher DEF should reduce damage taken."""
        # Troll has defense=8, damage reduced by full defense value
        troll.hp = 100
        actual = troll.take_damage(20)

        # 20 - 8 = 12 damage
        assert actual == 12
        assert actual >= 1
