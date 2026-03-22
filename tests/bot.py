"""
Shared TestBot class for all test harnesses.

Single source of truth for bot decision logic:
- Combat decisions (spell/item/attack based on HP/MP)
- Story choices (random or fixed paths)
- Shop/inventory handling

Used by: dragon_test.py, simulate.py, any other test harness.
"""

import re
import random


class TestBot:
    """Stateless test bot with configurable strategy."""

    def __init__(self, cls: str = "1", story_pick: str = "random", name: str = "TestBot"):
        """
        Args:
            cls: "1"=Warrior, "2"=Mage, "3"=Rogue
            story_pick: "1"=kind, "2"=pragmatic, "3"=dark, "random"
            name: Bot name for logging
        """
        self.cls = cls
        self.story_pick = story_pick
        self.name = name
        self.decisions = []          # Track decisions for logging
        self.player_ref = None       # Set by test harness after Player created

    def decide(self, prompt: str) -> str:
        """Main decision entry point. Returns response to prompt."""
        p = prompt.strip()
        r = self._pick(p)
        self.decisions.append({"prompt": p[:120], "response": r})
        return r

    def _pick(self, p: str) -> str:
        """Route prompt to appropriate handler."""
        pl = p.lower()

        # Language selection
        if any(x in pl for x in ["selecione", "select language"]):
            return "1"  # Always English

        # Name input
        if any(x in pl for x in ["name", "nome"]):
            return self.name

        # Class selection
        if any(x in pl for x in ["1, 2, or 3", "1, 2 ou 3"]):
            return self.cls

        # Combat action
        if "action" in pl:
            return self._combat_decision(p)

        # Story choice
        if any(x in pl for x in ["choice", "escolha"]):
            return self._story_decision(p)

        # Shop/buying
        if any(x in pl for x in ["buy", "comprar"]):
            return "l"  # Leave shop immediately

        # Use item from inventory
        if "use item" in pl:
            return "1"  # Use first item

        # Cancel inventory
        if "cancel" in pl:
            return "0"

        # Default: confirm/continue on all pauses
        return ""

    def _combat_decision(self, prompt: str) -> str:
        """Decide combat action: attack/spell/item/run based on state."""
        m = re.search(r"1-(\d+)", prompt)
        max_action = int(m.group(1)) if m else 4

        # No player ref → safe default
        if not self.player_ref:
            return "1"  # Attack

        p = self.player_ref
        hp_pct = p.hp / max(1, p.max_hp)

        # Low HP + have items → use item
        if hp_pct < 0.35 and p.inventory:
            item_slot = max_action - 1
            return str(item_slot)

        # Have MP + have spells → cast spell
        num_spells = max_action - 3  # item and run take last 2 slots
        if num_spells >= 1 and p.mp >= 10:
            return "2"  # First spell slot

        # Default: attack
        return "1"

    def _story_decision(self, prompt: str) -> str:
        """Decide story choice: random or follow strategy."""
        m = re.search(r"1-(\d+)", prompt)
        max_choice = int(m.group(1)) if m else 3

        if self.story_pick == "random":
            return str(random.randint(1, max_choice))

        # Return configured choice, or 1 if out of range
        return self.story_pick if int(self.story_pick) <= max_choice else "1"
