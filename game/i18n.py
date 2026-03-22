import importlib

_lang: dict = {}


def set_language(lang: str) -> None:
    global _lang
    ui_mod    = importlib.import_module(f"game.lang.{lang}_ui")
    story_mod = importlib.import_module(f"game.lang.{lang}_story")
    _lang = {**ui_mod.STRINGS, **story_mod.STRINGS}


def t(key: str, **kwargs) -> str:
    value = _lang.get(key, key)
    if kwargs:
        return value.format(**kwargs)
    return value
