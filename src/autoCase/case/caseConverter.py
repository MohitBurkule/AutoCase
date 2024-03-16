
def camelCase(words: list[str]) -> str:
    """
    This function is used to convert a list of words into camel case.

    :return:
    """
    return words[0] + ''.join([word.capitalize() for word in words[1:]])

def kebabCase(words: list[str]) -> str:
    """
    This function is used to convert a list of words into kebab case.

    :return:
    """
    words = [word.lower() for word in words]
    return '-'.join(words)

def snakeCase(words: list[str]) -> str:
    """
    This function is used to convert a list of words into snake case.

    :return:
    """
    words = [word.lower() for word in words]
    return '_'.join(words)

def titleCase(words: list[str]) -> str:
    """
    This function is used to convert a list of words into title case.

    :return:
    """
    words = [word.lower() for word in words]
    return ' '.join(words)