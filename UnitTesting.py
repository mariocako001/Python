import time
import unittest
from FileOutput import FileOutput

from main import Solution


class TestSolution(unittest.TestCase):
    test_run_information = []

    def setUp(self):
        """
        starts timer for each test case
        """
        self.startTime = time.perf_counter()

    def tearDown(self):
        """
        ends timer for each test case
        prints test result to console with: name, pass/fail, and duration when teardown is called
        """
        duration = (time.perf_counter() - self.startTime) * 1000

        if hasattr(self, '_outcome'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)

        error = self.getFailures(result.errors)
        failure = self.getFailures(result.failures)
        test_result = "FAILURE"
        if not error and not failure:
            test_result = "SUCCESS"

        print('%s: %s  %.5f ms' % (self.id(), test_result, duration))
        self.test_run_information.append((self.id(), test_result, duration))

    @classmethod
    def tearDownClass(self):
        """
        prints all test result to file with: name, pass/fail, and duration when tearDownClass is called
        """

        file_output = FileOutput(self.test_run_information)
        file_output.log()

    def getFailures(self, exception_list):
        """
        :param exception_list:
        :return: list of exceptions
        """
        if exception_list and exception_list[-1][0] is self:
            print(exception_list[-1][1])
            return exception_list[-1][1]

    def test_given_int_list_expected_one_item(self):
        test_input = [1, 2, -3, 0, 7]
        expected_value = [[-3, 1, 2]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_int_list_expected_two_items(self):
        test_input = [-2, -1, 0, 1, 2]
        expected_value = [[-2, 0, 2], [-1, 0, 1]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_int_list_expected_three_items(self):
        test_input = [-2, -1, 0, 1, 2, 3]
        expected_value = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_int_list_positive_numbers_only_expected_empty(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_int_list_negative_numbers_only_expected_empty(self):
        test_input = [-1, -2, -3, -4, -5, -6, -7, -8]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_double_list_numbers_only_expected_empty(self):
        test_input = [-2.2, -1.1, 0.0, 1.1, 2.2]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_int_and_double_only_expected_empty(self):
        test_input = [0, 1, 2, 3, 4.4, 5.5, -1, -2, -3, -4.4, -5.5]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_repeated_int_negative_and_positive_ones_expected_empty(self):
        test_input = [-1, -1, -1, 1, 1, 1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_repeated_double_negative_and_positive_one_point_one_expected_empty(self):
        test_input = [-1.1, -1.1, -1.1, 1.1, 1.1, 1.1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_int_in_range_negative_1_to_1_expected_same_as_input(self):
        test_input = [-1, 0, 1]
        expected_value = [[-1, 0, 1]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_three_zeros_expected_three_zeros(self):
        test_input = [0, 0, 0]
        expected_value = [[0, 0, 0]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_chars_expected_empty(self):
        test_input = ['', 'a']
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_positive_doubles_expected_empty(self):
        test_input = [1.1, 2.2]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_negative_doubles_expected_empty(self):
        test_input = [-1.1, -2.2]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_positive_int_expected_empty(self):
        test_input = [1, 2]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_negative_int_expected_empty(self):
        test_input = [-1, -2]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_zeros_expected_empty(self):
        test_input = [0, 0]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_one_char_expected_empty(self):
        test_input = ['a']
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_one_int_expected_empty(self):
        test_input = [1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_one_double_expected_empty(self):
        test_input = [1.1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_empty_list_expected_empty(self):
        test_input = ['a']
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_double_sum_equal_zero_expected_empty(self):
        test_input = [0.0, -1.1, 1.1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_one_char_two_int_expected_empty(self):
        test_input = ['a', 1, -1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_two_ints_sum_zero_expected_empty(self):
        test_input = [-1, 1]
        expected_value = []
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)

    def test_given_list_of_ints_range_negative_five_to_positive_5_expected_valid_output(self):
        test_input = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        expected_value = [[-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -2, 5],
                          [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
        result = Solution.threeSum(self, test_input)
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
