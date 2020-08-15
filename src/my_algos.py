import string


def my_algo_01(x):
    """
    Given an integer, return the integer with reversed digits.
    Note: The integer could be either positive or negative.
    :param x:
    :return:
    """
    y = str(x)
    if x < 0:
        return int(f"-{y[:0:-1]}")
    else:
        return int(y[::-1])


cleanup_all = str.maketrans({p: '' for p in string.punctuation})


def my_algo_02(sentence):
    words = sentence.translate(cleanup_all).split()
    return round(sum(len(word) for word in words) / len(words))
