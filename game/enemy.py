import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Enemy:
    name: str
    hp: int
    max_hp: int
    atk: int
    defense: int
    spd: int
    xp: int
    gold: int
    abilities: List[str]
    status_effects: list = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> int:
        actual = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual


def make_enemy(name: str, floor: int) -> Enemy:
    s = 1 + (floor - 1) * 0.3
    if name == "Dragon":
        s = min(s, 2.0)   # scale Dragon for the 7-floor game
    templates: dict[str, tuple] = {
        "Goblin":    (int(30*s), int(8*s),  int(3*s),  10, int(15*s), int(5*s),
                      ["attack", "poison_sting"]),
        "Orc":       (int(60*s), int(12*s), int(6*s),  6,  int(25*s), int(8*s),
                      ["attack", "heavy_strike", "curse"]),
        "Skeleton":  (int(40*s), int(10*s), int(4*s),  12, int(20*s), int(6*s),
                      ["attack", "bone_throw"]),
        "Dark Mage": (int(35*s), int(15*s), int(2*s),  11, int(30*s), int(10*s),
                      ["attack", "fireball", "curse"]),
        "Troll":     (int(80*s), int(14*s), int(8*s),  5,  int(35*s), int(12*s),
                      ["attack", "regenerate", "stun_bash"]),
        "Wraith":    (int(45*s), int(13*s), int(4*s),  10, int(28*s), int(9*s),
                      ["attack", "drain_mana", "life_steal"]),
        "Cultist":   (int(50*s), int(11*s), int(5*s),  11, int(32*s), int(11*s),
                      ["attack", "dark_ritual", "shadow_bolt"]),
        "Dragon":    (int(220*s),int(24*s), 18,        8,  200,       50,
                      ["attack", "fire_breath", "tail_swipe", "toxic_breath",
                       "wing_stun", "regenerate"]),
    }
    hp, atk, defense, spd, xp, gold, abilities = templates[name]
    return Enemy(name, hp, hp, atk, defense, spd, xp, gold, abilities)


def make_boss_with_modifiers(floor: int, modifier: dict) -> Enemy:
    """Build the Dragon and apply story-driven stat modifiers."""
    boss = make_enemy("Dragon", floor)
    hp_mult  = modifier.get("dragon_hp_mult",  1.0)
    atk_mult = modifier.get("dragon_atk_mult", 1.0)
    boss.hp     = int(boss.hp  * hp_mult)
    boss.max_hp = int(boss.max_hp * hp_mult)
    boss.atk    = int(boss.atk * atk_mult)
    return boss


FLOOR_ENEMIES: dict[int, list[str]] = {
    1: ["Goblin", "Goblin", "Skeleton"],
    2: ["Goblin", "Orc", "Skeleton"],
    3: ["Orc", "Skeleton", "Dark Mage", "Wraith"],
    4: ["Orc", "Dark Mage", "Troll", "Wraith"],
    5: ["Dark Mage", "Troll", "Wraith", "Cultist"],
    6: ["Troll", "Dark Mage", "Cultist"],
    7: ["Dragon"],
}


def get_random_enemy(floor: int) -> Enemy:
    pool = FLOOR_ENEMIES.get(floor, ["Goblin"])
    return make_enemy(random.choice(pool), floor)


def get_boss(floor: int) -> Enemy:
    return make_enemy("Dragon", floor)
