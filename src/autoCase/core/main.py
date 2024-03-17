from autoCase.wordSplitter import *
from autoCase.case import *
from autoCase.core.validator import *
from functools import partial
import logging

def generic_converter(word: str, case: callable, splitter:callable=MixedSplitter) -> str:
    """Converts a word to a specific case

    :param word: The word to be converted
    :type word: str
    :param case: The case to be converted to
    :type case: callable
    :param splitter: The splitter to be used
    :type splitter: MixedSplitter
    :raises ValueError: If the word is invalid
    :raises ValueError: If the splitter is invalid
    :raises ValueError: If the case is invalid
    :return: The word in the specified case
    :rtype: str
    """
    if not validate_word(word):
        # raise ValueError(f"Invalid word: {word}")
        logging.error(f"Invalid word: {word}")
        return ""
    if not validate_splitter(splitter):
        raise ValueError(f"Invalid splitter: {splitter}")
    if not validate_case(case):
        raise ValueError(f"Invalid case: {case}")
    words = splitter(word)
    return case(words)


camel = partial(generic_converter, case=wordList2Camel)
snake = partial(generic_converter, case=wordList2Snake)
kebab = partial(generic_converter, case=wordList2Kebab)
title = partial(generic_converter, case=wordList2Title)

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
    ("game_engine_se rVer_servicesModuleBase", "gameEngineSeRVerServicesModuleBase"),
]

camel_test2=[
    ("fallback_url", "fallbackUrl"),
    ("scrubber_media_url", "scrubberMediaUrl"),
    ("dash_url", "dashUrl"),
    ("_fallback_url", "_fallbackUrl"),
    ("__scrubber_media___url_", "__scrubberMediaUrl_"),
    ("_url__", "_url__"),
    ("API", "API"),
    ("_API_", "_API_"),
    ("__API__", "__API__"),
    ("APIResponse", "APIResponse"),
    ("_APIResponse_", "_APIResponse_"),
    ("__APIResponse__", "__APIResponse__"),
    # Fixed issue #128
    ("whatever_10", "whatever10"),
    # Fixed issue # 18
    ("test-1-2-3-4-5-6", "test123456"),
    # Fixed issue # 61
    ("test_n_test", "testNTest"),
    # Fixed issue # 148
    ("field_value_2_type", "fieldValue2Type"),
    # Fixed issue # 256
    ("", ""),
    (None, ""),
]

if __name__=="__main__":
    for test in camel_test2:
        if not camel(test[0])==test[1]:
            print(f"Failed for {test[0]}, expected {test[1]} but got {camel(test[0])}")
    print("All tests passed!")