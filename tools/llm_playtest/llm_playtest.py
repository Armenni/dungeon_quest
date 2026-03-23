#!/usr/bin/env python3
"""
LLM Playtester — plays Dungeon Quest step by step using Claude as the decision maker.

At each game state, Claude:
  1. Chooses an action (with reasoning)
  2. Notes UX issues — anything confusing or unclear
  3. Flags possible bugs or logic errors
  4. Suggests missing features for that specific moment

Usage:
    python tools/llm_playtest/llm_playtest.py
    python tools/llm_playtest/llm_playtest.py --class Mage --name Aria
    python tools/llm_playtest/llm_playtest.py --seed 42
    python tools/llm_playtest/llm_playtest.py --dry-run        # use simple bot, no Claude calls

Output:
    - Live step-by-step display in terminal
    - tools/llm_playtest/logs/playtest_{class}_{outcome}_floor{N}_{timestamp}.json
    - tools/llm_playtest/logs/playtest_{class}_{outcome}_floor{N}_{timestamp}.md
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

# Force UTF-8 output on Windows (game engine uses Unicode chars like ★)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from game.engine import GameEngine

LOGS_DIR = os.path.join(os.path.dirname(__file__), "logs")


# ── Prompt ─────────────────────────────────────────────────────────────────────

_SYSTEM = (
    "You are an experienced RPG specialist playtesting Dungeon Quest.\n"
    "Your job: play to win AND deliver honest, insight-driven feedback.\n\n"
    "Intellectual honesty rules:\n"
    "- Say exactly why something is confusing, broken, or missing — be specific\n"
    "- Don't soften feedback; directness is the only useful currency\n"
    "- Never generate filler observations to fill a list — empty [] is better than noise\n"
    "- Push on real issues; don't accept mechanics at face value if they feel off\n"
    "- Balance positives and negatives only when both are genuinely warranted\n\n"
    "Play strategy: items when HP<35%, spells when MP available, gear over potions early.\n\n"
    "Reply ONLY with JSON (no markdown):\n"
    '{"action":"<number or leave>","reasoning":"<honest 1-2 sentences: why this choice, '
    'any strategic concern>","ux_notes":["..."],"bug_suspects":["..."],"missing_features":["..."]}\n'
    "Max 2 items per list. Omit list entries entirely if nothing genuinely notable."
)


def _format_state(state: dict) -> str:
    """Compact single-block state for Claude — minimises input tokens."""
    s = state["state"]
    parts = [f"Floor {state['floor']} | {s.upper()}"]

    p = state.get("player")
    if p:
        inv = ", ".join(p["inventory"]) or "none"
        eq  = f"{p['weapon'] or '-'}/{p['armor'] or '-'}"
        st  = ", ".join(p["statuses"]) or "none"
        fl  = ", ".join(p["flags"]) or "none"
        parts.append(
            f"Player: {p['name']} {p['class']} Lv{p['level']} | "
            f"HP:{p['hp']} MP:{p['mp']} | ATK:{p['atk']} DEF:{p['defense']} MAG:{p['magic']} | "
            f"Gold:{p['gold']}g | Equip:{eq} | Inv:[{inv}] | Status:{st} | Flags:{fl}"
        )

    e = state.get("enemy")
    if e:
        est = ", ".join(e["statuses"]) or "none"
        parts.append(f"Enemy: {e['name']} HP:{e['hp']} ATK:{e['atk']} Status:{est}")

    # Only show combat_log in combat state — it's stale in shop/story
    events: list[str] = []
    if s == "combat":
        events = [m for m in (state.get("combat_log") or [])[-4:] if m.strip()]
    events += [m for m in (state.get("messages") or [])[-3:] if m.strip()]
    if events:
        parts.append("Events: " + " | ".join(events))

    opts = state.get("options") or []
    if opts:
        parts.append("Options: " + " | ".join(opts))

    return "\n".join(parts)


# ── Claude call ────────────────────────────────────────────────────────────────

def _ask_claude(state: dict) -> dict:
    """Call Claude CLI and parse JSON response. Falls back to attack on failure."""
    prompt = _SYSTEM + "\n\n" + _format_state(state)
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "claude-haiku-4-5-20251001"],
            capture_output=True, text=True, timeout=90,
        )
        raw = result.stdout.strip()
        if not raw and result.stderr.strip():
            return _fallback(f"Claude stderr: {result.stderr.strip()[:120]}")
        # Strip markdown code fences if present
        m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
        if m:
            raw = m.group(1)
        # Find first JSON object
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if m:
            raw = m.group(0)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        return _fallback(f"JSON parse error: {e}")
    except subprocess.TimeoutExpired:
        return _fallback("Claude timed out")
    except FileNotFoundError:
        return _fallback("'claude' CLI not found — run with --dry-run")


def _fallback(reason: str) -> dict:
    print(f"  [WARN] {reason}. Using fallback action.")
    return {"action": "1", "reasoning": reason,
            "ux_notes": [], "bug_suspects": [], "missing_features": []}


# ── Dry-run bot ────────────────────────────────────────────────────────────────

def _bot_decide(state: dict) -> dict:
    """Simple deterministic bot for --dry-run (no LLM calls)."""
    import random
    game_state = state["state"]
    opts = state.get("options") or []

    if game_state == "combat":
        p = state["player"]
        hp_cur, hp_max = (int(x) for x in p["hp"].split("/"))
        mp_cur, _ = (int(x) for x in p["mp"].split("/"))
        num_opts = len(opts)
        if hp_cur / max(hp_max, 1) < 0.35 and num_opts >= 3:
            return {"action": str(num_opts - 1), "reasoning": "Low HP — use item",
                    "ux_notes": [], "bug_suspects": [], "missing_features": []}
        if mp_cur >= 10 and num_opts > 3:
            return {"action": "2", "reasoning": "Have MP — cast first spell",
                    "ux_notes": [], "bug_suspects": [], "missing_features": []}
        return {"action": "1", "reasoning": "Attack",
                "ux_notes": [], "bug_suspects": [], "missing_features": []}

    if game_state == "story":
        return {"action": str(random.randint(1, max(1, len(opts)))),
                "reasoning": "Random story choice",
                "ux_notes": [], "bug_suspects": [], "missing_features": []}

    if game_state == "shop":
        p = state["player"]
        gold = p["gold"]
        # Prefer armor, then weapon, then potions — buy first affordable upgrade
        for slot_kw in ("[armor]", "[weapon]", "Potion"):
            for i, opt in enumerate(opts, 1):
                if "leave" in opt.lower():
                    continue
                m = re.search(r"\((\d+)g\)", opt)
                if m and int(m.group(1)) <= gold and slot_kw.lower() in opt.lower():
                    return {"action": str(i), "reasoning": f"Buy {slot_kw}",
                            "ux_notes": [], "bug_suspects": [], "missing_features": []}
        return {"action": "leave", "reasoning": "Nothing affordable / leave shop",
                "ux_notes": [], "bug_suspects": [], "missing_features": []}

    return {"action": "", "reasoning": "Continue",
            "ux_notes": [], "bug_suspects": [], "missing_features": []}


# ── MD report ──────────────────────────────────────────────────────────────────

def _write_md_report(report: dict, path: str):
    cfg = report["config"]
    summary = report["summary"]
    lines = [
        f"# Playtest Report — {cfg['name']} the {cfg['class']}",
        "",
        f"**Date:** {report['timestamp'][:10]}  ",
        f"**Outcome:** {report['outcome'].upper()}  ",
        f"**Floor reached:** {report['floor_reached']}  ",
        f"**Total steps:** {report['total_steps']}  ",
        f"**Mode:** {'dry-run (bot)' if cfg['dry_run'] else 'Claude LLM'}  ",
        f"**Seed:** {cfg['seed'] if cfg['seed'] is not None else 'random'}",
        "",
    ]

    if summary["ux_notes"]:
        lines += [f"## UX Notes ({len(summary['ux_notes'])})"]
        for n in summary["ux_notes"]:
            lines.append(f"- {n}")
        lines.append("")

    if summary["bug_suspects"]:
        lines += [f"## Bug Suspects ({len(summary['bug_suspects'])})"]
        for b in summary["bug_suspects"]:
            lines.append(f"- {b}")
        lines.append("")

    if summary["missing_features"]:
        lines += [f"## Missing Features ({len(summary['missing_features'])})"]
        for f in summary["missing_features"]:
            lines.append(f"- {f}")
        lines.append("")

    lines += ["## Step Log", ""]
    lines.append("| Step | Floor | State | Action | Reasoning |")
    lines.append("|------|-------|-------|--------|-----------|")
    for s in report["steps"]:
        reasoning = s["reasoning"].replace("|", "/")[:60]
        lines.append(f"| {s['step']} | {s['floor']} | {s['state']} | `{s['action']}` | {reasoning} |")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ── Main runner ────────────────────────────────────────────────────────────────

def run_playtest(player_class: str, name: str, seed: int | None,
                 dry_run: bool) -> dict:
    import random as _random
    if seed is not None:
        _random.seed(seed)

    engine = GameEngine()
    state = engine.new_game(name, player_class)

    steps = []
    all_ux: list[str] = []
    all_bugs: list[str] = []
    all_missing: list[str] = []

    mode = "dry-run (bot)" if dry_run else "Claude"
    print(f"\n{'='*62}")
    print(f"  LLM PLAYTESTER  |  {name} the {player_class}  |  mode: {mode}")
    print(f"{'='*62}\n")

    step = 0
    while state["state"] not in ("game_over", "victory"):
        step += 1

        # -- Display current state ---------------------------------------------
        print(f"-- Step {step:3d}  |  Floor {state['floor']}  |  {state['state'].upper()} --")
        for msg in (state.get("messages") or []):
            if msg.strip():
                print(f"  {msg}")
        for entry in (state.get("combat_log") or [])[-3:]:
            if entry.strip():
                print(f"  > {entry}")

        # ── Get decision ───────────────────────────────────────────────────────
        if dry_run:
            decision = _bot_decide(state)
        else:
            print("  [thinking...]")
            decision = _ask_claude(state)

        action = str(decision.get("action", "1")).strip() or "1"

        # ── Print decision ─────────────────────────────────────────────────────
        print(f"  -> {action!r:8s} | {decision.get('reasoning', '')}")
        for note in decision.get("ux_notes") or []:
            print(f"  [UX]   {note}")
        for bug in decision.get("bug_suspects") or []:
            print(f"  [BUG?] {bug}")
        for feat in decision.get("missing_features") or []:
            print(f"  [WISH] {feat}")
        print()

        all_ux.extend(decision.get("ux_notes") or [])
        all_bugs.extend(decision.get("bug_suspects") or [])
        all_missing.extend(decision.get("missing_features") or [])

        steps.append({
            "step": step,
            "floor": state["floor"],
            "state": state["state"],
            "action": action,
            "reasoning": decision.get("reasoning", ""),
            "ux_notes": decision.get("ux_notes") or [],
            "bug_suspects": decision.get("bug_suspects") or [],
            "missing_features": decision.get("missing_features") or [],
        })

        if step > 600:
            print("  [ABORT] Step limit reached — possible infinite loop!")
            break

        state = engine.action(action)

    # ── Final outcome ──────────────────────────────────────────────────────────
    outcome = state["state"]
    floor_reached = state["floor"]
    print(f"\n{'='*62}")
    print(f"  OUTCOME: {outcome.upper()}  |  {step} steps  |  Floor {floor_reached}")
    for msg in (state.get("messages") or []):
        if msg.strip():
            print(f"  {msg}")

    # ── Summary ────────────────────────────────────────────────────────────────
    deduped_ux = sorted(set(all_ux))
    deduped_bugs = sorted(set(all_bugs))
    deduped_missing = sorted(set(all_missing))

    print("\n-- PLAYTESTER REPORT --")
    if deduped_ux:
        print(f"\n  UX NOTES ({len(deduped_ux)}):")
        for n in deduped_ux:
            print(f"    * {n}")
    if deduped_bugs:
        print(f"\n  BUG SUSPECTS ({len(deduped_bugs)}):")
        for b in deduped_bugs:
            print(f"    * {b}")
    if deduped_missing:
        print(f"\n  MISSING FEATURES ({len(deduped_missing)}):")
        for f in deduped_missing:
            print(f"    * {f}")
    if not (deduped_ux or deduped_bugs or deduped_missing):
        print("  No issues noted.")

    # ── Build report ───────────────────────────────────────────────────────────
    report = {
        "timestamp": datetime.now().isoformat(),
        "config": {"name": name, "class": player_class, "seed": seed, "dry_run": dry_run},
        "outcome": outcome,
        "floor_reached": floor_reached,
        "total_steps": step,
        "steps": steps,
        "summary": {
            "ux_notes": deduped_ux,
            "bug_suspects": deduped_bugs,
            "missing_features": deduped_missing,
        },
    }

    # ── Save logs ──────────────────────────────────────────────────────────────
    os.makedirs(LOGS_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = f"playtest_{player_class.lower()}_{outcome}_floor{floor_reached}_{ts}"
    json_path = os.path.join(LOGS_DIR, stem + ".json")
    md_path = os.path.join(LOGS_DIR, stem + ".md")

    with open(json_path, "w") as f:
        json.dump(report, f, indent=2)
    _write_md_report(report, md_path)
    print(f"\n  JSON → {json_path}")
    print(f"  MD   → {md_path}")

    return report


def main():
    parser = argparse.ArgumentParser(description="LLM Playtester for Dungeon Quest")
    parser.add_argument("--class", dest="player_class", default="Mage",
                        choices=["Warrior", "Mage", "Rogue"])
    parser.add_argument("--name", default="Aria")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true",
                        help="Use simple bot instead of Claude (fast, no LLM calls)")
    args = parser.parse_args()

    run_playtest(args.player_class, args.name, args.seed, args.dry_run)


if __name__ == "__main__":
    main()
