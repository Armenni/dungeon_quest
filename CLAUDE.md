# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Game

```bash
pip install rich
python main.py
```

No build step, no tests. The only dependency is `rich>=13.0.0`.

## Architecture

Turn-based terminal RPG. Entry point is `main.py` → creates `UI`, prompts for name/class, then hands off to `Dungeon.run()`.

### Data flow

```
main.py
  └─ Dungeon.run()          # floor loop, combat loop, shop, story events
       ├─ combat.py          # player_attack / player_magic / enemy_turn → return (dmg, msg, ability)
       ├─ status.py          # tick_statuses / apply_status / consume_stun
       ├─ story.py           # EVENTS list → resolve_ending() scores flags → ENDINGS dict
       ├─ shop.py            # run_shop() uses SHOP_STOCK + POTION_SHOP
       └─ ui.py              # all Rich rendering; UI.log is a rolling 5-line combat log
```

### Key design patterns

- **All game text is hardcoded** — no i18n layer yet. Every user-visible string lives in the module that owns the logic (combat messages in `combat.py`, story text in `story.py`, shop labels in `shop.py`, etc.).
- **Enemy abilities** are string identifiers (e.g. `"fire_breath"`, `"wing_stun"`) stored in `Enemy.abilities`. `enemy_turn()` in `combat.py` dispatches on them with `if ability == "..."` blocks.
- **Story endings** are determined by scoring `player.story_flags` against `_SCORES` in `story.py`. Each story choice sets one flag; `resolve_ending()` picks the highest-scoring ending key from `ENDINGS`.
- **Dragon modifiers** (`dragon_modifier` dict in each ending) are passed from `resolve_ending()` into `_combat()` and alter boss stats, grant passive effects per-turn (`ally_dmg_per_turn`), and can trigger a one-shot revive (`revive_once`).
- **Equipment stat recalc**: `Player._recalc_equipment()` always recomputes effective stats from `_base_*` fields plus equipped item bonuses — never mutate `atk/defense/magic/max_hp` directly; go through `apply_bonus()` or equip/unequip instead.
- **`UI`** is passed by reference everywhere. `UI.log` accumulates combat messages; `show_combat()` renders the last 5. Clear with `clear_log()` at the start of each combat.
