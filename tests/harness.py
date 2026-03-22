"""
TestHarness: Context manager for clean I/O mocking.

Encapsulates all Console/input patching in one place, making it:
- Easier to maintain if Rich API changes
- Clear what's being patched and why
- Safe to restore in case of errors

Usage:
    bot = TestBot(cls="1", story_pick="1", name="Warrior_Test")
    with TestHarness(bot) as harness:
        run_game(bot)
        print(harness.output_log)  # Access captured output
"""

import builtins
from rich.console import Console


class TestHarness:
    """Context manager for test I/O mocking."""

    # Class-level storage for active harness (for patched functions)
    _active_harness = None

    def __init__(self, bot):
        """
        Args:
            bot: TestBot instance to use for decisions
        """
        self.bot = bot
        self.output_log = []

        # Store original methods for restoration
        self._original_builtins_input = None
        self._original_console_input = None
        self._original_console_print = None
        self._original_console_clear = None

    def __enter__(self):
        """Set up patches when entering context."""
        TestHarness._active_harness = self

        # Patch builtins.input
        self._original_builtins_input = builtins.input
        builtins.input = self._patched_input

        # Patch Console methods
        self._original_console_input = Console.input
        self._original_console_print = Console.print
        self._original_console_clear = Console.clear

        Console.input = self._patched_console_input
        Console.print = self._patched_console_print
        Console.clear = self._patched_console_clear

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore original methods when exiting context."""
        # Restore builtins.input
        if self._original_builtins_input:
            builtins.input = self._original_builtins_input

        # Restore Console methods
        if self._original_console_input:
            Console.input = self._original_console_input
        if self._original_console_print:
            Console.print = self._original_console_print
        if self._original_console_clear:
            Console.clear = self._original_console_clear

        TestHarness._active_harness = None
        return False

    # ── Static patched methods ──────────────────────────────────────────────────

    @staticmethod
    def _patched_input(prompt: str = "") -> str:
        """Patched builtins.input — use bot to decide."""
        h = TestHarness._active_harness
        if not h:
            return ""
        return h.bot.decide(str(prompt))

    @staticmethod
    def _patched_console_input(self, prompt: str = "", **kwargs) -> str:
        """Patched Console.input — use bot to decide."""
        h = TestHarness._active_harness
        if not h:
            return ""
        return h.bot.decide(str(prompt))

    @staticmethod
    def _patched_console_print(self, *args, **kwargs) -> None:
        """Patched Console.print — log output instead of printing."""
        h = TestHarness._active_harness
        if not h:
            return
        msg = " ".join(str(a) for a in args)
        if msg.strip():
            h.output_log.append(msg[:500])  # Truncate very long lines

    @staticmethod
    def _patched_console_clear(self) -> None:
        """Patched Console.clear — no-op to keep output readable."""
        pass
