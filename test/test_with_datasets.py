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
            algo_work.algo_02,
            [
                # ((input_value), expected_output)
                (["Hi all, my name is Tom...I am originally from Australia."], 4.2),
                (["I need to work very hard to learn more about algorithms in Python!"], 4.08)
            ]
        ],
        [
            algo_work.algo_03a,
            [
                # (input_value, expected_output)
                (['364', '1836'], '2200'),
            ]
        ],
        [
            algo_work.algo_03b,
            [
                # (input_value, expected_output)
                (['364', '1836'], '2200'),
            ]
        ],
        [
            algo_work.algo_04a,
            [
                # (input_value, expected_output)
                (['alphabet'], 1),
                (['barbados'], 2),
                (['crunchy'], 1)
            ]
        ],
        [
            algo_work.algo_04b,
            [
                # (input_value, expected_output)
                (['alphabet'], 1),
                (['barbados'], 2),
                (['crunchy'], 1)
            ]
        ],
        [
            algo_work.algo_05,
            [
                # (input_value, expected_output)
                (['radkar'], True)
            ]
        ],
        [
            algo_work.algo_06,
            [
                # (input_value, expected_output)
                ([[6, 5, 4, 4]], True),
                ([[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], False),
                ([[1, 1, 2, 3, 7]], True)
            ]
        ],
        [
            algo_work.algo_07,
            [
                # (input_value, expected_output)
                ([[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
                ([[1, 7, 0, 0, 8, 0, 10, 12, 0, 4]], [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])
            ]
        ],
        [
            algo_work.algo_08,
            [
                # (input_value, expected_output)
                ([[1, None, 2, 3, None, None, 5, None]], [1, 1, 2, 3, 3, 3, 5, 5])
            ]
        ],
        [
            algo_work.algo_09,
            [
                # (input_value, expected_output)
                (['We are really pleased to meet you in our city', 'The city was hit by a really heavy storm'],
                 [(['The', 'We', 'a', 'are', 'by', 'heavy', 'hit', 'in', 'meet', 'our', 'pleased', 'storm', 'to', 'was',
                   'you'],
                  ['city', 'really'])])
            ]
        ],
        [
            algo_work.algo_10,
            [
                # (input_value, expected_output)
                ([35], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
            ]
        ],
    ]

    @pytest.mark.parametrize(argnames=['algorithm', 'test_data'], argvalues=data_set)
    def test_original_algorithm(self, algorithm, test_data):
        for input_data, expected_output in test_data:
            assert algorithm(*input_data) == expected_output