#!/usr/bin/env python3
"""
Automated playtest — patches Console.input to drive a full run.
Story choices aimed at: spared_prisoner + ignored_village + refused_dark_pact + deciphered_tome
Expected ending: The True Hero
"""
import sys, os, random

random.seed(42)

# ── Patch Console before any game imports ─────────────────────────────────────
from rich.console import Console
from rich.text import Text

STORY_CHOICES = ["1", "2", "1", "1"]   # per event: spared, ignored, refused, deciphered
_story_idx    = [0]
_use_item_hp  = [False]                 # flip to True when we want to use a potion

def _plain(markup) -> str:
    try:
        return Text.from_markup(str(markup)).plain.lower()
    except Exception:
        return str(markup).lower()

def auto_input(self, prompt="", **kwargs) -> str:
    p = _plain(prompt)

    if "name" in p:
        r = "Aric"
    elif "1, 2, or 3" in p:
        r = "2"                         # Mage
    elif "your choice" in p:
        i = _story_idx[0]; _story_idx[0] += 1
        r = STORY_CHOICES[i] if i < len(STORY_CHOICES) else "1"
    elif "action" in p:
        r = "1"                         # always attack
    elif "buy" in p or "leave" in p:
        r = "l"                         # leave shop immediately
    elif "use item" in p:
        r = "0"                         # cancel
    else:
        r = ""                          # press enter on all pauses

    # Echo the bot's decision so we can follow along
    label = p.strip()[:45].replace("\n", " ")
    print(f"  [BOT] {label!r:47s} → {r!r}", flush=True)
    return r

def auto_clear(self):
    # Replace clear() with a divider so output is readable in one scroll
    print("\n" + "━" * 70, flush=True)

Console.input = auto_input
Console.clear  = auto_clear

# ── Run the game ──────────────────────────────────────────────────────────────
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")

import main as game_main
game_main.main()
