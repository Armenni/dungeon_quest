import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
from rich import box
from game.i18n import t

console = Console()

ENEMY_ART: dict[str, str] = {
    "Goblin":    "[green]( o_o)[/green]  [dim]<goblin>[/dim]",
    "Orc":       "[bold green]( O_O)[/bold green]  [dim]<orc>[/dim]",
    "Skeleton":  "[white](x_x)[/white]  [dim]<skeleton>[/dim]",
    "Dark Mage": "[magenta](>_<)[/magenta]  [dim]<dark mage>[/dim]",
    "Troll":     "[bold]( @_@)[/bold]  [dim]<troll>[/dim]",
    "Dragon":    "[bold red]( >_<)[/bold red]  [dim]<<  DRAGON  >>[/dim]",
}

CLASS_ART: dict[str, str] = {
    "Warrior": "[bold red](^_^)[/bold red]  [dim]<warrior>[/dim]",
    "Mage":    "[bold blue](~_~)[/bold blue]  [dim]<mage>[/dim]",
    "Rogue":   "[bold green](._-)[/bold green]  [dim]<rogue>[/dim]",
}


def _bar(pct: float, width: int = 20) -> str:
    filled = max(0, min(width, int(pct * width)))
    color = "green" if pct > 0.5 else "yellow" if pct > 0.25 else "red"
    return f"[{color}]{'█' * filled}[/{color}]{'░' * (width - filled)}"


class UI:
    def __init__(self):
        self.log: list[str] = []

    def clear(self):
        console.clear()

    def print(self, msg: str = ""):
        console.print(msg)

    def input(self, prompt: str) -> str:
        return console.input(f"[bold cyan]{prompt}[/bold cyan]").strip()

    def pause(self, msg: str = None):
        if msg is None:
            msg = t("press_enter")
        console.input(f"\n[dim]{msg}[/dim]")

    # ── Title ─────────────────────────────────────────────────────────────────

    def show_title(self):
        self.clear()
        console.print()
        console.print("  [bold yellow]╔══════════════════════════════════╗[/bold yellow]")
        console.print("  [bold yellow]║[/bold yellow]  [bold red]D U N G E O N   Q U E S T[/bold red]  [bold yellow]║[/bold yellow]")
        console.print("  [bold yellow]╚══════════════════════════════════╝[/bold yellow]")
        console.print(f"      [italic dim]{t('subtitle')}[/italic dim]\n")

    # ── Class selection ────────────────────────────────────────────────────────

    def choose_class(self) -> str:
        console.print(f"[bold yellow]{t('choose_class')}[/bold yellow]\n")
        options = {
            "1": ("Warrior", t("class_warrior_desc"), "bold red"),
            "2": ("Mage",    t("class_mage_desc"),    "bold blue"),
            "3": ("Rogue",   t("class_rogue_desc"),   "bold green"),
        }
        for key, (name, desc, style) in options.items():
            console.print(f"  [{style}]{key}. {name}[/{style}] — {desc}")
        while True:
            choice = self.input(t("enter_class_prompt"))
            if choice in options:
                return options[choice][0]
            console.print(t("invalid_choice"))

    # ── Combat screen ──────────────────────────────────────────────────────────

    def show_combat(self, player, enemy):
        self.clear()
        from game.status import status_tags

        # Enemy panel
        enemy_art  = ENEMY_ART.get(enemy.name, f"(?_?)  <{enemy.name}>")
        e_hp_pct   = enemy.hp / max(1, enemy.max_hp)
        e_tags     = status_tags(enemy)
        enemy_panel = Panel(
            f"{enemy_art}\n\n"
            f"HP: [red]{enemy.hp}[/red]/{enemy.max_hp}  {_bar(e_hp_pct)}"
            f"{e_tags}",
            title=f"[bold red]{enemy.name}[/bold red]",
            border_style="red",
            width=46,
        )

        # Player panel
        player_art  = CLASS_ART.get(player.player_class, "(^_^)  <hero>")
        p_hp_pct    = player.hp / max(1, player.max_hp)
        p_mp_pct    = player.mp / max(1, player.max_mp)
        p_tags      = status_tags(player)
        w_name      = player.weapon.name if player.weapon else "none"
        a_name      = player.armor.name  if player.armor  else "none"
        player_panel = Panel(
            f"{player_art}\n\n"
            f"HP: [red]{player.hp}[/red]/{player.max_hp}  {_bar(p_hp_pct)}\n"
            f"MP: [blue]{player.mp}[/blue]/{player.max_mp}  {_bar(p_mp_pct)}\n"
            f"[dim]⚔ {w_name}   🛡 {a_name}[/dim]"
            f"{p_tags}",
            title=f"[bold green]{player.name}[/bold green] Lv.{player.level}",
            border_style="green",
            width=46,
        )

        console.print(Columns([enemy_panel, player_panel]))

        if self.log:
            for line in self.log[-5:]:
                console.print(f"  {line}")
        console.print()

    def add_log(self, msg: str):
        self.log.append(msg)

    def clear_log(self):
        self.log.clear()

    # ── Combat menu ────────────────────────────────────────────────────────────

    def show_combat_menu(self, player) -> str:
        from game.combat import SPELLS
        spells = list(SPELLS.get(player.player_class, {}).keys())

        console.print(f"[bold yellow]{t('actions_header')}[/bold yellow]")
        console.print(f"  [cyan]1.[/cyan] {t('action_attack')}")
        for i, spell in enumerate(spells):
            cost = SPELLS[player.player_class][spell]["cost"]
            has_mp = player.mp >= cost
            if has_mp:
                console.print(f"  [blue]{i+2}.[/blue] {spell}  [dim](MP: {cost})[/dim]")
            else:
                console.print(f"  [dim]{i+2}.[/dim] {spell}  [dim](MP: {cost}) (Not enough MP)[/dim]")
        item_num = 2 + len(spells)
        console.print(f"  [green]{item_num}.[/green] {t('action_use_item')}  [dim]({len(player.inventory)})[/dim]")

        while True:
            choice = self.input(t("action_prompt", n=item_num))
            if choice.isdigit():
                choice_int = int(choice)
                if choice_int == 1:  # Attack
                    return choice
                elif 2 <= choice_int < 2 + len(spells):  # Spell
                    spell_idx = choice_int - 2
                    spell = spells[spell_idx]
                    cost = SPELLS[player.player_class][spell]["cost"]
                    if player.mp >= cost:
                        return choice
                    else:
                        console.print(f"[red]{t('not_enough_mp')}[/red]")
                        continue
                elif choice_int == item_num:  # Items
                    return choice
            console.print(t("invalid"))

    # ── Inventory ──────────────────────────────────────────────────────────────

    def show_inventory(self, player) -> int:
        if not player.inventory:
            console.print(t("no_items"))
            return -1
        console.print(t("inventory_header"))
        for i, item in enumerate(player.inventory):
            console.print(f"  [cyan]{i+1}.[/cyan] {item.name} — {item.description}")
        console.print(t("cancel_option"))
        while True:
            choice = self.input(t("use_item_prompt"))
            if choice == "0":
                return -1
            if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
                return int(choice) - 1
            console.print(t("invalid"))

    # ── Floor ─────────────────────────────────────────────────────────────────

    def show_floor(self, floor: int, max_floors: int):
        self.clear()
        subtitle = t("floor_final_subtitle") if floor == max_floors else t("floor_subtitle")
        console.print(Panel(
            f"[bold yellow]{t('floor_label', floor=floor, max=max_floors)}[/bold yellow]",
            subtitle=subtitle,
            border_style="yellow",
        ))

    # ── Story events ───────────────────────────────────────────────────────────

    def show_story_event(self, event) -> int:
        """Display the story event and return chosen index (0-based)."""
        self.clear()
        console.print(Panel(
            f"[italic]{t(event.narrative)}[/italic]",
            title=f"[bold yellow]{t(event.title)}[/bold yellow]",
            border_style="yellow",
            padding=(1, 2),
        ))
        console.print()
        for i, choice in enumerate(event.choices, 1):
            console.print(f"  [cyan]{i}.[/cyan] {t(choice.text)}")
        console.print()
        while True:
            c = self.input(t("story_choice_prompt", n=len(event.choices)))
            if c.isdigit() and 1 <= int(c) <= len(event.choices):
                idx = int(c) - 1
                chosen = event.choices[idx]
                console.print(f"\n[italic dim]{t(chosen.outcome)}[/italic dim]")
                return idx
            console.print(t("invalid"))

    # ── End screens ────────────────────────────────────────────────────────────

    def show_game_over(self, player):
        self.clear()
        console.print(Panel(
            f"[bold red]{t('game_over')}[/bold red]\n\n"
            f"[italic]{t('player_fallen', name=player.name)}[/italic]\n\n"
            f"{t('reached_level')} [bold]{player.level}[/bold]\n"
            f"{t('gold_collected')} [yellow]{player.gold}[/yellow]",
            title=f"[bold]{t('defeated_title')}[/bold]",
            border_style="red",
        ))

    def show_victory(self, player, ending: dict = None):
        self.clear()
        if ending:
            console.print(Panel(
                f"[bold yellow]★  {t(ending['title'])}  ★[/bold yellow]\n\n"
                f"[italic]{t(ending['description'])}[/italic]\n\n"
                f"[dim]{t('final_level')} {player.level}   {t('gold_label')} {player.gold}[/dim]",
                title=f"[bold]{t('dungeon_cleared')}[/bold]",
                border_style="yellow",
                padding=(1, 2),
            ))
        else:
            console.print(Panel(
                f"[bold yellow]{t('victory')}[/bold yellow]\n\n"
                f"[italic]{t('slain_dragon', name=player.name)}[/italic]\n\n"
                f"{t('final_level')} [bold]{player.level}[/bold]\n"
                f"{t('gold_label')} [yellow]{player.gold}[/yellow]",
                title=f"[bold]{t('dungeon_cleared')}[/bold]",
                border_style="yellow",
            ))
