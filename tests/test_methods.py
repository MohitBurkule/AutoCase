"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

from autoCase import camel, snake, kebab, title

camel_test=[
    ("game_engine_server_services_module_base", "gameEngineServerServicesModuleBase"),
    ("hiThere", "hiThere"),
    ("hi123", "hi123"),
    ("hi_123", "hi123"),
    ("hi_123_there", "hi123There"),
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


def test_camel_test():
    """
    This defines the expected usage, which can then be used in various test cases.
    Pytest will not execute this code directly, since the function does not contain the suffex "test"
    """
    for test in camel_test:
        assert camel(test[0]) == test[1]


def test_hello(unit_test_mocks: None):
    """
    This is a simple test, which can use a mock to override online functionality.
    unit_test_mocks: Fixture located in conftest.py, implictly imported via pytest.
    """
    pass#hello_test()


def test_int_hello():
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    pass#hello_test()
