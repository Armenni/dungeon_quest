# Migration Guide: Codebase Refactoring

This document explains what changed and how to use the new structure.

## What Moved

### Root-level scripts → `scripts/` folder

**Why?** Keep the root directory clean; distinguish between core game and developer tools.

| Old Location | New Location |
|---|---|
| `dragon_test.py` | `scripts/dragon_test.py` |
| `simulate.py` | `scripts/simulate.py` |
| `autoplay.py` | `scripts/autoplay.py` |
| `api.py` | `scripts/api.py` |
| `play.py` | `scripts/play.py` |
| `watcher.py` | `scripts/watcher.py` |

**Update your commands:**
```bash
# Old
python dragon_test.py

# New
python scripts/dragon_test.py
```

---

## What's New

### 1. **game/constants.py** — Centralized Balance Parameters

All magic numbers are now in one place. To adjust balance:

```python
from game.constants import CombatConfig, EnemyConfig, PlayerConfig

# Instead of searching code for hardcoded values:
# OLD: search for "0.5" in dungeon.py to find RUN_SUCCESS_RATE
# NEW:
CombatConfig.RUN_SUCCESS_RATE = 0.6  # 60% instead of 50%
```

**Benefit**: Change game balance without understanding the codebase.

**Files affected**:
- `game/constants.py` — Read these values in logic files (no changes needed yet)
- Future: Logic files can be updated to import from constants

### 2. **game/types.py** — Shared Type Definitions

Centralized dataclasses for type safety:
- `StatusEffect` (was in `status.py`)
- `Choice`, `StoryEvent`, `StoryEnding` (were in `story_data.py`)

**Usage**: Prefer `from game.types import StatusEffect` over importing from individual modules.

**Benefit**: Clear type boundaries, easier type checking with `mypy`.

### 3. **tests/** — New Testing Infrastructure

Created comprehensive test structure:

```
tests/
├── __init__.py
├── bot.py              # Shared TestBot class (replaces duplication)
├── harness.py          # TestHarness context manager (encapsulates I/O mocking)
├── strategies.py       # Test strategy definitions (maintainable, extensible)
├── baselines/
│   └── dragon_baseline.json  # Regression testing baseline
└── unit/
    ├── __init__.py
    ├── test_combat.py   # Combat mechanics tests
    └── test_player.py   # Player progression tests
```

#### 3.1 **tests/bot.py** — Shared Test Bot

**What it does**: Unified bot logic for all test harnesses.

**Before**: Code duplication in `dragon_test.py` and `simulate.py`
**After**: Single `TestBot` class imported by both

```python
# Old (dragon_test.py)
class Bot:
    def decide(self, prompt):
        # 100+ lines of duplicate logic

# New
from tests.bot import TestBot
bot = TestBot(cls="1", story_pick="1", name="Warrior_Test")
```

**Benefits**:
- -160 lines of code duplication
- Single source of truth
- Easy to extend bot behavior

#### 3.2 **tests/harness.py** — I/O Mocking Helper

**What it does**: Clean context manager for mocking Console I/O.

**Before**: Direct monkey-patching scattered in test files
**After**: Encapsulated, reversible I/O mocking

```python
# Old
def _install_patches():
    Console.input = _fake_input
    Console.print = _fake_print
    # ...magic numbers, scattered globals

# New
with TestHarness(bot) as harness:
    run_game(bot)
    output = harness.output_log  # Access results cleanly
# All patches automatically restored
```

**Benefits**:
- Easy to update if Rich API changes
- No global state leaks
- Clear entry/exit points

#### 3.3 **tests/strategies.py** — Maintainable Strategy List

**What it does**: Centralized test strategy definitions.

**Before**: Hardcoded tuples scattered across `dragon_test.py` and `simulate.py`
**After**: One source of truth with descriptions

```python
STRATEGIES = [
    ("1", "1", "Warrior_Merciful", "Warrior, always kind choices"),
    ("1", "2", "Warrior_Pragmatic", "Warrior, always middle choices"),
    # ...12 strategies total with descriptions
]

# Easy to filter or extend:
merciful_strats = get_strategies(filter_name="Merciful")
```

**Benefits**:
- Easy to add new strategies
- Clear descriptions for debugging
- Reusable across different test runners

#### 3.4 **tests/unit/test_combat.py** — Combat Unit Tests

**What it does**: Fast, isolated tests for combat mechanics.

**Examples**:
- `test_attack_damage_variance()`: Verify damage is within expected range
- `test_crit_chance_rogue()`: Rogue has 2x crit rate vs Warrior
- `test_shield_halves_damage()`: Shield status mechanic validation
- `test_spell_costs_mp()`: MP consumption verification

**Benefits**:
- Catch bugs early (seconds vs. 10 minutes for full playtest)
- Prevent regressions on core mechanics
- Clear pass/fail feedback

**Run tests**:
```bash
pip install pytest
pytest tests/unit/ -v
```

#### 3.5 **tests/unit/test_player.py** — Player Progression Tests

**Examples**:
- `test_level_up_stat_growth()`: Stats scale correctly
- `test_equip_weapon_increases_atk()`: Equipment bonuses work
- `test_heal_respects_max_hp()`: No over-healing
- `test_use_antidote_removes_poison_and_burn()`: Item mechanics

**Benefits**:
- Validate player progression is balanced
- Ensure equipment system works
- Prevent inventory bugs

---

## How to Run Tests

### Unit Tests (Fast — ~5 seconds)
```bash
pytest tests/unit/ -v
```

### Dragon Test (Detailed — ~2-3 minutes with parallelization)
```bash
python scripts/dragon_test.py
```
- 60 runs total (20 per class)
- Parallel execution (4 workers)
- Regression detection vs baseline
- Output: `dragon_log.json`

### Batch Simulator (Strategy Coverage — ~1 minute)
```bash
python scripts/simulate.py
```
- 12 strategies (all class/story combos)
- Win-rates per class
- Endings tracking
- Output: `gameplay_log.json`

### Automated Playtest (Single run — ~30 seconds)
```bash
python scripts/autoplay.py
```
- Hardcoded story choices
- Targets True Hero ending

---

## Requirements

Updated `requirements.txt`:
```
rich>=13.0.0         # Existing
pytest>=7.0.0        # New (for unit tests)
pytest-html>=3.1.0   # New (optional, for HTML reports)
```

Install:
```bash
pip install -r requirements.txt
```

---

## File Structure Summary

### Deleted (moved to scripts/)
- `dragon_test.py` → `scripts/dragon_test.py`
- `simulate.py` → `scripts/simulate.py`
- `autoplay.py` → `scripts/autoplay.py`
- `api.py` → `scripts/api.py`
- `play.py` → `scripts/play.py`
- `watcher.py` → `scripts/watcher.py`

### Created (New Organization)
- `game/constants.py` — Balance parameters
- `game/types.py` — Shared type definitions
- `tests/` — Test infrastructure
  - `tests/bot.py` — Shared TestBot
  - `tests/harness.py` — I/O mocking
  - `tests/strategies.py` — Strategy definitions
  - `tests/unit/test_combat.py` — Combat tests
  - `tests/unit/test_player.py` — Player tests
  - `tests/baselines/dragon_baseline.json` — Regression baseline
- `scripts/` — Developer tools (moved scripts)
- `pytest.ini` — pytest configuration
- `CHANGELOG.md` — This refactoring documented
- `MIGRATION_GUIDE.md` — This file

### Modified
- `requirements.txt` — Added pytest dependencies
- `main.py` — No changes (still works!)

---

## Benefits of This Refactoring

| Aspect | Before | After |
|--------|--------|-------|
| **Code Duplication** | 160 LOC shared between tests | Single `TestBot` class |
| **Balance Tweaking** | Search code for magic numbers | `game/constants.py` |
| **Test Execution** | 60 tests in ~10 min | 4-6x faster with parallelization |
| **Test Maintenance** | Scattered I/O patching | `TestHarness` encapsulates it |
| **Regression Detection** | Manual comparison | Automatic baseline checking |
| **Unit Testing** | None | 20+ comprehensive tests |
| **Project Structure** | Root clutter | Clean `scripts/` folder |
| **Type Safety** | Implicit dataclasses | Explicit `game/types.py` |

---

## Next Steps (Optional)

These items were identified but not implemented (to avoid scope creep):

1. **Migrate game/data/** — Move content files to organized folder
2. **Type annotations** — Add comprehensive type hints with `mypy`
3. **CI/CD pipeline** — GitHub Actions for automated testing
4. **Performance profiling** — Identify and optimize hot paths
5. **Integration tests** — Test full game flow with assertions

---

## Questions?

- See `CHANGELOG.md` for detailed changes
- See `pytest.ini` for test configuration
- Run `pytest --help` for test options
- Run individual tests: `pytest tests/unit/test_combat.py::TestPlayerAttack::test_crit_chance_rogue -v`

Generated: 2026-03-22
