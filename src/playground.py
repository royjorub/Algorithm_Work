import string


def algo_02(sentence):
    """
    For a given sentence, return the average word length.
    Note: Remember to remove punctuation first.
    :param sentence:
    :return:
    """
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()

    return round(sum(len(word) for word in words) / len(words), 2)


def algo_02_b(sentence):
    """
    For a given sentence, return the average word length.
    Note: Remember to remove punctuation first.
    :param sentence:
    :return:
    """
    for p in string.punctuation:
        sentence = sentence.replace(p, '')
    words = sentence.split()

    return round(sum(len(word) for word in words) / len(words), 2)


def my_algo_02_a(sentence):
    """
    For a given sentence, return the average word length.
    Note: Remember to remove punctuation first.
    :param sentence:
    :return:
    """
    _skip = string.punctuation + string.whitespace

    words = []
    word_len_sum = 0
    word_count = 0

    _tmp_word = ''
    for c in sentence:
        # iterate each character in the sentence
        if c not in _skip:
            # if it is not in the skip list, i want to keep it
            _tmp_word += c
        elif c in string.whitespace:
            # otherwise if it is a whitespace, we are done with this word
            # so we add the word to our list of words and its len to our sum of word lens
            # and then we reset the word

            # words.append(_tmp_word)
            word_count += 1

            word_len_sum += len(_tmp_word)
            _tmp_word = ''

    return round(word_len_sum / word_count, 2)


cleanup_all = str.maketrans({p: '' for p in string.punctuation})


def my_algo_02_b(sentence):
    """
    For a given sentence, return the average word length.
    Note: Remember to remove punctuation first.
    :param sentence:
    :return:
    """

    word_len_sum = 0
    word_count = 1 if len(sentence) else 0

    for c in sentence.translate(cleanup_all):
        if c in string.whitespace:
            word_count += 1
        else:
            word_len_sum += 1

    return round(word_len_sum / word_count, 2)


cleanup_short = str.maketrans({p: None for p in "!?',;."})


def my_algo_02_c(sentence):
    """
    For a given sentence, return the average word length.
    Note: Remember to remove punctuation first.
    :param sentence:
    :return:
    """
    words = sentence.translate(cleanup_short).split()
    return round(sum(len(word) for word in words) / len(words), 2)


def my_algo_02_d(sentence):
    words = sentence.translate(cleanup_all).split()
    return round(sum(len(word) for word in words) / len(words), 2)


text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

import timeit
import functools


def efficiency_test(x=1, y=100):
    my_ta = timeit.Timer(functools.partial(my_algo_02_a, text * x))
    my_tb = timeit.Timer(functools.partial(my_algo_02_b, text * x))
    my_tc = timeit.Timer(functools.partial(my_algo_02_c, text * x))
    my_td = timeit.Timer(functools.partial(my_algo_02_d, text * x))
    orig_t = timeit.Timer(functools.partial(algo_02, text * x))
    orig_t_b = timeit.Timer(functools.partial(algo_02_b, text * x))

    # print('mya', my_ta.repeat(3, y))
    # print('myb', my_tb.repeat(3, y))
    # print('myc', my_tc.repeat(3, y))
    print('myd', my_td.repeat(3, y))
    # print('orig', orig_t.repeat(3, y))
    print('origb', orig_t_b.repeat(3, y))


data_set = [
    # algorithm, data
    [
        1,
        [
            # ((input_value), expected_output)
            ([-231], -132),
            ([345], 543)
        ]
    ],
    [
        2,
        [
            # ((input_value), expected_output)
            (["Hi all, my name is Tom...I am originally from Australia."], 4.2),
            (["I need to work very hard to learn more about algorithms in Python!"], 4.08)
        ]
    ],
    [
        3,
        [
            # (input_value, expected_output)
            (['364', '1836'], '2200'),
        ]
    ],
    [
        4,
        [
            # (input_value, expected_output)
            (['alphabet'], 1),
            (['barbados'], 2),
            (['crunchy'], 1)
        ]
    ],
    [
        5,
        [
            # (input_value, expected_output)
            (['radkar'], True)
        ]
    ],
    [
        6,
        [
            # (input_value, expected_output)
            ([[6, 5, 4, 4]], True),
            ([[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], False),
            ([[1, 1, 2, 3, 7]], True)
        ]
    ],
    [
        7,
        [
            # (input_value, expected_output)
            ([[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
            ([[1, 7, 0, 0, 8, 0, 10, 12, 0, 4]], [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])
        ]
    ],
    [
        8,
        [
            # (input_value, expected_output)
            ([[1, None, 2, 3, None, None, 5, None]], [1, 1, 2, 3, 3, 3, 5, 5])
        ]
    ],
    [
        9,
        [
            # (input_value, expected_output)
            (['We are really pleased to meet you in our city', 'The city was hit by a really heavy storm'],
             (['The', 'We', 'a', 'are', 'by', 'heavy', 'hit', 'in', 'meet', 'our', 'pleased', 'storm', 'to', 'was',
               'you'],
              ['city', 'really']))
        ]
    ],
    [
        10,
        [
            # (input_value, expected_output)
            ([35], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        ]
    ],
]

data_map = {k: v for k, v in data_set}


def algo_03(num1, num2):
    """
    Given a string of length one, the ord()
    function returns an integer representing the Unicode code point of the character
    when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

    :param num1, num2:
    :return:
    """
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1 // 10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)


def my_algo_03(num1, num2):
    """
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Notes:
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.

    :param num1, num2:
    :return:
    """
    pass


import collections


def algo_04a(s):
    """
    Given a string, find the first non-repeating character in it and return its index.
    If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
    """
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1


# Approach 2
# import collections - at top of page and on test file

def algo_04b(s):
    count = collections.Counter(s)
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


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


fun_string = "i once ate a pickle, it was yummy!"


def friends_and_enemies(x=1, y=100):
    mine = timeit.Timer(functools.partial(my_algo_04, fun_string * x))
    orig_a = timeit.Timer(functools.partial(algo_04a, fun_string * x))
    orig_b = timeit.Timer(functools.partial(algo_04b, fun_string * x))

    print('mine', mine.repeat(3, y))
    print('origa', orig_a.repeat(3, y))
    print('origb', orig_b.repeat(3, y))


# given two dictionaries:
# a: create a new dictionary which contains all the items that are identical in both (key+value)
# b: create a new dictionary which contains all the items that are not found in both
# pay close attention, you could have the same key in both with different values - how do you resolve this?
# useful tip: symmetric difference

# take a look at collection.OrderedDict can you implement your own ordered dictionary?
