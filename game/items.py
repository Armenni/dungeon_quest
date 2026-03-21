from dataclasses import dataclass


@dataclass
class Item:
    name: str
    description: str
    item_type: str  # "potion" | "potion_mp" | "elixir" | "elixir_dragon" | "cure"
    value: int
    price: int = 0


ITEMS: dict[str, Item] = {
    "health_potion":         Item("Health Potion",         "Restores 30 HP",           "potion",       30, price=15),
    "greater_health_potion": Item("Greater Health Potion", "Restores 60 HP",           "potion",       60, price=25),
    "mana_potion":           Item("Mana Potion",           "Restores 20 MP",           "potion_mp",    20, price=12),
    "elixir":                Item("Elixir",                "Restores 80 HP and 30 MP", "elixir",       80, price=35),
    "elixir_dragon":         Item("Dragon Tears",          "Restores 80 HP and 30 MP", "elixir_dragon",80, price=0),
    "antidote":              Item("Antidote",              "Cures poison and burn",    "cure",          0, price=20),
}
