"""
dragon_test.py — 3 runs per class vs the Dragon, detailed fight log
"""
import json, re, random, builtins
from datetime import datetime

# ── Bot ───────────────────────────────────────────────────────────────────────

class Bot:
    def __init__(self, cls: str, story: str, name: str):
        self.cls   = cls      # "1"=Warrior "2"=Mage "3"=Rogue
        self.story = story    # "1","2","3","random"
        self.name  = name
        self.player_ref = None   # set after Player is created

    def decide(self, prompt: str) -> str:
        p = prompt.strip()
        pl = p.lower()

        if "selecione" in pl or "select language" in pl: return "1"
        if "name" in pl or "nome" in pl:                 return self.name
        if "1, 2, or 3" in pl or "1, 2 ou 3" in pl:    return self.cls

        if "action" in pl:
            return self._combat(p)

        if "use item" in pl:
            # use first item
            return "1"

        if "choice" in pl or "escolha" in pl:
            m = re.search(r"1-(\d+)", p)
            top = int(m.group(1)) if m else 3
            if self.story == "random":
                return str(random.randint(1, top))
            return self.story if int(self.story) <= top else "1"

        if "buy" in pl or "comprar" in pl: return "l"
        return ""

    def _combat(self, prompt: str) -> str:
        m = re.search(r"1-(\d+)", prompt)
        top    = int(m.group(1)) if m else 4
        # top = run_num; top-1 = item slot; 2..top-2 = spells
        item_n = top - 1
        run_n  = top

        p = self.player_ref
        if p is None:
            return "1"

        hp_pct = p.hp / max(1, p.max_hp)

        # Use item if low HP and have items
        if hp_pct < 0.35 and p.inventory:
            return str(item_n)

        # Use spell if have MP (Warrior: Battlecry; Mage: Fireball; Rogue: Backstab)
        num_spells = top - 3   # item and run take the last 2 slots
        if num_spells >= 1 and p.mp >= 10:
            return "2"

        # Default: attack
        return "1"


# ── I/O patches ───────────────────────────────────────────────────────────────

_BOT: Bot     = None
_RUN: dict    = None

builtins.input = lambda prompt="": _BOT.decide(str(prompt))

from rich.console import Console as _C

def _inp(self, prompt="", **kw):  return _BOT.decide(str(prompt))
def _prn(self, *a, **kw):
    msg = " ".join(str(x) for x in a)
    if _RUN and msg.strip():
        _RUN["log"].append(msg[:300])
def _clr(self): pass

_C.input = _inp
_C.print = _prn
_C.clear = _clr

# ── Game imports (after patches) ──────────────────────────────────────────────

from game.i18n import set_language, t
from game.ui import UI
from game.player import Player
from game.dungeon import Dungeon
from game.enemy import make_boss_with_modifiers
from game.story import resolve_ending

# ── Intercept Dragon fight ────────────────────────────────────────────────────

def run_game(bot: Bot, seed: int) -> dict:
    global _BOT, _RUN
    random.seed(seed)
    _BOT = bot
    _RUN = {"log": [], "dragon": None}

    set_language("en")

    cls_map = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    player  = Player(bot.name, cls_map[bot.cls])
    bot.player_ref = player

    ui     = UI()
    dungeon = Dungeon(player, ui)

    # Patch _combat to intercept the Dragon fight
    _orig_combat = dungeon._combat

    def patched_combat(enemy, modifier):
        if enemy.name == "Dragon":
            result, fight_log = _dragon_fight(dungeon, player, enemy, modifier, ui)
            _RUN["dragon"] = fight_log
            return result
        return _orig_combat(enemy, modifier)

    dungeon._combat = patched_combat
    dungeon.run()

    # outcome — derive from dragon fight result (reliable) or floor reached
    d = _RUN["dragon"]
    if d is not None:
        outcome = "victory" if d["result"] == "dragon_defeated" else "dead"
    else:
        # Never reached Dragon → died on an earlier floor
        outcome = "dead"

    return {
        "name":    bot.name,
        "cls":     cls_map[bot.cls],
        "story":   bot.story,
        "seed":    seed,
        "outcome": outcome,
        "level":   player.level,
        "gold":    player.gold,
        "ending":  t(player.active_ending["title"]) if player.active_ending else None,
        "dragon":  d,
        "log":     _RUN["log"],
    }


def _dragon_fight(dungeon, player, enemy, modifier, ui) -> tuple:
    """Re-implements _combat with per-turn detailed logging for the Dragon."""
    from game.combat import (player_attack, player_magic, enemy_turn,
                             player_turn_start, enemy_turn_start, SPELLS)
    from game.status import consume_stun
    from game.items import ITEMS

    ui.clear_log()
    magic_mult  = modifier.get("player_magic_mult", 1.0)
    revive_used = False
    combat_turn = 0
    last_ability = ""
    turns_log   = []
    bot = _BOT

    while player.is_alive() and enemy.is_alive():
        turn = {"turn": combat_turn + 1,
                "player_hp": player.hp, "enemy_hp": enemy.hp,
                "player_mp": player.mp}

        # player DoT
        for msg, _ in player_turn_start(player):
            ui.add_log(msg)
        if not player.is_alive():
            break

        if consume_stun(player):
            ui.add_log(f"[yellow]{t('player_stunned')}[/yellow]")
            ui.show_combat(player, enemy)
            turn["action"] = "STUNNED"
        else:
            ui.show_combat(player, enemy)
            choice_str = ui.show_combat_menu(player)
            spells     = list(SPELLS.get(player.player_class, {}).keys())
            num_spells = len(spells)
            item_num   = 2 + num_spells
            run_num    = item_num + 1
            c = int(choice_str)

            if c == 1:
                dmg, crit = player_attack(player, enemy)
                crit_txt  = f" [bold yellow]{t('critical_hit')}[/bold yellow]" if crit else ""
                ui.add_log(f"[green]{t('player_attack', dmg=dmg)}{crit_txt}[/green]")
                turn["action"] = f"ATTACK dmg={dmg}" + (" CRIT" if crit else "")

            elif 2 <= c <= 1 + num_spells:
                spell_name = spells[c - 2]
                dmg, name, fx = player_magic(player, enemy, spell_name, magic_mult)
                if dmg == 0:
                    ui.add_log(f"[yellow]{fx}[/yellow]")
                    turn["action"] = f"SPELL {spell_name} FAILED ({fx})"
                else:
                    ui.add_log(f"[blue]{t('player_cast', name=name, dmg=dmg)}{fx}[/blue]")
                    turn["action"] = f"SPELL {spell_name} dmg={dmg}"

            elif c == item_num:
                idx = ui.show_inventory(player)
                if idx >= 0:
                    msg = player.use_item(idx)
                    ui.add_log(f"[green]{msg}[/green]")
                    turn["action"] = f"ITEM: {msg}"
                else:
                    # fallback to attack
                    dmg, crit = player_attack(player, enemy)
                    ui.add_log(f"[green]{t('player_attack', dmg=dmg)}[/green]")
                    turn["action"] = f"ATTACK(fb) dmg={dmg}"

            elif c == run_num:
                if random.random() < 0.5:
                    ui.add_log(f"[yellow]{t('fled')}[/yellow]")
                    ui.show_combat(player, enemy)
                    ui.pause()
                    return "run", {"turns": turns_log, "result": "fled"}
                else:
                    ui.add_log(f"[red]{t('escape_failed')}[/red]")
                    turn["action"] = "RUN_FAILED"

        # enemy DoT
        if not enemy.is_alive():
            break
        for msg, _ in enemy_turn_start(enemy):
            ui.add_log(msg)
        if not enemy.is_alive():
            break

        if consume_stun(enemy):
            ui.add_log(f"[yellow]{t('enemy_stunned', name=enemy.name)}[/yellow]")
            combat_turn += 1
            turn["enemy_action"] = "STUNNED"
        else:
            dmg, msg, ability = enemy_turn(enemy, player, combat_turn, last_ability)
            last_ability  = ability
            combat_turn  += 1
            turn["enemy_action"] = f"{ability} dmg={max(0,dmg)}"
            if dmg > 0:   ui.add_log(f"[red]{msg}[/red]")
            elif dmg < 0: ui.add_log(f"[italic dim]{msg}[/italic dim]")
            else:         ui.add_log(f"[dim]{msg}[/dim]")

        # ally damage modifier
        ally_dmg = modifier.get("ally_dmg_per_turn", 0)
        if ally_dmg and enemy.is_alive():
            enemy.hp = max(0, enemy.hp - ally_dmg)
            ui.add_log(f"[magenta]{t('dark_spirits', name=enemy.name, dmg=ally_dmg)}[/magenta]")
            turn["ally_dmg"] = ally_dmg

        # martyred saint revive
        if not player.is_alive() and modifier.get("revive_once") and not revive_used:
            revive_used = True
            modifier.pop("revive_once")
            player.hp = player.max_hp // 2
            ui.add_log(f"[bold cyan]{t('revive')}[/bold cyan]")
            turn["revived"] = True

        turns_log.append(turn)

    ui.show_combat(player, enemy)

    if not player.is_alive():
        turns_log.append({"result": "PLAYER_DIED",
                          "player_hp": 0, "enemy_hp": enemy.hp})
        return "dead", {"turns": turns_log, "result": "player_died",
                        "dragon_hp_left": enemy.hp,
                        "dragon_max_hp": enemy.max_hp}

    # victory
    leveled = player.gain_xp(enemy.xp)
    player.gold += enemy.gold
    ui.print(f"[bold green]{t('enemy_defeated', name=enemy.name)}[/bold green]")
    if leveled:
        ui.print(f"[bold yellow]{t('level_up', level=player.level)}[/bold yellow]")
    ui.pause()
    turns_log.append({"result": "DRAGON_DEFEATED",
                      "player_hp_left": player.hp,
                      "player_max_hp": player.max_hp})
    return "win", {"turns": turns_log, "result": "dragon_defeated",
                   "player_hp_left": player.hp,
                   "total_turns": len(turns_log)}


# ── Main ──────────────────────────────────────────────────────────────────────

RUNS_PER_CLASS = 20
STORIES = ["1", "2", "3", "random"]

def build_runs():
    runs = []
    cls_map = [("1", "Warrior"), ("2", "Mage"), ("3", "Rogue")]
    for cls, cls_name in cls_map:
        for i in range(RUNS_PER_CLASS):
            story = STORIES[i % len(STORIES)]
            runs.append((cls, story, f"{cls_name}_r{i+1:02d}"))
    return runs

def main():
    import sys
    class Tee:
        def __init__(self, *streams): self.streams = streams
        def write(self, data):
            for s in self.streams: s.write(data)
        def flush(self):
            for s in self.streams: s.flush()

    log_file = open("dragon_output.txt", "w")
    sys.stdout = Tee(sys.__stdout__, log_file)

    runs = build_runs()
    all_results = []
    cls_names = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    total = len(runs)
    print(f"Dragon Test — {RUNS_PER_CLASS} runs per class ({total} total)\n" + "─"*56)

    for i, (cls, story, name) in enumerate(runs):
        bot    = Bot(cls=cls, story=story, name=name)
        result = run_game(bot, seed=100 + i * 13)
        all_results.append(result)

        d = result["dragon"]
        if d is None:
            dragon_summary = "never reached Dragon (died earlier)"
        elif d["result"] == "player_died":
            pct = round(100 * d["dragon_hp_left"] / max(1, d["dragon_max_hp"]))
            dragon_summary = f"DIED  Dragon {d['dragon_hp_left']}/{d['dragon_max_hp']} HP ({pct}% left)"
        elif d["result"] == "dragon_defeated":
            dragon_summary = f"KILLED  player {d['player_hp_left']} HP left  {d['total_turns']} turns"
        else:
            dragon_summary = d["result"]

        icon = "✓" if result["outcome"] == "victory" else "✗"
        print(f"  {icon} {name:<16} lv={result['level']}  {dragon_summary}")

    # Per-class summary
    print("\n" + "─"*56)
    for c in ["1", "2", "3"]:
        group  = [r for r in all_results if r["cls"] == cls_names[c]]
        wins   = sum(1 for r in group if r["outcome"] == "victory")
        # avg Dragon HP% left on losses
        losses = [r for r in group if r["outcome"] == "dead" and r["dragon"] and r["dragon"]["result"] == "player_died"]
        avg_pct = 0
        if losses:
            avg_pct = round(sum(
                100 * r["dragon"]["dragon_hp_left"] / max(1, r["dragon"]["dragon_max_hp"])
                for r in losses
            ) / len(losses))
        no_reach = sum(1 for r in group if r["dragon"] is None)
        print(f"  {cls_names[c]:<8}: {wins}/{RUNS_PER_CLASS} wins  "
              f"| avg Dragon HP left on loss: {avg_pct}%  "
              f"| died before Dragon: {no_reach}")

    # Endings breakdown
    endings = {}
    for r in all_results:
        e = r["ending"] or "N/A"
        endings[e] = endings.get(e, 0) + 1
    print(f"\n  Endings: {endings}")

    total_wins = sum(1 for r in all_results if r["outcome"] == "victory")
    print(f"\n  Overall: {total_wins}/{total} wins  ({round(100*total_wins/total)}%)")

    with open("dragon_log.json", "w") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "runs": all_results}, f, indent=2)
    print("\nDetailed log → dragon_log.json")
    print("Output       → dragon_output.txt")
    log_file.close()
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
