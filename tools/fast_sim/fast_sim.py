#!/usr/bin/env python3
"""
Fast Simulator — headless batch runner for balance and logic testing.

Runs hundreds or thousands of games in parallel using random/fixed strategies.
Consolidates simulate.py and dragon_test.py into one tool.

Usage:
    python tools/fast_sim/fast_sim.py                              # 50 runs, all classes
    python tools/fast_sim/fast_sim.py --runs 500                   # 500 random runs
    python tools/fast_sim/fast_sim.py --runs 200 --class Mage      # Mage only
    python tools/fast_sim/fast_sim.py --mode dragon --runs 100     # Dragon fight only
    python tools/fast_sim/fast_sim.py --strategy dark              # All runs use dark path choices
    python tools/fast_sim/fast_sim.py --baseline                   # Compare vs saved baseline
    python tools/fast_sim/fast_sim.py --save-baseline              # Save current results as baseline

Output:
    - Live progress in terminal
    - tools/fast_sim/logs/sim_{strategy}_{runs}runs_{winrate}pct_{timestamp}.json
    - tools/fast_sim/logs/sim_{strategy}_{runs}runs_{winrate}pct_{timestamp}.md
"""

import argparse
import json
import os
import random
import re
import sys
from datetime import datetime
from multiprocessing import Pool, cpu_count

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")
BASELINE_PATH = os.path.join(os.path.dirname(__file__), "../../tests/baselines/sim_baseline.json")


# ── Bot decision logic ─────────────────────────────────────────────────────────

def _bot_decide_from_state(state: dict, story_strategy: str) -> str:
    """Make a decision from structured engine state. No prompt parsing needed."""
    game_state = state["state"]
    opts = state.get("options") or []

    if game_state == "combat":
        p = state["player"]
        hp_cur, hp_max = (int(x) for x in p["hp"].split("/"))
        mp_cur, _ = (int(x) for x in p["mp"].split("/"))
        num_opts = len(opts)

        # Low HP → use item
        if hp_cur / max(hp_max, 1) < 0.35 and num_opts >= 3:
            return str(num_opts - 1)  # item slot

        # Have MP → cast first spell
        if mp_cur >= 10 and num_opts > 3:
            return "2"

        return "1"  # Attack

    if game_state == "story":
        num_choices = max(1, len(opts))
        if story_strategy == "random":
            return str(random.randint(1, num_choices))
        if story_strategy == "kind":
            return "1"
        if story_strategy == "dark":
            return str(min(3, num_choices))
        if story_strategy == "pragmatic":
            return str(min(2, num_choices))
        return str(random.randint(1, num_choices))

    if game_state == "shop":
        p = state["player"]
        gold = p["gold"]
        # Buy cheapest equipment first, then leave
        best_idx = None
        best_price = gold + 1
        for i, opt in enumerate(opts, 1):
            if "leave" in opt.lower():
                continue
            m = re.search(r"\((\d+)g\)", opt)
            if m:
                price = int(m.group(1))
                if price <= gold and price < best_price:
                    best_price = price
                    best_idx = i
        return str(best_idx) if best_idx else "leave"

    return ""  # Continue/confirm all pauses and transitions


# ── Single game runner ─────────────────────────────────────────────────────────

def _run_one(args_tuple) -> dict:
    """Run one game. Designed for multiprocessing — no shared state."""
    player_class, player_name, story_strategy, seed, dragon_only = args_tuple

    # Each worker needs its own seed to avoid correlated results
    if seed is not None:
        random.seed(seed)

    # Import here so each process gets a fresh module state
    from game.engine import GameEngine

    engine = GameEngine()
    state = engine.new_game(player_name, player_class)

    # Dragon-only mode: skip to floor 7 by advancing through floors quickly
    if dragon_only:
        while state["state"] not in ("game_over", "victory") and state["floor"] < 7:
            state = engine.action("1")  # Attack / pick first option to advance fast

    steps = 0
    errors = []

    while state["state"] not in ("game_over", "victory"):
        steps += 1
        if steps > 600:
            errors.append("step_limit_exceeded")
            break

        try:
            action = _bot_decide_from_state(state, story_strategy)
            state = engine.action(action)
        except Exception as e:
            errors.append(str(e))
            break

    p = state.get("player") or {}
    return {
        "class": player_class,
        "strategy": story_strategy,
        "outcome": state["state"],
        "floor_reached": state["floor"],
        "level": p.get("level", 0),
        "gold": p.get("gold", 0),
        "ending": _extract_ending(state),
        "steps": steps,
        "errors": errors,
    }


def _extract_ending(state: dict) -> str | None:
    """Extract ending name from victory messages."""
    if state["state"] != "victory":
        return None
    for msg in state.get("messages") or []:
        if "Ending:" in msg:
            return msg.replace("Ending:", "").strip()
    return "unknown"


# ── Simulation runner ──────────────────────────────────────────────────────────

_CLASS_NAMES = {"Warrior": "1", "Mage": "2", "Rogue": "3"}
_STRATEGIES = ["random", "kind", "pragmatic", "dark"]


def _build_run_args(n_runs: int, player_class: str | None,
                    strategy: str | None, dragon_only: bool) -> list:
    """Build the argument list for all runs."""
    classes = [player_class] if player_class else list(_CLASS_NAMES.keys())
    strategies = [strategy] if strategy else _STRATEGIES

    args = []
    per_combo = max(1, n_runs // (len(classes) * len(strategies)))

    for cls in classes:
        for strat in strategies:
            for i in range(per_combo):
                args.append((cls, f"Bot_{cls[:3]}_{strat[:3]}_{i}",
                             strat, None, dragon_only))

    # Pad to exactly n_runs if rounding left us short
    while len(args) < n_runs:
        cls = random.choice(classes)
        strat = random.choice(strategies)
        args.append((cls, "BotRand", strat, None, dragon_only))

    return args[:n_runs]


def run_simulation(n_runs: int, player_class: str | None, strategy: str | None,
                   dragon_only: bool, workers: int | None) -> dict:
    """Run all simulations and return aggregated results."""
    n_workers = workers or min(cpu_count(), 4)
    run_args = _build_run_args(n_runs, player_class, strategy, dragon_only)

    mode = "dragon-only" if dragon_only else "full run"
    print(f"\nRunning {len(run_args)} simulations  |  mode: {mode}  |  workers: {n_workers}\n")

    with Pool(n_workers) as pool:
        results = []
        for i, result in enumerate(pool.imap_unordered(_run_one, run_args), 1):
            results.append(result)
            if i % max(1, len(run_args) // 20) == 0 or i == len(run_args):
                pct = i / len(run_args) * 100
                wins = sum(1 for r in results if r["outcome"] == "victory")
                print(f"  {pct:5.1f}%  ({i}/{len(run_args)})  victories so far: {wins}/{i}")

    return _aggregate(results)


def _aggregate(results: list) -> dict:
    total = len(results)
    victories = [r for r in results if r["outcome"] == "victory"]
    deaths = [r for r in results if r["outcome"] == "dead"]
    errors = [r for r in results if r["errors"]]

    # Per-class stats
    class_stats = {}
    for cls in _CLASS_NAMES:
        cls_runs = [r for r in results if r["class"] == cls]
        if cls_runs:
            cls_wins = sum(1 for r in cls_runs if r["outcome"] == "victory")
            floors = [r["floor_reached"] for r in cls_runs]
            class_stats[cls] = {
                "runs": len(cls_runs),
                "wins": cls_wins,
                "win_rate": round(cls_wins / len(cls_runs), 3),
                "avg_floor": round(sum(floors) / len(floors), 2),
                "avg_level": round(sum(r["level"] for r in cls_runs) / len(cls_runs), 2),
            }

    # Ending distribution
    ending_counts: dict[str, int] = {}
    for r in victories:
        e = r.get("ending") or "unknown"
        ending_counts[e] = ending_counts.get(e, 0) + 1

    # Floor death distribution
    floor_deaths: dict[int, int] = {}
    for r in deaths:
        f = r["floor_reached"]
        floor_deaths[f] = floor_deaths.get(f, 0) + 1

    return {
        "timestamp": datetime.now().isoformat(),
        "total_runs": total,
        "victories": len(victories),
        "deaths": len(deaths),
        "errors": len(errors),
        "win_rate": round(len(victories) / max(total, 1), 3),
        "avg_steps": round(sum(r["steps"] for r in results) / max(total, 1), 1),
        "class_stats": class_stats,
        "ending_distribution": dict(sorted(ending_counts.items(),
                                           key=lambda x: -x[1])),
        "floor_death_distribution": {str(k): v for k, v
                                     in sorted(floor_deaths.items())},
        "error_messages": list({e for r in errors for e in r["errors"]})[:20],
        "runs": results,
    }


# ── Baseline comparison ────────────────────────────────────────────────────────

def _check_baseline(current: dict):
    """Compare current results against saved baseline."""
    baseline_path = os.path.normpath(BASELINE_PATH)
    if not os.path.exists(baseline_path):
        print(f"  No baseline found at {baseline_path}. Run --save-baseline first.")
        return

    with open(baseline_path) as f:
        baseline = json.load(f)

    print("\n── Baseline Comparison ──")
    b_wr = baseline.get("win_rate", 0)
    c_wr = current.get("win_rate", 0)
    delta = c_wr - b_wr
    flag = " ⚠️" if abs(delta) > 0.05 else " ✓"
    print(f"  Win rate:  baseline={b_wr:.1%}  current={c_wr:.1%}  delta={delta:+.1%}{flag}")

    for cls, stats in current.get("class_stats", {}).items():
        b_cls = baseline.get("class_stats", {}).get(cls, {})
        b_wr_cls = b_cls.get("win_rate", 0)
        c_wr_cls = stats.get("win_rate", 0)
        d = c_wr_cls - b_wr_cls
        flag = " ⚠️" if abs(d) > 0.08 else " ✓"
        print(f"  {cls:8s}: baseline={b_wr_cls:.1%}  current={c_wr_cls:.1%}  delta={d:+.1%}{flag}")


def _save_baseline(results: dict):
    baseline_path = os.path.normpath(BASELINE_PATH)
    os.makedirs(os.path.dirname(baseline_path), exist_ok=True)
    # Save only the summary, not all individual runs
    summary = {k: v for k, v in results.items() if k != "runs"}
    with open(baseline_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Baseline saved → {baseline_path}")


# ── MD report ──────────────────────────────────────────────────────────────────

def _write_md_report(results: dict, path: str, player_class: str | None,
                     strategy: str | None, mode: str):
    wr = results["win_rate"]
    lines = [
        f"# Simulation Report",
        "",
        f"**Date:** {results['timestamp'][:10]}  ",
        f"**Mode:** {mode}  ",
        f"**Class filter:** {player_class or 'all'}  ",
        f"**Strategy filter:** {strategy or 'all'}  ",
        f"**Total runs:** {results['total_runs']}  ",
        f"**Win rate:** {wr:.1%}  ",
        f"**Victories:** {results['victories']}  Deaths: {results['deaths']}  Errors: {results['errors']}",
        "",
        "## Per-Class Stats",
        "",
        "| Class | Wins | Runs | Win Rate | Avg Floor | Avg Level |",
        "|-------|------|------|----------|-----------|-----------|",
    ]
    for cls, s in results["class_stats"].items():
        lines.append(
            f"| {cls} | {s['wins']} | {s['runs']} | {s['win_rate']:.0%} "
            f"| {s['avg_floor']} | {s['avg_level']} |"
        )

    lines += ["", "## Ending Distribution", ""]
    for ending, count in results["ending_distribution"].items():
        pct = count / max(results["victories"], 1) * 100
        lines.append(f"- **{ending}**: {count} ({pct:.0f}% of victories)")

    lines += ["", "## Deaths by Floor", ""]
    for floor, count in results["floor_death_distribution"].items():
        lines.append(f"- Floor {floor}: {count} deaths")

    if results.get("error_messages"):
        lines += ["", "## Errors", ""]
        for e in results["error_messages"]:
            lines.append(f"- `{e}`")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fast Simulator for Dungeon Quest")
    parser.add_argument("--runs", type=int, default=50)
    parser.add_argument("--class", dest="player_class", default=None,
                        choices=["Warrior", "Mage", "Rogue"])
    parser.add_argument("--strategy", default=None,
                        choices=["random", "kind", "pragmatic", "dark"])
    parser.add_argument("--mode", default="full", choices=["full", "dragon"],
                        help="'full' = complete dungeon run, 'dragon' = Dragon fight only")
    parser.add_argument("--workers", type=int, default=None,
                        help="Parallel workers (default: min(cpu_count, 4))")
    parser.add_argument("--baseline", action="store_true",
                        help="Compare results against saved baseline")
    parser.add_argument("--save-baseline", action="store_true",
                        help="Save current results as new baseline")
    args = parser.parse_args()

    dragon_only = args.mode == "dragon"
    results = run_simulation(
        n_runs=args.runs,
        player_class=args.player_class,
        strategy=args.strategy,
        dragon_only=dragon_only,
        workers=args.workers,
    )

    # ── Print summary ──────────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"  RESULTS  |  {results['total_runs']} runs  |  "
          f"win rate: {results['win_rate']:.1%}")
    print(f"  Victories: {results['victories']}  Deaths: {results['deaths']}  "
          f"Errors: {results['errors']}")
    print(f"\n  Per class:")
    for cls, s in results["class_stats"].items():
        print(f"    {cls:8s}  {s['wins']}/{s['runs']}  ({s['win_rate']:.0%})  "
              f"avg floor {s['avg_floor']}  avg lv {s['avg_level']}")
    print(f"\n  Endings: {results['ending_distribution']}")
    print(f"  Deaths by floor: {results['floor_death_distribution']}")

    if results["error_messages"]:
        print(f"\n  ⚠️  Errors encountered: {results['error_messages']}")

    if args.baseline:
        _check_baseline(results)

    if args.save_baseline:
        _save_baseline(results)

    # ── Save logs ──────────────────────────────────────────────────────────────
    os.makedirs(LOGS_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    wr_pct = int(results["win_rate"] * 100)
    strat_tag = args.strategy or "allstrats"
    cls_tag = args.player_class.lower() if args.player_class else "allclasses"
    mode_tag = "dragon" if dragon_only else "full"
    stem = f"sim_{mode_tag}_{cls_tag}_{strat_tag}_{args.runs}runs_{wr_pct}pct_{ts}"

    json_path = os.path.join(LOGS_DIR, stem + ".json")
    md_path = os.path.join(LOGS_DIR, stem + ".md")

    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    _write_md_report(results, md_path, args.player_class, args.strategy,
                     "dragon-only" if dragon_only else "full run")
    print(f"\n  JSON → {json_path}")
    print(f"  MD   → {md_path}")


if __name__ == "__main__":
    main()
