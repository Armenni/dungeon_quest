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

    # Track bought items per floor to prevent repurchasing
    if not hasattr(player, "_shop_bought"):
        player._shop_bought = {}
    if floor not in player._shop_bought:
        player._shop_bought[floor] = set()
    bought_keys = player._shop_bought[floor]

    while True:
        ui.clear()
        _show_shop(ui, player, stock, bought_keys)
        choice = ui.input(t("shop_prompt")).strip().lower()

        if choice == t("shop_leave_cmd"):
            break

        if choice == t("shop_sell_cmd"):
            if not _run_sell_mode(player, ui):
                break
            continue

        if not choice.isdigit():
            ui.print(t("invalid"))
            ui.pause(t("press_enter_short"))
            continue

        idx = int(choice) - 1
        items_list = _build_item_list(stock, bought_keys)

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
        bought_keys.add(key)

        if kind == "item":
            player.inventory.append(ITEMS[key])
            ui.print(f"[green]{t('bought_item', name=ITEMS[key].name)}[/green]")
        elif kind == "equip":
            eq = EQUIPMENT[key]
            msg = player.equip(eq)
            ui.print(f"[green]{msg}[/green]")

        ui.pause(t("press_enter_shopping"))


def _build_sell_list(player: Player) -> list[tuple[str, any, str, int]]:
    """Returns [(kind, ref, name, sell_price), ...] for sellable items."""
    result = []
    for i, item in enumerate(player.inventory):
        if item.price > 0:
            result.append(("inv", i, item.name, item.price // 2))
    if player.weapon and player.weapon.price > 0:
        result.append(("weapon", None, player.weapon.name, player.weapon.price // 2))
    if player.armor and player.armor.price > 0:
        result.append(("armor", None, player.armor.name, player.armor.price // 2))
    return result


def _run_sell_mode(player: Player, ui) -> bool:
    """Run sell mode. Returns True to return to buy mode, False to exit."""
    from rich import box
    from rich.panel import Panel
    from game.ui import console

    sell_list = _build_sell_list(player)
    if not sell_list:
        ui.print(t("sell_nothing"))
        ui.pause(t("press_enter_short"))
        return False

    ui.clear()
    console.print(Panel(
        f"[bold yellow]{t('sell_mode_header')}[/bold yellow]",
        border_style="yellow",
    ))
    for i, (kind, ref, name, price) in enumerate(sell_list, 1):
        equipped_tag = " [dim](equipped)[/dim]" if kind in ("weapon", "armor") else ""
        console.print(f"  {t('sell_item_line', n=i, name=name, price=price)}{equipped_tag}")
    console.print(t("cancel_option"))

    choice = ui.input(t("shop_sell_prompt")).strip().lower()

    if choice == t("shop_leave_cmd"):
        return False

    if choice == t("shop_buy_cmd"):
        return True

    if choice == "0" or not choice.isdigit():
        ui.print(t("sell_cancel"))
        ui.pause(t("press_enter_short"))
        return True

    idx = int(choice) - 1
    if not (0 <= idx < len(sell_list)):
        ui.print(t("invalid"))
        ui.pause(t("press_enter_short"))
        return True

    kind, ref, name, price = sell_list[idx]
    confirm = ui.input(t("sell_confirm", name=name, price=price)).strip().lower()
    if confirm != t("sell_confirm_cmd"):
        ui.print(t("sell_cancel"))
        ui.pause(t("press_enter_short"))
        return True

    player.gold += price
    if kind == "inv":
        player.inventory.pop(ref)
    elif kind == "weapon":
        player.unequip("weapon")
    elif kind == "armor":
        player.unequip("armor")

    ui.print(f"[green]{t('sold_item', name=name, price=price)}[/green]")
    ui.pause(t("press_enter_short"))
    return True


def _build_item_list(stock: dict, bought_keys: set = None) -> list[tuple[str, str, int]]:
    """Returns list of (kind, key, price) for all shop entries not yet bought."""
    if bought_keys is None:
        bought_keys = set()
    result = []
    for key, price in POTION_SHOP:
        if key not in bought_keys:
            result.append(("item", key, price))
    for key in stock.get("weapons", []):
        if key not in bought_keys:
            eq = EQUIPMENT[key]
            result.append(("equip", key, eq.price))
    for key in stock.get("armors", []):
        if key not in bought_keys:
            eq = EQUIPMENT[key]
            result.append(("equip", key, eq.price))
    return result


def _show_shop(ui, player: Player, stock: dict, bought_keys: set = None):
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    from game.ui import console

    if bought_keys is None:
        bought_keys = set()

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold yellow")
    table.add_column("#",    style="cyan",  width=3)
    table.add_column("Item", style="white", width=24)
    table.add_column("Description",          width=28)
    table.add_column("Price", style="yellow", width=7)

    items_list = _build_item_list(stock, bought_keys)
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
