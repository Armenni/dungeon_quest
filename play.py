#!/usr/bin/env python3
"""
AI bot that plays a full run via the API.
Usage: python play.py
"""
import requests, json, time, random, sys

BASE = "http://127.0.0.1:5000"
DIVIDER = "─" * 60

# Story choices aimed at: True Hero ending
# Event 1 (prisoner):  1 = spare him
# Event 2 (survivors): 1 = aid them
# Event 3 (sage):      1 = refuse dark pact
# Event 4 (tome):      3 = seal the tome (kept_secrets → helps scholar_king too)
STORY_CHOICES = ["1", "1", "1", "3"]
_story_idx = 0

# Shop budget: buy one piece of armour first, then potions
BOUGHT = {"armor": False, "weapon": False}


def post(path, body):
    r = requests.post(f"{BASE}{path}", json=body, timeout=10)
    return r.json()


def get(path):
    r = requests.get(f"{BASE}{path}", timeout=10)
    return r.json()


def show(data):
    print()
    # messages
    for m in data.get("messages", []):
        print(f"  {m}")
    # combat log
    for m in data.get("combat_log", []):
        print(f"    » {m}")
    # player status bar
    p = data.get("player")
    if p:
        statuses = f"  [{', '.join(p['statuses'])}]" if p['statuses'] else ""
        flags    = f"  flags: {p['flags']}" if p['flags'] else ""
        print(f"\n  [{p['name']} Lv{p['level']} | HP {p['hp']} | MP {p['mp']} | "
              f"ATK {p['atk']} DEF {p['defense']} MAG {p['magic']} | "
              f"Gold {p['gold']}g | {p['weapon'] or 'no weapon'} / {p['armor'] or 'no armor'}"
              f"{statuses}]{flags}")
    # enemy
    e = data.get("enemy")
    if e:
        est = f"  [{', '.join(e['statuses'])}]" if e['statuses'] else ""
        print(f"  [{e['name']} | HP {e['hp']} | ATK {e['atk']}{est}]")
    # state
    print(f"\n  State: {data['state']}  |  Floor: {data['floor']}")
    print(DIVIDER)


def decide(data) -> str:
    global _story_idx
    state   = data["state"]
    options = data["options"]
    p       = data.get("player", {})

    if state == "combat":
        hp_str  = p.get("hp", "1/1")
        hp, mhp = (int(x) for x in hp_str.split("/"))
        mp_str  = p.get("mp", "0/0")
        mp, _   = (int(x) for x in mp_str.split("/"))
        inv     = p.get("inventory", [])
        pclass  = p.get("class", "Warrior")

        # Use a potion if below 35% HP and we have one
        if hp / mhp < 0.35 and any("Potion" in i or "Elixir" in i for i in inv):
            idx = next(i for i, item in enumerate(inv)
                       if "Potion" in item or "Elixir" in item)
            item_slot = 2 + len([o for o in options if o.startswith("2:") or
                                  (o[0].isdigit() and ":" in o and
                                   not o.startswith("1:") and
                                   not o.startswith(str(2 + {"Warrior":1,"Mage":2,"Rogue":1}.get(pclass,1) + 1) + ":"))]) + 1
            # find item option number
            for opt in options:
                if "Use Item" in opt:
                    num = int(opt.split(":")[0])
                    choice = f"{num}:{idx+1}"
                    print(f"\n  [BOT] Low HP ({hp}/{mhp}) — using item: {choice}")
                    return choice

        # Use spell if available and MP is sufficient
        spells = {"Warrior": ("Battlecry", 10), "Mage": ("Fireball", 15), "Rogue": ("Backstab", 12)}
        spell_name, spell_cost = spells.get(pclass, ("", 99))
        if spell_name and mp >= spell_cost:
            # Find the spell option number
            for opt in options:
                if spell_name in opt:
                    num = int(opt.split(":")[0])
                    print(f"\n  [BOT] Casting {spell_name}  (choice {num})")
                    return str(num)

        print(f"\n  [BOT] Attacking (choice 1)")
        return "1"

    elif state == "story":
        choice = STORY_CHOICES[_story_idx] if _story_idx < len(STORY_CHOICES) else "1"
        print(f"\n  [BOT] Story choice {choice}: {options[int(choice)-1]}")
        _story_idx += 1
        return choice

    elif state == "shop":
        gold = p.get("gold", 0)
        # Try to buy armour first (best value), then a potion if cheap
        for i, opt in enumerate(options, 1):
            if opt.startswith("leave"):
                continue
            price_part = opt.split("(")[-1].rstrip("g)")
            try:
                price = int(price_part)
            except ValueError:
                continue

            if "[armor]" in opt and not BOUGHT["armor"] and gold >= price:
                print(f"\n  [BOT] Buying armor: {opt}")
                BOUGHT["armor"] = True
                return str(i)

        for i, opt in enumerate(options, 1):
            if opt.startswith("leave"):
                continue
            if "Health Potion" in opt:
                price_part = opt.split("(")[-1].rstrip("g)")
                try:
                    price = int(price_part)
                except ValueError:
                    continue
                if gold >= price:
                    print(f"\n  [BOT] Buying potion: {opt}")
                    return str(i)

        print(f"\n  [BOT] Leaving shop")
        return "leave"

    return "1"


def main():
    print(DIVIDER)
    print("  DUNGEON QUEST — Full Playthrough Bot")
    print(DIVIDER)

    # Start game
    data = post("/new_game", {"name": "Aric", "class": "Mage"})
    show(data)

    turn = 0
    while data.get("state") not in ("game_over", "victory"):
        turn += 1
        if turn > 300:
            print("  [BOT] Turn limit reached — stopping.")
            break

        choice = decide(data)
        time.sleep(0.05)   # small pause so output is readable
        data = post("/action", {"input": choice})
        show(data)

    state = data.get("state")
    print()
    if state == "victory":
        print("  ★★★  VICTORY — playthrough complete  ★★★")
    elif state == "game_over":
        print("  ✗  GAME OVER")
    else:
        print("  Stopped.")


if __name__ == "__main__":
    main()
