from dataclasses import dataclass
from typing import List, Tuple
from game.i18n import t


@dataclass
class StatusEffect:
    name: str       # display name
    etype: str      # "poison" | "burn" | "stun" | "weakened"
    duration: int   # turns remaining
    magnitude: int  # damage per tick, or potency


EFFECT_COLORS: dict[str, str] = {
    "poison":   "green",
    "burn":     "red",
    "stun":     "yellow",
    "weakened": "dim",
    "shielded": "blue",
}


def apply_status(target, etype: str, duration: int, magnitude: int = 0):
    """Add or refresh a status on a target. Refreshes if already present."""
    for e in target.status_effects:
        if e.etype == etype:
            e.duration  = max(e.duration, duration)
            e.magnitude = max(e.magnitude, magnitude)
            return
    target.status_effects.append(StatusEffect(t(f"status_{etype}"), etype, duration, magnitude))


def tick_statuses(target) -> List[Tuple[str, int]]:
    """
    Process DoT effects at the start of a turn.
    Returns list of (rich_message, damage_dealt) pairs.
    Stun/weakened are NOT ticked here — checked inline in combat.
    """
    results: List[Tuple[str, int]] = []
    keep: List[StatusEffect] = []

    for e in target.status_effects:
        c = EFFECT_COLORS.get(e.etype, "white")
        if e.etype == "stun":
            keep.append(e)   # stun duration managed exclusively by consume_stun
            continue
        if e.etype in ("poison", "burn"):
            target.hp = max(0, target.hp - e.magnitude)
            results.append((f"[{c}]{e.name}[/{c}] {t('deals_damage', n=e.magnitude)}", e.magnitude))
        e.duration -= 1      # weakened and DoTs tick down here
        if e.duration > 0:
            keep.append(e)
        else:
            results.append((f"[dim]{t('status_fades', name=e.name)}[/dim]", 0))

    target.status_effects = keep
    return results


def consume_stun(target) -> bool:
    """Check for stun, consume one turn of it, return True if stunned."""
    for e in target.status_effects:
        if e.etype == "stun":
            e.duration -= 1
            target.status_effects = [x for x in target.status_effects if x.duration > 0]
            return True
    return False


def weakened_penalty(target) -> int:
    """ATK reduction from weakened (not applied to stats — used inline)."""
    for e in target.status_effects:
        if e.etype == "weakened":
            return e.magnitude
    return 0


def status_tags(target) -> str:
    """Compact Rich-formatted tag string for the combat HUD."""
    if not target.status_effects:
        return ""
    parts = []
    for e in target.status_effects:
        c = EFFECT_COLORS.get(e.etype, "white")
        parts.append(f"[{c}]{e.etype[:3].upper()}({e.duration})[/{c}]")
    return "  " + " ".join(parts)
