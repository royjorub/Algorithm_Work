import pytest

from src import algo_work


class TestOriginalDataSet:
    data_set = [
        # algorithm, data
        [
            algo_work.algo_01,
            [
                # ((input_value), expected_output)
                ([-231], -132),
                ([345], 543)
            ]
        ],
        [
            algo_work.algo_03a,
            [
                # (input_value, expected_output)
                (['364', '1836'], '2200'),
            ]
        ],
    ]

    @pytest.mark.parametrize(argnames=['algorithm', 'test_data'], argvalues=data_set)
    def test_original_algorithm(self, algorithm, test_data):
        for input_data, expected_output in test_data:
            assert algorithm(*input_data) == expected_output