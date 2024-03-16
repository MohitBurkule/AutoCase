def CamelSplitter(word: str) -> list:
    """
    This function is used to split camel case words into a list of words.

    :return:
    """
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
    word = list(word)
    words = []
    temp = ''
    for i in range(len(word)):
        if word[i] in alphabets:
            if temp:
                words.append(temp)
            temp = word[i]
        else:
            temp += word[i]
    words.append(temp)
    return words

def SnakeSplitter(word: str) -> list:
    """
    This function is used to split snake case words into a list of words.

    :return:
    """
    return word.split('_')

def KebabSplitter(word: str) -> list:
    """
    This function is used to split kebab case words into a list of words.

    :return:
    """
    return word.split('-')

def TitleSplitter(word: str) -> list:
    """
    This function is used to split titled case words into a list of words.

    :return:
    """
    return word.split(' ')

if __name__ == "__main__":
    for test in camel_split_tests:
        print(CamelSplitter(test[0]) == test[1])