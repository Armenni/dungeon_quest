"""
Test strategy definitions for reproducible testing.

Each strategy defines a class/story-path combination to test different
game paths and detect balance issues.

Strategies can be:
- Picked individual runs (for debugging)
- Run in parallel (stress testing)
- Compared for win-rate regressions
"""

# Strategy tuple: (class, story_pick, name, description)
# class: "1"=Warrior, "2"=Mage, "3"=Rogue
# story_pick: "1"=kind/merciful, "2"=pragmatic, "3"=dark, "random"

STRATEGIES = [
    # ── Main Paths (3 classes × 3 story choices) ───────────────────────────────

    # Warrior paths
    ("1", "1", "Warrior_Merciful",
     "Warrior, always kind choices, uses spells"),
    ("1", "2", "Warrior_Pragmatic",
     "Warrior, always middle choices, balanced"),
    ("1", "3", "Warrior_Dark",
     "Warrior, always dark choices, aggressive"),

    # Mage paths
    ("2", "1", "Mage_Merciful",
     "Mage, always kind choices, full spell rotation"),
    ("2", "2", "Mage_Pragmatic",
     "Mage, always middle choices"),
    ("2", "3", "Mage_Dark",
     "Mage, always dark choices"),

    # Rogue paths
    ("3", "1", "Rogue_Merciful",
     "Rogue, always kind choices, high crit"),
    ("3", "2", "Rogue_Pragmatic",
     "Rogue, always middle choices"),
    ("3", "3", "Rogue_Dark",
     "Rogue, always dark choices"),

    # ── Random/Mixed Strategies ─────────────────────────────────────────────────

    ("1", "random", "Warrior_Random",
     "Warrior, random story choices"),
    ("2", "random", "Mage_Random",
     "Mage, random story choices"),
    ("3", "random", "Rogue_Random",
     "Rogue, random story choices"),

    # ── Edge Cases (for stress testing) ──────────────────────────────────────────

    # (Optional: uncomment to add stress tests)
    # ("1", "1", "Warrior_NoItems",
    #  "Warrior, never use potions"),
    # ("2", "1", "Mage_LowMana",
    #  "Mage, conservative with mana"),
]


def get_strategies(filter_name: str = None) -> list:
    """
    Get strategies, optionally filtered by name substring.

    Args:
        filter_name: Optional substring to filter (e.g., "Warrior" returns Warrior_*)

    Returns:
        List of (class, story_pick, name, description) tuples
    """
    if not filter_name:
        return STRATEGIES
    return [s for s in STRATEGIES if filter_name.lower() in s[2].lower()]


def get_strategy_by_name(name: str) -> tuple:
    """Get a single strategy by exact name."""
    for s in STRATEGIES:
        if s[2] == name:
            return s
    raise ValueError(f"Strategy not found: {name}")
