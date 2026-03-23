from typing import List, Optional, Union
from game.items import Item, ITEMS
from game.equipment import Equipment
from game.i18n import t


# The five primary stats drive derived combat values:
#   ATK   = strength * 2 + 5  + equipment_atk_bonus  + _base_atk (event bonuses)
#   MAGIC = intelligence * 4  + equipment_magic_bonus + _base_magic (event bonuses)
#   Dodge % = agility * 3
#   Crit %  = 5 + luck * 3
#   Shop discount = (charisma - 1) * 5% (capped at 50%)
PRIMARY_STATS = ("strength", "intelligence", "agility", "luck", "charisma")

CLASS_STATS: dict[str, dict] = {
    "Warrior": {"hp": 120, "mp": 20, "defense": 12, "spd": 8,
                "strength": 5, "intelligence": 1, "agility": 4, "luck": 2, "charisma": 1},
    "Mage":    {"hp": 70,  "mp": 80, "defense": 6,  "spd": 9,
                "strength": 1, "intelligence": 5, "agility": 2, "luck": 4, "charisma": 1},
    "Rogue":   {"hp": 90,  "mp": 30, "defense": 8,  "spd": 15,
                "strength": 3, "intelligence": 2, "agility": 5, "luck": 3, "charisma": 4},
}


class Player:
    def __init__(self, name: str, player_class: str):
        self.name = name
        self.player_class = player_class
        s = CLASS_STATS[player_class]

        # Primary stats (drive derived stats and mechanics)
        self.strength     = s["strength"]
        self.intelligence = s["intelligence"]
        self.agility      = s["agility"]
        self.luck         = s["luck"]
        self.charisma     = s["charisma"]

        # Flat bonus stats (defense and hp have no primary stat driving them)
        self._base_defense = s["defense"]
        self._base_max_hp  = s["hp"]
        # Legacy event/bonus offsets on top of primary-derived values
        self._base_atk   = 0
        self._base_magic = 0

        # Effective stats (recalculated; do not mutate directly)
        self.atk     = 0
        self.defense = 0
        self.magic   = 0
        self.max_hp  = 0
        self.hp      = 0
        self.max_mp  = s["mp"]
        self.mp      = self.max_mp
        self.spd     = s["spd"]

        self.level   = 1
        self.xp      = 0
        self.xp_next = 50
        self.gold    = 10

        # True after levelling up until the player picks a stat to raise
        self.pending_stat_choice = False

        self.inventory: List[Union[Item, Equipment]] = [ITEMS["health_potion"], ITEMS["health_potion"]]
        self.bag: List[Equipment] = []  # unequipped gear

        # Equipment slots
        self.weapon: Optional[Equipment] = None
        self.armor:  Optional[Equipment] = None

        # Status effects (managed by game/status.py)
        self.status_effects: list = []

        # Story system
        self.story_flags: dict[str, bool] = {}
        self.active_ending: Optional[dict] = None

        self._recalc_equipment()
        self.hp = self.max_hp

    # ── Properties ────────────────────────────────────────────────────────────

    @property
    def crit_chance(self) -> float:
        """Critical hit probability (0.0–1.0)."""
        return min(0.75, (5 + self.luck * 3) / 100)

    @property
    def dodge_chance(self) -> float:
        """Dodge probability (0.0–1.0)."""
        return min(0.60, self.agility * 3 / 100)

    @property
    def shop_discount(self) -> float:
        """Fraction to multiply shop prices by (lower = cheaper)."""
        return max(0.50, 1.0 - (self.charisma - 1) * 0.05)

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
        self.level         += 1
        self.xp            -= self.xp_next
        self.xp_next        = int(self.xp_next * 1.5)
        # Flat stat gains (DEF/HP/MP don't have a primary stat)
        self._base_defense += 1
        self._base_max_hp  += 10
        self.max_mp        += 5
        self.mp             = self.max_mp
        # Player must choose which primary stat to raise
        self.pending_stat_choice = True
        self._recalc_equipment()
        self.hp = self.max_hp  # full heal on level-up

    def apply_stat_up(self, stat: str):
        """Apply +1 to a primary stat chosen during level-up."""
        if stat in PRIMARY_STATS:
            setattr(self, stat, getattr(self, stat) + 1)
            self._recalc_equipment()
        self.pending_stat_choice = False

    def apply_bonus(self, atk: int = 0, defense: int = 0, magic: int = 0,
                    max_hp: int = 0, hp: int = 0,
                    strength: int = 0, intelligence: int = 0,
                    agility: int = 0, luck: int = 0, charisma: int = 0):
        """Permanent stat bonus from story events.

        Accepts both legacy keys (atk, magic) and primary stat keys.
        Legacy atk/magic add flat offsets on top of the primary-stat derivation.
        """
        self.strength     += strength
        self.intelligence += intelligence
        self.agility      += agility
        self.luck         += luck
        self.charisma     += charisma
        self._base_atk    += atk
        self._base_magic  += magic
        self._base_defense += defense
        self._base_max_hp  += max_hp
        self._recalc_equipment()
        if max_hp > 0:
            self.hp = min(self.hp + max_hp, self.max_hp)
        if hp != 0:
            self.hp = max(1, min(self.max_hp, self.hp + hp))

    # ── Equipment ─────────────────────────────────────────────────────────────

    def equip(self, eq: Equipment) -> tuple[str, Optional[Equipment]]:
        """Equip an item. Returns (message, displaced_item_or_None)."""
        old_eq = None
        if eq.slot == "weapon":
            old_eq = self.weapon
            self.weapon = eq
        else:
            old_eq = self.armor
            self.armor = eq
        # Remove from bag if it was there
        if eq in self.bag:
            self.bag.remove(eq)
        self._recalc_equipment()
        return t("equipped", name=eq.name), old_eq

    def unequip(self, slot: str) -> str:
        """Unequip gear into the bag. Returns the item name or ''."""
        if slot == "weapon" and self.weapon:
            item = self.weapon
            self.weapon = None
            self.bag.append(item)
            self._recalc_equipment()
            return item.name
        if slot == "armor" and self.armor:
            item = self.armor
            self.armor = None
            self.bag.append(item)
            self._recalc_equipment()
            return item.name
        return ""

    def _recalc_equipment(self):
        w = self.weapon
        a = self.armor
        str_atk   = self.strength * 2 + 5
        int_magic = self.intelligence * 4
        self.atk     = str_atk   + self._base_atk   + (w.atk_bonus   if w else 0) + (a.atk_bonus   if a else 0)
        self.defense = self._base_defense            + (w.def_bonus    if w else 0) + (a.def_bonus    if a else 0)
        self.magic   = int_magic + self._base_magic  + (w.magic_bonus  if w else 0) + (a.magic_bonus  if a else 0)
        hp_bonus     = (w.hp_bonus if w else 0) + (a.hp_bonus if a else 0)
        old_max      = self.max_hp
        self.max_hp  = self._base_max_hp + hp_bonus
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
