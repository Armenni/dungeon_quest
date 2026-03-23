import json
import random
from pathlib import Path

HAS_FLESH: set[str] = {
    "Goblin", "Orc", "Dark Mage", "Troll", "Cultist", "Dragon", "Cave Spider"
}
# No flesh: Skeleton, Stone Golem, Wraith

_cache: dict[str, dict] = {}


def load_flavor(lang: str = "en") -> dict:
    if lang in _cache:
        return _cache[lang]
    path = Path(__file__).parent / "lang" / f"{lang}_flavor.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _cache[lang] = data
    return data


def get_flavor(category: str, has_flesh: bool, cause: str = "normal",
               lang: str = "en") -> str:
    """Pick a random flavor string. Returns '' on any miss — never crashes."""
    try:
        data = load_flavor(lang)
        node = data.get(category, [])

        if isinstance(node, list):
            return random.choice(node) if node else ""

        flesh_key = "true" if has_flesh else "false"
        if cause in node:
            options = node[cause].get(flesh_key, [])
        elif flesh_key in node:
            # Flat has_flesh dict (e.g. status_tick_burn)
            options = node[flesh_key]
        else:
            options = []

        return random.choice(options) if options else ""
    except Exception:
        return ""
