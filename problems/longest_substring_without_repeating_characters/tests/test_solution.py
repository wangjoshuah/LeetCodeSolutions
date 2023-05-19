import pytest

from problems.longest_substring_without_repeating_characters.solution import solution_1, solution_2

test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    ("a", 1),
    ("ab", 2),
    ("abc", 3),
    ("abcd", 4),
    ("abcde", 5),
    ("abcdef", 6),
    ("abcdefg", 7),
    ("abcdefgh", 8),
    ("abcdefghi", 9),
    ("abcdefghij", 10),
    ("abcdefghijk", 11),
    ("abcdefghijkl", 12),
    ("abcdefghijklm", 13),
    ("abcdefghijklmn", 14),
    ("abcdefghijklmno", 15),
    ("abcdefghijklmnop", 16),
    ("abcdefghijklmnopq", 17),
    ("abcdefghijklmnopqr", 18),
    ("abcdefghijklmnopqrs", 19),
    ("abcdefghijklmnopqrst", 20),
    ("ababababababababababababababababababababababa", 2)
]


@pytest.mark.parametrize("input_str, output", test_cases)
def test_solution_1(input_str, output):
    assert solution_1(input_str) == output


@pytest.mark.parametrize("input_str, output", test_cases)
def test_solution_2(input_str, output):
    assert solution_2(input_str) == output
