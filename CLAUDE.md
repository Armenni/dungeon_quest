# CLAUDE.md

## Running the Game

```bash
pip install rich
python main.py
```

Run tests:
```bash
pip install pytest pytest-html
pytest tests/unit/ -v
```

## Two Entry Points

| Entry point | Purpose |
|---|---|
| `main.py` → `Dungeon.run()` | TUI (terminal UI, Rich rendering) |
| `game/engine.py` → `GameEngine` | Stateless API (no UI dependency), used by `tools/` |

Both call the same `combat.py`, `story_logic.py`, `player.py`, `status.py`.

## File Map

```
GAMEDATA.md           Quick-reference for all game stats, formulas, enemies, items, endings — read before designing content

game/
  i18n.py             set_language() merges {lang}_ui + {lang}_story dicts; t(key, **kwargs)
  lang/
    en_ui.py          English UI/combat/shop strings (~130 lines) — source of truth for UI text
    en_story.py       English story events + endings text (~360 lines) — source of truth for narrative
    pt_br_ui.py       Portuguese UI strings
    pt_br_story.py    Portuguese story + endings

  story_data.py       Choice + StoryEvent dataclasses, EVENTS list, ENDINGS dict, _SCORES table
  story_logic.py      resolve_ending(), get_event(), apply_effect()  (~50 lines, stable)
  story.py            Re-export shim — do not edit; import from story_data/story_logic directly

  combat.py           player_attack(), player_magic(), enemy_turn(), SPELLS dict
  dungeon.py          TUI game loop (floor loop, combat loop, shop, story events)
  ui.py               All Rich rendering; UI.log is a rolling 5-line combat log
  player.py           Player class — stats, equipment, inventory, levelling
  enemy.py            Enemy dataclass, make_enemy(), FLOOR_ENEMIES (7 floors)
  equipment.py        EQUIPMENT dict, SHOP_STOCK per floor, POTION_SHOP
  items.py            ITEMS dict (potions, elixirs, antidotes)
  shop.py             run_shop() — TUI only
  status.py           tick_statuses(), apply_status(), consume_stun()
  engine.py           GameEngine state machine — full game flow, no UI (7 floors)

  constants.py        Balance constants (PlayerConfig, EnemyConfig, CombatConfig, GameConfig,
                      ShopConfig) — NOT yet imported by game code; reference/tuning doc only
  types.py            Dataclass definitions — NOT yet imported by game code; reference doc only

tools/                Developer tools (not part of the playable game)
  llm_playtest/
    llm_playtest.py   LLM-driven playtester — Claude plays step by step, logs UX/bugs/wishes
    logs/             Per-run JSON + MD reports (gitignored)
  fast_sim/
    fast_sim.py       Batch simulator — hundreds/thousands of runs, balance + logic testing
    logs/             Per-run JSON + MD reports (gitignored)
  api/
    api_server.py     REST API server wrapping engine (requires flask)
    watcher.py        File-bridge between Claude Code and the API
    logs/             Gitignored

tests/
  bot.py              Shared TestBot class (used by unit tests)
  harness.py          TestHarness context manager for I/O mocking
  strategies.py       12 test strategies (3 classes × story paths)
  baselines/
    dragon_baseline.json   Regression baseline for Dragon fight balance
    sim_baseline.json      Regression baseline for fast_sim.py (created by --save-baseline)
  unit/
    test_combat.py    15 combat unit tests
    test_player.py    12 player progression unit tests

docs/                 Generated documentation (reference only, not maintained actively)
  CHANGELOG.md
  MIGRATION_GUIDE.md
  REFACTORING_SUMMARY.md
  DOCUMENTATION_INDEX.md

  (tool logs live in tools/*/logs/ — gitignored, not source)
```

## i18n Pattern

`set_language("pt_br")` loads `pt_br_ui.py` + `pt_br_story.py` and merges their `STRINGS` dicts.
All user-visible text goes through `t(key, **kwargs)` — never hardcode strings in logic files.

- UI/combat/shop strings → `en_ui.py`
- Story event text, endings, prisoner bonus, shop_weapons_locked → `en_story.py`

## Key Invariants

- **Equipment stat recalc**: Never mutate `atk/defense/magic/max_hp` directly. Use `apply_bonus()` or `equip()`/`unequip()`. `Player._recalc_equipment()` always recomputes from `_base_*` fields.
- **Story endings**: `resolve_ending(player.story_flags)` scores flags against `_SCORES` in `story_data.py` and returns the highest-scoring ending from `ENDINGS`.
- **Dragon modifiers**: `dragon_modifier` dict from `resolve_ending()` is passed into `_combat()`. Keys: `dragon_hp_mult`, `dragon_atk_mult`, `player_def_bonus`, `ally_dmg_per_turn`, `revive_once`, `player_magic_mult`, `bonus_msg`.
- **Enemy abilities**: String identifiers (e.g. `"fire_breath"`) stored in `Enemy.abilities`. `enemy_turn()` in `combat.py` dispatches with `if ability == "..."` blocks.
- **Shop exit command**: Language-specific — stored as `shop_leave_cmd` key in each `*_ui.py` file (`"l"` for English, `"s"` for Portuguese).
- **constants.py / types.py**: These files exist but are NOT imported by any game module. They are balance reference documents. Do not add imports from them without a deliberate refactor decision.
- **Alternate events**: `get_event(floor)` in `story_logic.py` returns the first matching event. Multiple `StoryEvent` entries with the same `floor_after` are supported by the data model but `get_event()` must be updated to `random.choice` to activate them.

## Navigation Hints

| Task | Read | Skip |
|---|---|---|
| Fix combat bug | `combat.py`, `en_ui.py` | `en_story.py`, `story_data.py` |
| Fix shop bug | `shop.py`, `en_ui.py` | `en_story.py`, `story_data.py` |
| Debug story scoring / ending logic | `story_logic.py` | `story_data.py`, both lang files |
| Add / edit a story event | `story_data.py`, `en_story.py` | `story_logic.py`, `en_ui.py` |
| Add a new language | `en_ui.py`, `en_story.py`, `main.py` | Everything else |
| Change UI rendering | `ui.py`, `en_ui.py` | `en_story.py` |
| Change player stats / levelling | `player.py` | Lang files |
| Tune balance numbers | `constants.py` (reference), then edit source | — |
| Run unit tests | `pytest tests/unit/ -v` | — |
| LLM playtester (Claude plays + feedback) | `python tools/llm_playtest/llm_playtest.py` | — |
| LLM playtester (dry run, no Claude) | `python tools/llm_playtest/llm_playtest.py --dry-run` | — |
| Balance check (50 runs) | `python tools/fast_sim/fast_sim.py` | — |
| Balance check (500 runs, Mage only) | `python tools/fast_sim/fast_sim.py --runs 500 --class Mage` | — |
| Dragon fight stress test | `python tools/fast_sim/fast_sim.py --mode dragon --runs 200` | — |

## Development Roadmap

The game is being expanded from a single dungeon crawler toward a persistent overworld
with base building, companions, and multiple dungeons. Development is planned in
playable iterations — each version is a complete, enjoyable game.

See memory files for the full iteration plan. Current target: **v0.1 — A Richer Dungeon**.

### v0.1 scope (next task)
1. Fix `get_event()` for random alternate event selection (1-line change)
2. Add 12 new story events (2 alternates per floor × 6 floors) via `/storyteller:create`
3. Add 2 new enemy types via `/enemy-designer:create`
4. Add 1 new Rogue-dominant ending ("Shadow Broker") via `/storyteller:create`

### Planned versions
| Version | Theme | Key addition |
|---|---|---|
| v0.1 | A Richer Dungeon | Alternate events, more enemies, new ending |
| v0.2 | It Remembers You | Save/load, 5-stat system (STR/INT/AGI/LUK/CHA), equip screen, D6 stat checks |
| v0.3 | The Refuge | Overworld loop, base screen, 3-node map |
| v0.4 | Something to Grind | Goblin Warrens dungeon, companion skill growth |
| v0.5 | Earn the Dragon | Cultist Camp, Cult Leader mini-boss, Dragon locked |
| v0.6 | The Base Lives | Full base buildings, companion injury/recovery, POC complete |
