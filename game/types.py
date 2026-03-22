"""
Shared type definitions for the game.

Centralized dataclasses used across modules to ensure type safety
and consistency.
"""

from dataclasses import dataclass


@dataclass
class StatusEffect:
    """A temporary status affecting a player or enemy."""
    name: str       # Display name (e.g., "Poisoned")
    etype: str      # Type: "poison" | "burn" | "stun" | "weakened" | "shielded"
    duration: int   # Turns remaining
    magnitude: int  # Damage per tick, or potency magnitude


@dataclass
class Choice:
    """A player choice in a story event."""
    text: str           # Choice text key (translatable, e.g., "choice_spare_text")
    outcome: str        # Outcome message key (e.g., "choice_spare_outcome")
    flag: str           # Story flag set if chosen (e.g., "spared_prisoner")
    effect: dict        # Mechanical effect: {"atk": 2, "gold": 10, "item": "key"}
    class_only: str = None  # Restrict to class: "Warrior" | "Mage" | "Rogue" | None


@dataclass
class StoryEvent:
    """A story event that triggers between floors."""
    title: str          # Event title key (e.g., "prisoner_title")
    narrative: str      # Event description key (e.g., "prisoner_narrative")
    floor_after: int    # Triggers after clearing this floor (1-6)
    choices: list       # List of Choice objects


@dataclass
class StoryEnding:
    """An ending the player can achieve."""
    title: str              # Ending name key
    description: str        # Ending description key
    dragon_modifier: dict   # Modifiers applied to Dragon fight
    # Example:
    # {
    #   "dragon_hp_mult": 0.7,
    #   "dragon_atk_mult": 1.0,
    #   "player_def_bonus": 0,
    #   "ally_dmg_per_turn": 0,
    #   "revive_once": False,
    #   "bonus_msg": "weak_dragon"
    # }
