import unittest

from typing import Set, List
from problems.remove_invalid_parentheses.solution import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.example_0_input = "()"
        self.example_0_output = ["()"]
        self.example_1_input = "()())()"
        self.example_1_output = ["()()()", "(())()"]
        self.example_2_input = "(a)())()"
        self.example_2_output = ["(a)()()", "(a())()"]
        self.example_3_input = ")("
        self.example_3_output = [""]
        self.example_4_input = ")(f"
        self.example_4_output = ["f"]
        self.example_5_input = "))"
        self.example_5_output = [""]
        self.example_6_input = "(j))("
        self.example_6_output = ["(j)"]
        self.example_7_input = "x("
        self.example_7_output = ["x"]
        self.example_8_input = "()((((()"
        self.example_8_output = ["()()"]
        self.example_9_input = "())(()"
        self.example_9_output = ["()()"]
        self.example_10_input = "())(((()m)("
        self.example_10_output = ["()(()m)"]

    def test_valid_string(self):
        self.assertTrue(self.solution.is_valid_string(""))
        self.assertTrue(self.solution.is_valid_string("a"))
        self.assertTrue(self.solution.is_valid_string("()"))
        self.assertTrue(self.solution.is_valid_string("()()"))
        self.assertTrue(self.solution.is_valid_string("(())"))
        self.assertFalse(self.solution.is_valid_string("(()"))
        self.assertFalse(self.solution.is_valid_string(")()("))

    def test_example_0(self):
        self.assertCountEqual(self.example_0_output,
                              self.solution.removeInvalidParentheses(self.example_0_input))

    def test_example_1(self):
        self.assertCountEqual(self.example_1_output,
                              self.solution.removeInvalidParentheses(self.example_1_input))

    def test_example_2(self):
        self.assertCountEqual(self.example_2_output,
                              self.solution.removeInvalidParentheses(self.example_2_input))

    def test_example_3(self):
        self.assertCountEqual(self.example_3_output,
                              self.solution.removeInvalidParentheses(self.example_3_input))

    def test_example_4(self):
        self.assertCountEqual(self.example_4_output,
                              self.solution.removeInvalidParentheses(self.example_4_input))

    def test_example_5(self):
        self.assertCountEqual(self.example_5_output,
                              self.solution.removeInvalidParentheses(self.example_5_input))

    def test_example_6(self):
        self.assertCountEqual(self.example_6_output,
                              self.solution.removeInvalidParentheses(self.example_6_input))

    def test_example_7(self):
        self.assertCountEqual(self.example_7_output,
                              self.solution.removeInvalidParentheses(self.example_7_input))

    def test_example_8(self):
        self.assertCountEqual(self.example_8_output,
                              self.solution.removeInvalidParentheses(self.example_8_input))

    def test_example_9(self):
        self.assertCountEqual(self.example_9_output,
                              self.solution.removeInvalidParentheses(self.example_9_input))

    def test_example_10(self):
        self.assertCountEqual(self.example_10_output,
                              self.solution.removeInvalidParentheses(self.example_10_input))
