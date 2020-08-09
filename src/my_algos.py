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
