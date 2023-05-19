from time import sleep
from typing import Set


def solution_1(input_str: str) -> int:
    if not input_str:
        return 0

    longest_substring = input_str[0]
    current_substring_tracker: Set[str] = set(longest_substring)
    for character in input_str[1:]:
        next_substring_tracker: Set[str] = set()
        for substring in current_substring_tracker:
            sleep(0.001)
            if character not in substring:
                appended_substring = substring + character
                next_substring_tracker.add(appended_substring)
                if len(appended_substring) > len(longest_substring):
                    longest_substring = appended_substring
        next_substring_tracker.add(character)
        current_substring_tracker = next_substring_tracker.copy()

    return len(longest_substring)


def solution_2(input_str: str) -> int:
    if not input_str:
        return 0

    num_distinct_characters = len(set(input_str))
    longest_substring = input_str[0]

    current_substring_tracker: Set[str] = set(longest_substring)
    for character in input_str[1:]:
        next_substring_tracker: Set[str] = set()
        for substring in current_substring_tracker:
            sleep(0.001)
            if character not in substring:
                appended_substring = substring + character
                next_substring_tracker.add(appended_substring)
                if len(appended_substring) > len(longest_substring):
                    longest_substring = appended_substring
                    if len(longest_substring) == num_distinct_characters:
                        return len(longest_substring)
        next_substring_tracker.add(character)
        current_substring_tracker = next_substring_tracker.copy()

    return len(longest_substring)
