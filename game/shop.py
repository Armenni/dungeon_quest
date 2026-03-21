from game.player import Player
from game.items import ITEMS
from game.equipment import EQUIPMENT, SHOP_STOCK, POTION_SHOP
from game.i18n import t


def run_shop(player: Player, ui) -> None:
    """Run the shop loop for the current floor."""
    floor = getattr(player, "_shop_floor", 1)
    stock = SHOP_STOCK.get(floor, SHOP_STOCK[4])

    # Merchant refuses to sell weapons to someone who looted the village
    if player.story_flags.get("looted_village") and stock.get("weapons"):
        ui.print(f"\n[red]{t('shop_weapons_locked')}[/red]\n")
        stock = {"weapons": [], "armors": stock.get("armors", [])}

    while True:
        ui.clear()
        _show_shop(ui, player, stock)
        choice = ui.input(t("shop_prompt")).strip().lower()

        if choice == "l":
            break

        if not choice.isdigit():
            ui.print(t("invalid"))
            ui.pause(t("press_enter_short"))
            continue

        idx = int(choice) - 1
        items_list = _build_item_list(stock)

        if not (0 <= idx < len(items_list)):
            ui.print(t("invalid"))
            ui.pause(t("press_enter_short"))
            continue

        kind, key, price = items_list[idx]

        if player.gold < price:
            ui.print(f"[red]{t('not_enough_gold', gold=player.gold)}[/red]")
            ui.pause(t("press_enter_short"))
            continue

        player.gold -= price

        if kind == "item":
            player.inventory.append(ITEMS[key])
            ui.print(f"[green]{t('bought_item', name=ITEMS[key].name)}[/green]")
        elif kind == "equip":
            eq = EQUIPMENT[key]
            msg = player.equip(eq)
            ui.print(f"[green]{msg}[/green]")

        ui.pause(t("press_enter_shopping"))


def _build_item_list(stock: dict) -> list[tuple[str, str, int]]:
    """Returns list of (kind, key, price) for all shop entries."""
    result = []
    for key, price in POTION_SHOP:
        result.append(("item", key, price))
    for key in stock.get("weapons", []):
        eq = EQUIPMENT[key]
        result.append(("equip", key, eq.price))
    for key in stock.get("armors", []):
        eq = EQUIPMENT[key]
        result.append(("equip", key, eq.price))
    return result


def _show_shop(ui, player: Player, stock: dict):
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    from rich.console import Console

    console = Console()

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold yellow")
    table.add_column("#",    style="cyan",  width=3)
    table.add_column("Item", style="white", width=24)
    table.add_column("Description",          width=28)
    table.add_column("Price", style="yellow", width=7)

    items_list = _build_item_list(stock)
    for i, (kind, key, price) in enumerate(items_list, 1):
        if kind == "item":
            item = ITEMS[key]
            table.add_row(str(i), item.name, item.description, f"{price}g")
        else:
            eq = EQUIPMENT[key]
            # Show what bonuses the player would gain vs current gear
            current = player.weapon if eq.slot == "weapon" else player.armor
            bonus_str = _delta_str(eq, current)
            table.add_row(str(i), f"[bold]{eq.name}[/bold] ({eq.slot})",
                          f"{eq.description}  {bonus_str}", f"{price}g")

    # Current equipment summary
    w_name = player.weapon.name if player.weapon else f"[dim]none[/dim]"
    a_name = player.armor.name  if player.armor  else f"[dim]none[/dim]"
    footer = t("shop_footer", weapon=w_name, armor=a_name, gold=player.gold)

    console.print(Panel(table, title=f"[bold]{t('merchant_title')}[/bold]",
                        subtitle=footer, border_style="yellow"))


def _delta_str(eq, current) -> str:
    """Show stat delta vs currently equipped item."""
    if current is None:
        parts = []
        if eq.atk_bonus:   parts.append(f"[green]+{eq.atk_bonus} {t('stat_atk')}[/green]")
        if eq.def_bonus:   parts.append(f"[green]+{eq.def_bonus} {t('stat_def')}[/green]")
        if eq.magic_bonus: parts.append(f"[green]+{eq.magic_bonus} {t('stat_mag')}[/green]")
        if eq.hp_bonus:    parts.append(f"[green]+{eq.hp_bonus} {t('stat_hp')}[/green]")
        return " ".join(parts)

    parts = []
    for attr, label_key in [("atk_bonus", "stat_atk"), ("def_bonus", "stat_def"),
                             ("magic_bonus", "stat_mag"), ("hp_bonus", "stat_hp")]:
        delta = getattr(eq, attr) - getattr(current, attr)
        label = t(label_key)
        if delta > 0:
            parts.append(f"[green]+{delta} {label}[/green]")
        elif delta < 0:
            parts.append(f"[red]{delta} {label}[/red]")
    return " ".join(parts) if parts else f"[dim]{t('no_change')}[/dim]"
