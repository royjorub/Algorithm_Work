import pytest
from src import algo_work
import collections


class TestOriginal:

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            [-231, -132],
            [345, 543],
        ]
    )
    def test_algo_01(self, input_value, expected_value):
        assert algo_work.algo_01(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            ["Hi all, my name is Tom...I am originally from Australia.", 4.2],
            ["I need to work very hard to learn more about algorithms in Python!", 4.08]
        ]
    )
    def test_algo_02(self, input_value, expected_value):
        assert algo_work.algo_02(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value_1', 'input_value_2', 'expected_value'],
        argvalues=[
            ['364', '1836', 2200]
        ]
    )
    def test_algo_03a(self, input_value_1, input_value_2, expected_value):
        assert algo_work.algo_03a(input_value_1, input_value_2) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value_1', 'input_value_2', 'expected_value'],
        argvalues=[
            ['364', '1836', 2200]
        ]
    )
    def test_algo_03b(self, input_value_1, input_value_2, expected_value):
        assert algo_work.algo_03b(input_value_1, input_value_2) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            ['alphabet', 1],
            ['barbados', 2],
            ['crunchy', 1],
        ]
    )
    def test_algo_04a(self, input_value, expected_value):
        assert algo_work.algo_04a(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            ['alphabet', 1],
            ['barbados', 2],
            ['crunchy', 1],
        ]
    )
    def test_algo_04b(self, input_value, expected_value):
        assert algo_work.algo_04b(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            ['radkar', True],
        ]
    )
    def test_algo_05(self, input_value, expected_value):
        assert algo_work.algo_05(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            [[6, 5, 4, 4], True],
            [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], False],
            [[1, 1, 2, 3, 7], True],
        ]
    )
    def test_algo_06(self, input_value, expected_value):
        assert algo_work.algo_06(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
            [[1, 7, 0, 0, 8, 0, 10, 12, 0, 4], [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]],
        ]
    )
    def test_algo_07(self, input_value, expected_value):
        assert algo_work.algo_07(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value', 'expected_value'],
        argvalues=[
            [[1, None, 2, 3, None, None, 5, None], [1, 1, 2, 3, 3, 3, 5, 5]],
        ]
    )
    def test_algo_08(self, input_value, expected_value):
        assert algo_work.algo_08(input_value) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value_1','input_value_2', 'expected_value'],
        argvalues=[
            ['We are really pleased to meet you in our city', 'The city was hit by a really heavy storm', (['The','We','a','are','by','heavy','hit','in','meet','our','pleased','storm','to','was','you'],['city', 'really'])],
        ]
    )
    def test_algo_09(self, input_value_1, input_value_2, expected_value):
        assert algo_work.algo_09(input_value_1,input_value_2) == expected_value

    @pytest.mark.parametrize(
        argnames=['input_value_1', 'expected_value'],
        argvalues=[
            [35, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]],
        ]
    )
    def test_algo_10(self, input_value, expected_value):
        assert algo_work.algo_10(input_value) == expected_value


class TestFailOnPurpose:

    def test_algo_01_with_bad_input(self):
        with pytest.raises(ValueError):
            algo_work.algo_01('asdlkajsd')
