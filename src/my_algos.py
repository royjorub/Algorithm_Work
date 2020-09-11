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


def my_algo_04(s):
    alone = {}
    friends = []

    for idx, c in enumerate(s):
        if c in friends:
            continue
        elif c in alone:
            friends.append(c)
            alone.pop(c)
        else:
            alone[c] = idx

    def sorter(t):
        return t[-1]

    if not alone:
        return -1
    else:
        sorted_loners = sorted(alone.items(), key=sorter)
        first_loner = sorted_loners[0]
        return first_loner[-1]

