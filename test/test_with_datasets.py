import pytest

from src import algo_work, my_algos

orig_algos = {
    1: [algo_work.algo_01],
    2: [algo_work.algo_02],
    3: [algo_work.algo_03a, algo_work.algo_03b],
    4: [algo_work.algo_04a, algo_work.algo_04b],
    5: [algo_work.algo_05],
    6: [algo_work.algo_06],
    7: [algo_work.algo_07],
    8: [algo_work.algo_08],
    9: [algo_work.algo_09],
    10: [algo_work.algo_10],

}
my_algos = {
    1: [my_algos.my_algo_01],
    2: [my_algos.my_algo_02],
    3: [my_algos.my_algo_04],
}

original_data_map = {
    1: [([-231], -132), ([345], 543)],
    2: [(['Hi all, my name is Tom...I am originally from Australia.'], 4.2),
        (['I need to work very hard to learn more about algorithms in Python!'], 4.08)],
    3: [(['364', '1836'], '2200')],
    4: [(['alphabet'], 1), (['barbados'], 2), (['crunchy'], 1)], 5: [(['radkar'], True)],
    6: [([[6, 5, 4, 4]], True), ([[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], False), ([[1, 1, 2, 3, 7]], True)],
    7: [([[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
        ([[1, 7, 0, 0, 8, 0, 10, 12, 0, 4]], [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])],
    8: [([[1, None, 2, 3, None, None, 5, None]], [1, 1, 2, 3, 3, 3, 5, 5])],
    9: [(['We are really pleased to meet you in our city',
          'The city was hit by a really heavy storm'],
         (['The', 'We', 'a', 'are',
           'by', 'heavy', 'hit', 'in',
           'meet', 'our', 'pleased',
           'storm', 'to', 'was',
           'you'],
          ['city', 'really']))],
    10: [([35], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])]}


class TestOriginalDataSet:

    def helper_run_algorithm(self, algorithm,  data):
        failures = []
        for idx, (input_data, expected_output) in enumerate(data):
            output = algorithm(*input_data)
            if not output == expected_output:
                failures.append((idx, output, expected_output))
        return failures

    def test_original_algorithm(self):
        for algorithm_id, algorithms in orig_algos.items():
            for algorithm in algorithms:
                failures = self.helper_run_algorithm(algorithm, original_data_map[algorithm_id])
                assert not failures, f"{algorithm}: {failures}"

    def test_my_algorithm(self):
        for algorithm_id, algorithms in my_algos.items():
            for algorithm in algorithms:
                failures = self.helper_run_algorithm(algorithm, original_data_map[algorithm_id])
                assert not failures, f"{algorithm}: {failures}"
