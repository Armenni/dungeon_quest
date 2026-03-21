"""
simulate.py — Headless Dungeon Quest batch simulator
Patches all I/O, runs N games with varied strategies, logs to gameplay_log.json

Usage:  python simulate.py
"""
import json
import re
import random
import sys
import builtins
from datetime import datetime

# ── Bot ───────────────────────────────────────────────────────────────────────

class Bot:
    """
    Stateless decision bot. Strategy controls class + story choices.
    Strategies: warrior_merciful, warrior_dark, mage_scholar, rogue_random, etc.
    """
    def __init__(self, cls: str = "1", story_pick: str = "random", name: str = "Bot"):
        self.cls        = cls           # "1"=Warrior "2"=Mage "3"=Rogue
        self.story_pick = story_pick    # "1","2","3" or "random"
        self.name       = name
        self.decisions  = []
        self.events     = []

    def decide(self, prompt: str) -> str:
        p = prompt.strip()
        r = self._pick(p)
        self.decisions.append({"prompt": p[:120], "response": r})
        return r

    def _pick(self, p: str) -> str:
        pl = p.lower()

        # language
        if "selecione" in pl or "select language" in pl:
            return "1"
        # name
        if "name" in pl or "nome" in pl:
            return self.name
        # class
        if "1, 2, or 3" in pl or "1, 2 ou 3" in pl:
            return self.cls
        # combat action  e.g. "Action (1-4): "
        if "action" in pl:
            m = re.search(r"1-(\d+)", p)
            top = int(m.group(1)) if m else 4
            spell_top = top - 2   # last two are Items and Run
            # prefer spells when available (index 2); fall back to attack
            if spell_top >= 1:
                return "2"
            return "1"
        # use item (always use first item if prompted)
        if "use item" in pl:
            return "1"
        # inventory cancel
        if "cancel" in pl:
            return "0"
        # story choice
        if "choice" in pl or "escolha" in pl:
            m = re.search(r"1-(\d+)", p)
            top = int(m.group(1)) if m else 3
            if self.story_pick == "random":
                return str(random.randint(1, top))
            return self.story_pick if int(self.story_pick) <= top else "1"
        # shop: always leave
        if "buy" in pl or "comprar" in pl:
            return "l"
        # default: enter / pick 1
        return ""

    def log_event(self, msg: str):
        self.events.append(msg)


# ── I/O patches ───────────────────────────────────────────────────────────────

_ACTIVE_BOT: Bot = None
_ACTIVE_RUN: dict = None


def _install_patches():
    """Monkey-patch builtins.input and Rich Console before game import."""
    builtins.input = lambda prompt="": _ACTIVE_BOT.decide(str(prompt))

    from rich.console import Console

    def _fake_input(self, prompt="", **kw):
        return _ACTIVE_BOT.decide(str(prompt))

    def _fake_print(self, *args, **kw):
        msg = " ".join(str(a) for a in args)
        if _ACTIVE_RUN is not None and msg.strip():
            _ACTIVE_RUN["log"].append(msg[:300])

    def _fake_clear(self):
        pass

    Console.input = _fake_input
    Console.print  = _fake_print
    Console.clear  = _fake_clear


_install_patches()

# ── Game import (after patches) ───────────────────────────────────────────────

from game.i18n import set_language, t
from game.ui import UI
from game.player import Player
from game.dungeon import Dungeon


# ── Runner ────────────────────────────────────────────────────────────────────

def run_game(bot: Bot) -> dict:
    global _ACTIVE_BOT, _ACTIVE_RUN

    _ACTIVE_BOT = bot
    _ACTIVE_RUN = {
        "bot":      bot.name,
        "strategy": {"cls": bot.cls, "story": bot.story_pick},
        "log":      [],
        "outcome":  None,
        "ending":   None,
        "floor_reached": 0,
        "final_level":   0,
        "final_gold":    0,
        "decisions": bot.decisions,
    }
    bot.decisions = []

    set_language("en")

    ui     = UI()
    name   = bot.name
    cls_map = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    pcls   = cls_map.get(bot.cls, "Warrior")

    player = Player(name, pcls)

    # Patch Dungeon to track floor progress
    dungeon = Dungeon(player, ui)
    orig_floor_run = dungeon.run

    def tracked_run():
        orig_floor_run()
        _ACTIVE_RUN["floor_reached"] = dungeon.floor
        _ACTIVE_RUN["final_level"]   = player.level
        _ACTIVE_RUN["final_gold"]    = player.gold
        if player.active_ending:
            _ACTIVE_RUN["ending"] = t(player.active_ending.get("title", "?"))
        # outcome: check last log line for clues
        log_joined = " ".join(_ACTIVE_RUN["log"]).lower()
        if "game over" in log_joined or "fallen" in log_joined:
            _ACTIVE_RUN["outcome"] = "dead"
        else:
            _ACTIVE_RUN["outcome"] = "victory"

    dungeon.run = tracked_run
    dungeon.run()

    _ACTIVE_RUN["decisions"] = bot.decisions[:]
    return _ACTIVE_RUN


# ── Strategies ────────────────────────────────────────────────────────────────

STRATEGIES = [
    # (cls, story_pick, name)
    ("1", "1", "Warrior_Merciful"),    # warrior, always choice 1 (kind path)
    ("1", "2", "Warrior_Pragmatic"),   # warrior, always choice 2
    ("1", "3", "Warrior_Dark"),        # warrior, always choice 3 (dark path)
    ("2", "1", "Mage_Merciful"),
    ("2", "random", "Mage_Random"),
    ("3", "1", "Rogue_Merciful"),
    ("3", "3", "Rogue_Dark"),
    ("3", "random", "Rogue_Random"),
]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    results = []
    print(f"Running {len(STRATEGIES)} simulations...\n")

    for cls, story, name in STRATEGIES:
        bot = Bot(cls=cls, story_pick=story, name=name)
        run = run_game(bot)
        results.append(run)
        outcome_icon = "✓" if run["outcome"] == "victory" else "✗"
        print(f"  {outcome_icon} {name:<22} "
              f"floor={run['floor_reached']}  "
              f"lvl={run['final_level']}  "
              f"gold={run['final_gold']}  "
              f"ending={run['ending'] or 'N/A'}")

    # Save full log
    out = {
        "timestamp": datetime.now().isoformat(),
        "runs": results,
        "summary": {
            "total":    len(results),
            "victories": sum(1 for r in results if r["outcome"] == "victory"),
            "deaths":    sum(1 for r in results if r["outcome"] == "dead"),
            "endings":   {},
            "class_winrates": {},
        }
    }

    cls_names = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    cls_wins  = {"1": [0, 0], "2": [0, 0], "3": [0, 0]}
    for r in results:
        c = r["strategy"]["cls"]
        cls_wins[c][1] += 1
        if r["outcome"] == "victory":
            cls_wins[c][0] += 1
        e = r["ending"]
        if e:
            out["summary"]["endings"][e] = out["summary"]["endings"].get(e, 0) + 1

    for c, (wins, total) in cls_wins.items():
        if total:
            out["summary"]["class_winrates"][cls_names[c]] = f"{wins}/{total}"

    path = "gameplay_log.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nFull log saved to {path}")
    print(f"Victories: {out['summary']['victories']}/{out['summary']['total']}")
    print(f"Class win-rates: {out['summary']['class_winrates']}")
    print(f"Endings seen: {out['summary']['endings']}")


if __name__ == "__main__":
    main()
