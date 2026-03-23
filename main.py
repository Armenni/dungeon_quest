from game.i18n import set_language, t
from game.ui import UI
from game.player import Player
from game.dungeon import Dungeon
from game.save import load_game, delete_save, restore_player


def main():
    lang_prompt = "Select language / Selecione o idioma:\n  1. English\n  2. Português (BR)\n> "
    while True:
        lang_choice = input(lang_prompt).strip()
        if lang_choice in ("1", "2"):
            break
        print("Invalid choice. Please enter 1 or 2. / Escolha inválida. Digite 1 ou 2.")

    if lang_choice == "2":
        set_language("pt_br")
    else:
        set_language("en")

    ui = UI()
    ui.show_title()

    # Check for existing save
    save_data = load_game()
    if save_data:
        while True:
            choice = ui.input(t("save_prompt")).strip().lower()
            if choice == t("save_continue_cmd"):
                player = restore_player(save_data)
                floor = save_data["floor"]
                ui.print(f"[bold cyan]{t('save_loaded', name=player.name)}[/bold cyan]")
                ui.pause()
                dungeon = Dungeon(player, ui)
                dungeon.floor = floor
                dungeon.run()
                return
            elif choice == t("save_new_cmd"):
                delete_save()
                break

    name = ui.input(t("enter_name"))
    if not name:
        name = t("default_name")

    ui.print()
    player_class = ui.choose_class()

    player = Player(name, player_class)
    dungeon = Dungeon(player, ui)
    dungeon.run()


if __name__ == "__main__":
    main()
