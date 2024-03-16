from autoCase.wordSplitter import *
from autoCase.case import *
from autoCase.core.validator import *
from functools import partial


def generic_converter(word: str, case: callable, splitter: MixedSplitter) -> str:
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
        raise ValueError(f"Invalid word: {word}")
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
