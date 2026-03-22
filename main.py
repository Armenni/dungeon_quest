from game.i18n import set_language, t
from game.ui import UI
from game.player import Player
from game.dungeon import Dungeon


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
