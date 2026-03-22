from typing import List, Optional
from game.items import Item, ITEMS
from game.equipment import Equipment
from game.i18n import t


CLASS_STATS: dict[str, dict] = {
    "Warrior": {"hp": 120, "mp": 20,  "atk": 15, "defense": 12, "spd": 8,  "magic": 5},
    "Mage":    {"hp": 70,  "mp": 80,  "atk": 8,  "defense": 6,  "spd": 9,  "magic": 20},
    "Rogue":   {"hp": 90,  "mp": 30,  "atk": 12, "defense": 8,  "spd": 15, "magic": 8},
}


class Player:
    def __init__(self, name: str, player_class: str):
        self.name = name
        self.player_class = player_class
        s = CLASS_STATS[player_class]

        # Base stats (never include equipment bonuses)
        self._base_atk     = s["atk"]
        self._base_defense = s["defense"]
        self._base_magic   = s["magic"]
        self._base_max_hp  = s["hp"]

        # Effective stats (base + equipment)
        self.atk     = self._base_atk
        self.defense = self._base_defense
        self.magic   = self._base_magic
        self.max_hp  = self._base_max_hp
        self.hp      = self.max_hp
        self.max_mp  = s["mp"]
        self.mp      = self.max_mp
        self.spd     = s["spd"]

        self.level   = 1
        self.xp      = 0
        self.xp_next = 50
        self.gold    = 10

        self.inventory: List[Item] = [ITEMS["health_potion"], ITEMS["health_potion"]]

        # Equipment slots
        self.weapon: Optional[Equipment] = None
        self.armor:  Optional[Equipment] = None

        # Status effects (managed by game/status.py)
        self.status_effects: list = []

        # Story system
        self.story_flags: dict[str, bool] = {}
        self.active_ending: Optional[dict] = None

    # ── Combat ────────────────────────────────────────────────────────────────

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> int:
        shield = next((e for e in self.status_effects if e.etype == "shielded"), None)
        if shield:
            self.status_effects.remove(shield)
            damage = damage // 2
        actual = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

    def heal(self, amount: int):
        self.hp = min(self.max_hp, self.hp + amount)

    def restore_mp(self, amount: int):
        self.mp = min(self.max_mp, self.mp + amount)

    # ── Progression ───────────────────────────────────────────────────────────

    def gain_xp(self, amount: int) -> bool:
        self.xp += amount
        if self.xp >= self.xp_next:
            self._level_up()
            return True
        return False

    def _level_up(self):
        self.level        += 1
        self.xp           -= self.xp_next
        self.xp_next       = int(self.xp_next * 1.5)
        self._base_atk    += 3
        self._base_defense += 2
        self._base_magic  += 2
        self._base_max_hp += 15
        self.max_mp       += 10
        self.mp            = self.max_mp
        self._recalc_equipment()
        self.hp = self.max_hp   # full heal on level-up

    def apply_bonus(self, atk: int = 0, defense: int = 0, magic: int = 0,
                    max_hp: int = 0, hp: int = 0):
        """Permanent stat bonus from story events."""
        self._base_atk    += atk
        self._base_defense += defense
        self._base_magic  += magic
        self._base_max_hp += max_hp
        self._recalc_equipment()
        if max_hp > 0:
            self.hp = min(self.hp + max_hp, self.max_hp)
        if hp != 0:
            self.hp = max(1, min(self.max_hp, self.hp + hp))

    # ── Equipment ─────────────────────────────────────────────────────────────

    def equip(self, eq: Equipment) -> str:
        if eq.slot == "weapon":
            self.weapon = eq
        else:
            self.armor = eq
        self._recalc_equipment()
        return t("equipped", name=eq.name)

    def _recalc_equipment(self):
        w = self.weapon
        a = self.armor
        self.atk     = self._base_atk     + (w.atk_bonus   if w else 0) + (a.atk_bonus   if a else 0)
        self.defense = self._base_defense + (w.def_bonus    if w else 0) + (a.def_bonus    if a else 0)
        self.magic   = self._base_magic   + (w.magic_bonus  if w else 0) + (a.magic_bonus  if a else 0)
        hp_bonus     = (w.hp_bonus if w else 0) + (a.hp_bonus if a else 0)
        old_max      = self.max_hp
        self.max_hp  = self._base_max_hp + hp_bonus
        # Proportionally adjust current HP when max changes
        if old_max > 0 and self.max_hp != old_max:
            self.hp = min(self.hp + (self.max_hp - old_max), self.max_hp)

    # ── Inventory ─────────────────────────────────────────────────────────────

    def use_item(self, index: int) -> str:
        if not (0 <= index < len(self.inventory)):
            return t("invalid_item")
        item = self.inventory.pop(index)
        if item.item_type == "potion":
            self.heal(item.value)
            return t("item_used_hp", name=item.name, val=item.value)
        elif item.item_type == "potion_mp":
            self.restore_mp(item.value)
            return t("item_used_mp", name=item.name, val=item.value)
        elif item.item_type in ("elixir", "elixir_dragon"):
            self.heal(item.value)
            self.restore_mp(30)
            return t("item_used_elixir", name=item.name, val=item.value)
        elif item.item_type == "cure":
            self.status_effects = [e for e in self.status_effects
                                   if e.etype not in ("poison", "burn")]
            return t("item_used_cure", name=item.name)
        return t("item_used_generic", name=item.name)
