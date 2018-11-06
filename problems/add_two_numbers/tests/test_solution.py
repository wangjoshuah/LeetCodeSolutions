import unittest
from problems.add_two_numbers.solution import ListNode, Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_double_null_input(self):
        expected_output = ListNode(0)
        actual_output = self.solution.addTwoNumbers(None, None)
        self._check_lists_equal(expected_output, actual_output)

    def test_lists_of_length_one(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        expected_output = ListNode(3)
        actual_output = self.solution.addTwoNumbers(l1, l2)
        self._check_lists_equal(expected_output, actual_output)

    def test_carry_over_last_digit(self):
        l1 = ListNode(9)
        l2 = ListNode(9)
        expected_output = ListNode(8)
        expected_output.next = ListNode(1)
        actual_output = self.solution.addTwoNumbers(l1, l2)
        self._check_lists_equal(expected_output, actual_output)

    def test_no_carry_over(self):
        l1 = ListNode(8)
        l2 = ListNode(7)
        l2.next = ListNode(1)
        expected_output = ListNode(5)
        expected_output.next = ListNode(2)
        actual_output = self.solution.addTwoNumbers(l1, l2)
        self._check_lists_equal(expected_output, actual_output)

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
        actual_output = self.solution.addTwoNumbers(l1, l2)
        self._check_lists_equal(expected_output, actual_output)

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
        actual_output = self.solution.addTwoNumbers(l1, l2)
        self._check_lists_equal(expected_output, actual_output)

    def _check_lists_equal(self, expected_list, actual_list):
        self.assertIsNotNone(expected_list)
        self.assertIsNotNone(actual_list)
        print("expected_list is " + str(expected_list))
        print("actual_list is " + str(actual_list))
        while expected_list is not None or actual_list is not None:
            self.assertEqual(expected_list.val, actual_list.val)
            expected_list = expected_list.next
            actual_list = actual_list.next


if __name__ == '__main__':
    unittest.main()
