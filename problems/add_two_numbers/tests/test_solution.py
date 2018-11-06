import unittest
from problems.add_two_numbers.solution import ListNode, Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_double_null_input(self):
        expected_output = ListNode(0)
        iterative_solution = self.solution.add_two_numbers_iterative(None, None)
        recursive_solution = self.solution.add_two_numbers_recursive(None, None, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_lists_of_length_one(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        expected_output = ListNode(3)
        iterative_solution = self.solution.add_two_numbers_iterative(l1, l2)
        recursive_solution = self.solution.add_two_numbers_recursive(l1, l2, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_carry_over_last_digit(self):
        l1 = ListNode(9)
        l2 = ListNode(9)
        expected_output = ListNode(8)
        expected_output.next = ListNode(1)
        iterative_solution = self.solution.add_two_numbers_iterative(l1, l2)
        recursive_solution = self.solution.add_two_numbers_recursive(l1, l2, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_no_carry_over(self):
        l1 = ListNode(8)
        l2 = ListNode(7)
        l2.next = ListNode(1)
        expected_output = ListNode(5)
        expected_output.next = ListNode(2)
        iterative_solution = self.solution.add_two_numbers_iterative(l1, l2)
        recursive_solution = self.solution.add_two_numbers_recursive(l1, l2, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_lists_equal_length(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        expected_output = ListNode(7)
        expected_output.next = ListNode(0)
        expected_output.next.next = ListNode(8)
        iterative_solution = self.solution.add_two_numbers_iterative(l1, l2)
        recursive_solution = self.solution.add_two_numbers_recursive(l1, l2, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_lists_different_length(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l2 = ListNode(9)
        l2.next = ListNode(9)
        expected_output = ListNode(8)
        expected_output.next = ListNode(9)
        expected_output.next.next = ListNode(0)
        expected_output.next.next.next = ListNode(1)
        iterative_solution = self.solution.add_two_numbers_iterative(l1, l2)
        recursive_solution = self.solution.add_two_numbers_recursive(l1, l2, ListNode(0))
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2])
        self._check_all_lists_equal(expected_output, [iterative_solution, recursive_solution, multi_list_solution])

    def test_multi_list_addition(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l2 = ListNode(9)
        l2.next = ListNode(9)
        l2.next.next = ListNode(9)
        l3 = ListNode(9)
        l3.next = ListNode(9)
        l3.next.next = ListNode(9)
        l3.next.next.next = ListNode(9)
        expected_output = ListNode(7)
        expected_output.next = ListNode(9)
        expected_output.next.next = ListNode(0)
        expected_output.next.next.next = ListNode(1)
        expected_output.next.next.next.next = ListNode(1)
        multi_list_solution = self.solution.add_multiple_numbers_iterative([l1, l2, l3])
        self._check_lists_equal(expected_output, multi_list_solution)

    def _check_lists_equal(self, expected_list, actual_list):
        self.assertIsNotNone(expected_list)
        self.assertIsNotNone(actual_list)
        self.assertEqual(expected_list, actual_list)

    def _check_all_lists_equal(self, expected_list, lists_to_check):
        for list_to_check in lists_to_check:
            self.assertEqual(expected_list, list_to_check)


if __name__ == '__main__':
    unittest.main()
