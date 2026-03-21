from dataclasses import dataclass


@dataclass
class Equipment:
    name: str
    description: str
    slot: str       # "weapon" | "armor"
    price: int      # 0 = not for sale (story/drop reward)
    atk_bonus: int = 0
    def_bonus: int = 0
    magic_bonus: int = 0
    hp_bonus: int = 0


EQUIPMENT: dict[str, Equipment] = {
    # ── Weapons ───────────────────────────────────────────────────────────────
    "iron_sword":    Equipment("Iron Sword",     "A reliable blade.",           "weapon",  40, atk_bonus=4),
    "steel_sword":   Equipment("Steel Sword",    "Heavy and sharp.",            "weapon",  90, atk_bonus=8),
    "silver_dagger": Equipment("Silver Dagger",  "Light and fast.",             "weapon",  45, atk_bonus=5),
    "wizard_staff":  Equipment("Wizard Staff",   "Channels arcane energy.",     "weapon",  45, magic_bonus=6),
    "arcane_tome":   Equipment("Arcane Tome",    "Ancient spells within.",      "weapon", 100, magic_bonus=12),
    "shadow_blade":  Equipment("Shadow Blade",   "Imbued with dark power.",     "weapon",   0, atk_bonus=7, magic_bonus=2),
    "runic_blade":   Equipment("Runic Blade",    "Runes of power glow faintly.","weapon", 180, atk_bonus=10, magic_bonus=5),
    "dragon_fang":   Equipment("Dragon Fang",    "A tooth from the beast.",     "weapon",   0, atk_bonus=16, magic_bonus=6),
    # ── Armors ────────────────────────────────────────────────────────────────
    "padded_vest":   Equipment("Padded Vest",    "Basic protection.",           "armor",   25, def_bonus=3),
    "leather_armor": Equipment("Leather Armor",  "Sturdy hide armor.",          "armor",   45, def_bonus=6),
    "chain_mail":    Equipment("Chain Mail",     "Interlocked iron rings.",     "armor",   80, def_bonus=10, hp_bonus=10),
    "mage_robes":    Equipment("Mage Robes",     "Woven with enchantments.",    "armor",   50, def_bonus=4, magic_bonus=4),
    "dragon_scale":  Equipment("Dragon Scale",   "Nearly impenetrable hide.",   "armor",    0, def_bonus=14, hp_bonus=20),
}

SHOP_STOCK: dict[int, dict[str, list[str]]] = {
    1: {"weapons": ["iron_sword", "silver_dagger"],              "armors": ["padded_vest"]},
    2: {"weapons": ["iron_sword", "silver_dagger","wizard_staff"],"armors": ["padded_vest", "leather_armor"]},
    3: {"weapons": ["steel_sword", "wizard_staff","arcane_tome"], "armors": ["leather_armor", "chain_mail", "mage_robes"]},
    4: {"weapons": ["steel_sword", "arcane_tome", "runic_blade"], "armors": ["chain_mail", "mage_robes"]},
}

POTION_SHOP: list[tuple[str, int]] = [
    ("health_potion",         15),
    ("greater_health_potion", 25),
    ("mana_potion",           12),
    ("elixir",                35),
    ("antidote",              20),
]
