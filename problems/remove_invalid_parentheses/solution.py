from typing import List, Set


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = self.strip_invalid_parentheses(s)

        valid_set: Set[str] = self.helper(s)

        if len(valid_set) == 0:
            return [""]
        return list(valid_set)

    def helper(self, s: str) -> Set[str]:
        valid_set: Set[str] = set()
        n_modifications_set: Set[str] = set()
        n_plus_1_modifications_set: Set[str] = set()
        n_modifications_set.add(s)
        while n_modifications_set:
            test_string = n_modifications_set.pop()
            if self.is_valid_string(test_string):
                valid_set.add(test_string)
            else:
                net_paren = self.net_parentheses(test_string)
                chars_to_remove: Set[str] = set()
                if net_paren <= 0:
                    chars_to_remove.add(")")
                if net_paren >= 0:
                    chars_to_remove.add("(")
                for i in range(len(test_string)):
                    if test_string[i] in chars_to_remove:
                        n_plus_1_modifications_set.add(self.remove_character_at_index(test_string, i))
            if len(n_modifications_set) == 0:
                if len(valid_set) > 0:
                    return valid_set
                n_modifications_set = n_plus_1_modifications_set
                n_plus_1_modifications_set = set()
        return valid_set

    def strip_invalid_parentheses(self, s: str) -> str:
        counter = 0
        while counter < len(s) and s[counter] != "(":
            if s[counter] is ")":
                s = self.remove_character_at_index(s, counter)
            else:
                counter += 1

        end_counter = len(s) - 1
        while end_counter > 0 and s[end_counter] != ")":
            if s[end_counter] is "(":
                s = self.remove_character_at_index(s, end_counter)
            end_counter -= 1
        return s

    def is_valid_string(self, s: str) -> bool:
        counter = 0
        for letter in s:
            if letter is "(":
                counter += 1
            elif letter is ")":
                counter -= 1
            if counter < 0:
                return False
        return counter is 0

    def net_parentheses(self, s: str) -> int:
        counter = 0
        for letter in s:
            if letter is "(":
                counter += 1
            elif letter is ")":
                counter -= 1
            if counter < 0:
                print("early exit")
                return -1
        return counter

    def remove_character_at_index(self, s: str, i: int) -> str:
        return s[0:i] + s[i+1:len(s)]

