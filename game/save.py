"""Save / Load system — single-slot auto-save to save.json."""
import json
import os
from typing import Optional

SAVE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "save.json")


def save_game(player, floor: int) -> None:
    """Serialize player + floor to save.json."""
    from game.equipment import Equipment

    def eq_name(eq) -> Optional[str]:
        return eq.name if eq else None

    data = {
        "floor": floor,
        "player": {
            "name":         player.name,
            "cls":          player.player_class,
            "level":        player.level,
            "xp":           player.xp,
            "xp_next":      player.xp_next,
            "hp":           player.hp,
            "max_hp":       player.max_hp,
            "mp":           player.mp,
            "max_mp":       player.max_mp,
            "gold":         player.gold,
            # Primary stats
            "strength":     player.strength,
            "intelligence": player.intelligence,
            "agility":      player.agility,
            "luck":         player.luck,
            "charisma":     player.charisma,
            # Flat offsets
            "_base_defense": player._base_defense,
            "_base_max_hp":  player._base_max_hp,
            "_base_atk":     player._base_atk,
            "_base_magic":   player._base_magic,
            # Equipment (by name)
            "weapon": eq_name(player.weapon),
            "armor":  eq_name(player.armor),
            "bag":    [eq.name for eq in player.bag],
            # Story state
            "story_flags": player.story_flags,
        }
    }
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_game() -> Optional[dict]:
    """Return parsed save data, or None if no save exists."""
    if not os.path.exists(SAVE_PATH):
        return None
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, KeyError):
        return None


def delete_save() -> None:
    """Remove the save file (called on death or victory)."""
    if os.path.exists(SAVE_PATH):
        os.remove(SAVE_PATH)


def restore_player(data: dict):
    """Rebuild a Player from saved data dict."""
    from game.player import Player
    from game.equipment import EQUIPMENT

    pd = data["player"]
    player = Player(pd["name"], pd["cls"])

    # Primary stats
    player.strength     = pd["strength"]
    player.intelligence = pd["intelligence"]
    player.agility      = pd["agility"]
    player.luck         = pd["luck"]
    player.charisma     = pd["charisma"]

    # Flat offsets
    player._base_defense = pd["_base_defense"]
    player._base_max_hp  = pd["_base_max_hp"]
    player._base_atk     = pd["_base_atk"]
    player._base_magic   = pd["_base_magic"]

    # Progression
    player.level   = pd["level"]
    player.xp      = pd["xp"]
    player.xp_next = pd["xp_next"]
    player.max_mp  = pd["max_mp"]
    player.gold    = pd["gold"]

    # Equipment
    player.weapon = EQUIPMENT.get(pd["weapon"]) if pd.get("weapon") else None
    player.armor  = EQUIPMENT.get(pd["armor"])  if pd.get("armor")  else None
    player.bag    = [EQUIPMENT[n] for n in pd.get("bag", []) if n in EQUIPMENT]

    # Story
    player.story_flags = pd.get("story_flags", {})

    # Recalculate effective stats, then set HP/MP from save
    player._recalc_equipment()
    player.hp = min(pd["hp"], player.max_hp)
    player.mp = min(pd["mp"], player.max_mp)

    return player
