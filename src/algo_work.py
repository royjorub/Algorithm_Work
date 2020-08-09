# taken from https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
import collections


def algo_01(x):
    """
    Given an integer, return the integer with reversed digits.
    Note: The integer could be either positive or negative.
    :param x:
    :return:
    """
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


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


def algo_03a(num1, num2):
    """
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Notes:
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.

    :param num1, num2:
    :return:
    """
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))


def algo_03b(num1, num2):
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


def algo_05(s):
    """
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    The string will only contain lowercase characters a-z.
    """
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if t == t[::-1]:
            return True

    return s == s[::-1]


def algo_06(nums):
    """
    Given an array of integers, determine whether the array is monotonic or not.
    """
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


def algo_07(nums):
    """
    Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
    the non-zero elements.
    """
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums


def algo_08(array):
    """
    Given an array containing None values fill in the None values with most recent
    non None value in the array
    """
    valid = 0
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res


def algo_09(sentence1, sentence2):
    """
    Given two sentences, return an array that has the words that appear in one sentence and not
    the other and an array with the words in common.
    """
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))  # ^ A.symmetric_difference(B), & A.intersection(B)


def algo_10(n):
    """
    Given k numbers which are less than n, return the set of prime number among them
    Note: The task is to write a program to print all Prime numbers in an Interval.
    Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    prime_nums = []
    for num in range(n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    # if the modulus == 0 is means that the number can be divided by a number preceding it
                    break
            else:
                prime_nums.append(num)
    return prime_nums
