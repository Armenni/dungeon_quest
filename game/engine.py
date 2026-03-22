"""
Game engine — pure state machine, no UI dependency.
The API talks to this; the TUI (dungeon.py) keeps working separately.
"""
import random
from typing import Optional
from game.player import Player
from game.enemy import get_random_enemy, make_boss_with_modifiers
from game.combat import player_attack, player_magic, enemy_turn, SPELLS
from game.status import consume_stun, tick_statuses
from game.items import ITEMS
from game.equipment import EQUIPMENT, SHOP_STOCK, POTION_SHOP
from game.story import get_event, resolve_ending, apply_effect
from game.i18n import set_language as _set_language, t
from game import i18n as _i18n_mod


class GameEngine:
    def __init__(self):
        self.state   = "idle"   # idle|combat|story|shop|game_over|victory
        self.player: Optional[Player] = None
        self.floor   = 1
        self.max_floors = 7
        self.enemy   = None

        self.messages:   list[str] = []   # narrative messages since last action
        self.combat_log: list[str] = []   # current combat round log

        self._floor_enemies: list = []    # remaining enemies this floor
        self._pending_story = None

        # shop
        self._shop_items: list = []       # (kind, key, price)

        # boss modifiers from story ending
        self._modifier:    dict  = {}
        self._magic_mult:  float = 1.0
        self._revive_used: bool  = False

        # per-combat tracking for boss AI
        self._combat_turn:      int = 0
        self._last_enemy_ability: str = ""

    # ── Public API ─────────────────────────────────────────────────────────────

    def new_game(self, name: str, player_class: str) -> dict:
        if not _i18n_mod._lang:
            _set_language("en")
        if player_class not in ("Warrior", "Mage", "Rogue"):
            return {"error": f"Unknown class '{player_class}'. Choose Warrior, Mage, or Rogue."}
        self.player = Player(name or "Hero", player_class)
        self.floor  = 1
        self.messages.clear()
        self.combat_log.clear()
        self.msg(f"Welcome, {self.player.name} the {self.player.player_class}!")
        self._start_floor()
        return self._response()

    def action(self, value: str) -> dict:
        self.messages.clear()
        v = value.strip()

        if self.state == "combat":
            self._combat_action(v)
        elif self.state == "story":
            self._story_action(v)
        elif self.state == "shop":
            self._shop_action(v)
        elif self.state in ("game_over", "victory"):
            self.msg("The game is over. Start a new game with POST /new_game.")
        else:
            self.msg(f"Unknown state: {self.state}")

        return self._response()

    # ── Floor management ───────────────────────────────────────────────────────

    def _start_floor(self):
        self.msg(f"=== Floor {self.floor} / {self.max_floors} ===")

        if self.floor == self.max_floors:
            self.player.active_ending = resolve_ending(self.player.story_flags)
            self._modifier    = dict(self.player.active_ending.get("dragon_modifier", {}))
            self._magic_mult  = self._modifier.get("player_magic_mult", 1.0)
            self._revive_used = False
            self._combat_turn = 0
            self._last_enemy_ability = ""
            bonus = self._modifier.get("bonus_msg", "")
            if bonus:
                self.msg(t(bonus))
            def_bonus = self._modifier.get("player_def_bonus", 0)
            if def_bonus:
                self.player.apply_bonus(defense=def_bonus)
            self.msg("The air grows heavy. Something ancient stirs...")
            self.enemy = make_boss_with_modifiers(self.floor, self._modifier)
            self.combat_log.clear()
            self.state = "combat"
            self.msg(f"The Dragon awakens! [HP {self.enemy.hp}/{self.enemy.max_hp}]")
        else:
            count = random.randint(2, 3)
            self._floor_enemies = [get_random_enemy(self.floor) for _ in range(count)]
            self._next_enemy()

    def _next_enemy(self):
        if not self._floor_enemies:
            self._floor_cleared()
            return
        self.enemy = self._floor_enemies.pop(0)
        self.combat_log.clear()
        self.state = "combat"
        self._combat_turn = 0
        self._last_enemy_ability = ""
        self.msg(f"A {self.enemy.name} appears! [HP {self.enemy.hp}  ATK {self.enemy.atk}]")

    def _floor_cleared(self):
        self.msg(f"Floor {self.floor} cleared!")
        event = get_event(self.floor)
        if event:
            self._pending_story = event
            self.state = "story"
            self.msg(f"\n[Story Event] {t(event.title)}")
            self.msg(t(event.narrative))
        else:
            self._open_shop()

    def _open_shop(self):
        stock = SHOP_STOCK.get(self.floor, SHOP_STOCK[1])
        self._shop_items = []
        for key, price in POTION_SHOP:
            self._shop_items.append(("item", key, price))
        for key in stock.get("weapons", []):
            self._shop_items.append(("equip", key, EQUIPMENT[key].price))
        for key in stock.get("armors", []):
            self._shop_items.append(("equip", key, EQUIPMENT[key].price))
        self.state = "shop"
        self.msg(f"A merchant appears. Your gold: {self.player.gold}g")

    # ── Combat ─────────────────────────────────────────────────────────────────

    def _combat_action(self, value: str):
        spells    = list(SPELLS.get(self.player.player_class, {}).keys())
        num_spells = len(spells)
        item_num   = 2 + num_spells
        run_num    = item_num + 1

        # Parse: "3" or "3:2" (use item 2)
        item_sub = None
        if ":" in value:
            parts    = value.split(":", 1)
            value    = parts[0]
            item_sub = parts[1]

        try:
            c = int(value)
        except ValueError:
            self.msg(f"Invalid action. Choose 1-{run_num}.")
            return
        if not (1 <= c <= run_num):
            self.msg(f"Choose 1-{run_num}.")
            return

        # ── Player turn: DoT tick ──────────────────────────────────────────────
        for msg, _ in tick_statuses(self.player):
            self.combat_log.append(msg)
        if not self.player.is_alive():
            self._handle_death()
            return

        # ── Player action ──────────────────────────────────────────────────────
        if consume_stun(self.player):
            self.combat_log.append("You are stunned — lose your turn!")
        else:
            if c == 1:
                dmg, crit = player_attack(self.player, self.enemy)
                suffix    = " CRITICAL HIT!" if crit else ""
                self.combat_log.append(f"You attack for {dmg} damage!{suffix}")

            elif 2 <= c <= 1 + num_spells:
                spell_name = spells[c - 2]
                dmg, name, fx = player_magic(self.player, self.enemy, spell_name, self._magic_mult)
                if dmg == 0:
                    self.combat_log.append(fx)
                else:
                    self.combat_log.append(f"You cast {name} for {dmg} damage!{fx}")

            elif c == item_num:
                inv = self.player.inventory
                if not inv:
                    self.combat_log.append("No items!")
                else:
                    idx = 0
                    if item_sub and item_sub.isdigit():
                        idx = max(0, min(int(item_sub) - 1, len(inv) - 1))
                    self.combat_log.append(self.player.use_item(idx))

            elif c == run_num:
                if random.random() < 0.5:
                    self.combat_log.append("You fled from battle!")
                    for line in self.combat_log:
                        self.msg(line)
                    self.combat_log.clear()
                    self._do_rest_event()
                    self._next_enemy()
                    return
                else:
                    self.combat_log.append("Failed to escape!")

        if not self.enemy.is_alive():
            self._victory_combat()
            return

        # ── Enemy turn: DoT tick ───────────────────────────────────────────────
        for msg, _ in tick_statuses(self.enemy):
            self.combat_log.append(msg)
        if not self.enemy.is_alive():
            self._victory_combat()
            return

        # ── Enemy action ───────────────────────────────────────────────────────
        if consume_stun(self.enemy):
            self.combat_log.append(f"{self.enemy.name} is stunned — loses its turn!")
            self._combat_turn += 1
        else:
            dmg, msg, ability = enemy_turn(
                self.enemy, self.player,
                self._combat_turn, self._last_enemy_ability)
            self._last_enemy_ability = ability
            self._combat_turn += 1
            self.combat_log.append(msg)

        # ── Story modifier: ally damage ────────────────────────────────────────
        ally = self._modifier.get("ally_dmg_per_turn", 0)
        if ally and self.enemy.is_alive():
            self.enemy.hp = max(0, self.enemy.hp - ally)
            self.combat_log.append(f"Dark spirits strike {self.enemy.name} for {ally}!")

        # ── Revive (martyred saint) ────────────────────────────────────────────
        if (not self.player.is_alive()
                and self._modifier.get("revive_once")
                and not self._revive_used):
            self._revive_used = True
            self._modifier.pop("revive_once")
            self.player.hp = self.player.max_hp // 2
            self.combat_log.append("The spirits revive you one last time!")

        if not self.player.is_alive():
            self._handle_death()

    def _victory_combat(self):
        leveled = self.player.gain_xp(self.enemy.xp)
        self.player.gold += self.enemy.gold
        self.combat_log.append(
            f"{self.enemy.name} defeated!  +{self.enemy.xp} XP  +{self.enemy.gold} gold")
        if leveled:
            self.combat_log.append(f"★ LEVEL UP! Now Level {self.player.level}! ★")
        if random.random() < 0.35:
            drop = random.choice(["health_potion", "mana_potion"])
            self.player.inventory.append(ITEMS[drop])
            self.combat_log.append(f"Dropped: {ITEMS[drop].name}!")
        for line in self.combat_log:
            self.msg(line)
        self.combat_log.clear()

        if self.floor == self.max_floors:
            self.state = "victory"
            ending = self.player.active_ending
            self.msg("\n=== VICTORY ===")
            if ending:
                self.msg(f"Ending: {t(ending['title'])}")
                self.msg(t(ending["description"]))
        else:
            self._do_rest_event()
            self._next_enemy()

    def _handle_death(self):
        for line in self.combat_log:
            self.msg(line)
        self.combat_log.clear()
        self.state = "game_over"
        self.msg(f"\nYou have been slain by {self.enemy.name}.")
        self.msg(f"Game Over — Level {self.player.level}, Floor {self.floor}.")

    def _do_rest_event(self):
        events = [
            ("rest_hp",    "hp"),
            ("rest_gold",  "gold"),
            ("rest_mp",    "mp"),
            ("rest_potion", "item"),
            ("rest_none",  "none"),
        ]
        key, kind = random.choice(events)
        self.msg(f"\n{t(key)}")
        if kind == "hp":
            h = int(self.player.max_hp * 0.2); self.player.heal(h); self.msg(t("gained_hp", n=h))
        elif kind == "gold":
            g = random.randint(5, 20); self.player.gold += g; self.msg(t("gained_gold", n=g))
        elif kind == "mp":
            r = int(self.player.max_mp * 0.3); self.player.restore_mp(r); self.msg(t("gained_mp", n=r))
        elif kind == "item":
            self.player.inventory.append(ITEMS["health_potion"]); self.msg(t("found_potion", name=ITEMS["health_potion"].name))

    # ── Story ──────────────────────────────────────────────────────────────────

    def _story_action(self, value: str):
        event = self._pending_story
        try:
            c = int(value)
        except ValueError:
            self.msg(f"Choose 1-{len(event.choices)}.")
            return
        if not (1 <= c <= len(event.choices)):
            self.msg(f"Choose 1-{len(event.choices)}.")
            return
        choice = event.choices[c - 1]
        self.player.story_flags[choice.flag] = True
        apply_effect(self.player, choice.effect)
        self.msg(t(choice.outcome))
        self._pending_story = None
        self._open_shop()

    # ── Shop ───────────────────────────────────────────────────────────────────

    def _shop_action(self, value: str):
        v = value.lower()
        if v in ("l", "leave", "done", "exit"):
            self.msg("You leave the merchant.")
            self.floor += 1
            self._start_floor()
            return

        # accept "buy N" or just "N"
        v = v.replace("buy", "").strip()
        if not v.isdigit():
            self.msg("Type a number to buy, or 'leave' to continue.")
            return
        idx = int(v) - 1
        if not (0 <= idx < len(self._shop_items)):
            self.msg(f"Choose 1-{len(self._shop_items)} or 'leave'.")
            return
        kind, key, price = self._shop_items[idx]
        if self.player.gold < price:
            self.msg(f"Not enough gold! ({self.player.gold}g, need {price}g)")
            return
        self.player.gold -= price
        if kind == "item":
            self.player.inventory.append(ITEMS[key])
            self.msg(f"Bought {ITEMS[key].name}! ({self.player.gold}g left)")
        else:
            self.msg(self.player.equip(EQUIPMENT[key]) + f" ({self.player.gold}g left)")

    # ── Response helpers ───────────────────────────────────────────────────────

    def msg(self, text: str):
        self.messages.append(text)

    def _response(self) -> dict:
        spells    = list(SPELLS.get(self.player.player_class, {}).keys()) if self.player else []
        num_spells = len(spells)
        item_num   = 2 + num_spells

        options: list[str] = []
        if self.state == "combat":
            options.append("1: Attack")
            for i, sp in enumerate(spells):
                cost = SPELLS[self.player.player_class][sp]["cost"]
                options.append(f"{i+2}: {sp}  (MP:{cost})")
            options.append(f"{item_num}: Use Item  ({len(self.player.inventory)} items)  — add ':N' to pick item")
            options.append(f"{item_num+1}: Run")
        elif self.state == "story" and self._pending_story:
            for i, c in enumerate(self._pending_story.choices, 1):
                options.append(f"{i}: {t(c.text)}")
        elif self.state == "shop":
            for i, (kind, key, price) in enumerate(self._shop_items, 1):
                if kind == "item":
                    options.append(f"{i}: {ITEMS[key].name}  ({price}g)")
                else:
                    eq = EQUIPMENT[key]
                    bonus = _eq_bonus_str(eq)
                    options.append(f"{i}: {eq.name} [{eq.slot}]  {bonus}  ({price}g)")
            options.append("leave: Leave shop")

        p = self.player
        return {
            "state":      self.state,
            "floor":      self.floor,
            "messages":   list(self.messages),
            "combat_log": list(self.combat_log[-6:]),
            "options":    options,
            "player": {
                "name":      p.name,
                "class":     p.player_class,
                "level":     p.level,
                "hp":        f"{p.hp}/{p.max_hp}",
                "mp":        f"{p.mp}/{p.max_mp}",
                "atk":       p.atk,
                "defense":   p.defense,
                "magic":     p.magic,
                "xp":        f"{p.xp}/{p.xp_next}",
                "gold":      p.gold,
                "weapon":    p.weapon.name if p.weapon else None,
                "armor":     p.armor.name  if p.armor  else None,
                "inventory": [i.name for i in p.inventory],
                "statuses":  [f"{e.name}({e.duration}t)" for e in p.status_effects],
                "flags":     list(p.story_flags.keys()),
            } if p else None,
            "enemy": {
                "name":    self.enemy.name,
                "hp":      f"{self.enemy.hp}/{self.enemy.max_hp}",
                "atk":     self.enemy.atk,
                "statuses":[f"{e.name}({e.duration}t)" for e in self.enemy.status_effects],
            } if self.enemy and self.state == "combat" else None,
        }


def _eq_bonus_str(eq) -> str:
    parts = []
    if eq.atk_bonus:   parts.append(f"+{eq.atk_bonus}ATK")
    if eq.def_bonus:   parts.append(f"+{eq.def_bonus}DEF")
    if eq.magic_bonus: parts.append(f"+{eq.magic_bonus}MAG")
    if eq.hp_bonus:    parts.append(f"+{eq.hp_bonus}HP")
    return " ".join(parts)
