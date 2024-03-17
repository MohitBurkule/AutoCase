def wordList2Camel(words: list[str]) -> str:
    """
    This function is used to convert a list of words into camel case.

    :return:
    """
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    return words[0] + "".join([word.capitalize() for word in words[1:]])


def wordList2Pascal(words: list[str]) -> str:
    """
    This function is used to convert a list of words into pascal case.

    :return:
    """
    words = wordList2Camel(words)
    return words.capitalize()


def wordList2Kebab(words: list[str]) -> str:
    """
    This function is used to convert a list of words into kebab case.

    :return:
    """
    #words = [word.lower() for word in words]
    return "-".join(words)


def wordList2Snake(words: list[str]) -> str:
    """
    This function is used to convert a list of words into snake case.

    :return:
    """
    #words = [word.lower() for word in words]
    return "_".join(words)


def wordList2Title(words: list[str]) -> str:
    """
    This function is used to convert a list of words into title case.

    :return:
    """
    #words = [word.lower() for word in words]
    return " ".join(words)
