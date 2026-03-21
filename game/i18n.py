import importlib

_lang: dict = {}


def set_language(lang: str) -> None:
    global _lang
    module = importlib.import_module(f"game.lang.{lang}")
    _lang = module.STRINGS


def t(key: str, **kwargs) -> str:
    value = _lang.get(key, key)
    if kwargs:
        return value.format(**kwargs)
    return value
