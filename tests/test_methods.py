from __future__ import annotations

from autoCase import camel, snake, kebab, title
from autoCase.wordSplitter import SnakeSplitter

camel_test = [
    ("game_engine_server_services_module_base", "gameEngineServerServicesModuleBase"),
    ("game_engIne_server_services_module_base", "gameEngIneServerServicesModuleBase"),
    ("game_engIne_ser-ver_services_module_base", "gameEngIneSerVerServicesModuleBase"),
    ("hiThere", "hiThere"),
    ("hey There", "heyThere"),
    ("hey there", "heyThere"),
    ("hey;There", "heyThere"),
    ("hi123", "hi123"),
    ("hi_123", "hi123"),
    ("hi_123_tHere", "hi123THere"),
    ("hi__", "hi"),
    ("_hi", "hi"),
    ("_hi_", "hi"),
    ("_hi_there", "hiThere"),
    ("_hi__there", "hiThere"),
    ("_hi_123_there", "hi123There"),
    ("_hi_123_there_", "hi123There"),
    ("_hi_123_there_123", "hi123There123"),
    ("_hi_123_tHerRe_123_", "hi123THerRe123"),
]
camel_from_snake = [
    ("game_engine_server_services_module_base", "gameEngineServerServicesModuleBase"),
    ("game_engIne_server_services_module_base", "gameEngIneServerServicesModuleBase"),
    ("game_engIne_ser-ver_services_module_base", "gameEng-IneSer-verServicesModuleBase"),
    ("hi_there", "HiThere"),
    ("hey_there", "HeyThere"),
    ("hi123", "Hi123"),
    ("hi_123", "Hi123"),
    ("hi_123_tHere", "Hi123THere"),
    ("hi__", "Hi"),
    ("_hi", "Hi"),
    ("_hi_", "Hi"),
    ("_hi_there", "HiThere"),
    ("_hi__there", "HiThere"),
    ("_hi_123_there", "Hi123There"),
    ("_hi_123_there_", "Hi123There"),
    ("_hi_123_there_123", "Hi123There123"),
    ("_hi_123_tHerRe_123_", "Hi123THerRe123"),
]


def test_camel():
    """
    This defines the expected usage, which can then be used in various test cases.
    Pytest will not execute this code directly, since the function does not contain the suffex "test"
    """
    for test in camel_test:
        assert camel(test[0]) == test[1]


def test_camel_from_snake():
    for test in camel_from_snake:
        assert (
            camel(test[0], splitter=SnakeSplitter) == test[1]
        ), f"Failed for {test[0]}, expected {test[1]} but got {camel(test[0], splitter=SnakeSplitter)}"


test_camel_from_snake()
