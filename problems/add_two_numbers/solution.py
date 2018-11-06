# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.next) + str(self.val)

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Add two numbers iteratively
        return self.add_two_numbers_iterative(l1, l2)
        """
        Add two numbers recursively
        return self.add_two_numbers_recursive(l1, l2, ListNode(0))
        """
        """
        Add multiple lists of numbers
        addends = list()
        if l1 is not None:
            addends.append(l1)
        if l2 is not None:
            addends.append(l2)
        return self.add_multiple_numbers_iterative(addends)
        """

    def add_two_numbers_recursive(self, l1, l2, carry_over):
        # both lists are done
        if (l1 is None
                and l2 is None
                and carry_over is None):
            return None

        if carry_over is None:
            carry_over = ListNode(0)
        if l1 is not None:
            carry_over.val += l1.val
            l1 = l1.next
        if l2 is not None:
            carry_over.val += l2.val
            l2 = l2.next

        next_carry_over = None
        if carry_over.val >= 10:
            carry_over.val -= 10
            next_carry_over = ListNode(1)
        carry_over.next = self.add_two_numbers_recursive(l1, l2, next_carry_over)
        return carry_over

    def add_two_numbers_iterative(self, l1, l2):
        sum_list = ListNode(0)
        current_place = sum_list
        # While both lists still have elements
        while l1 is not None and l2 is not None:
            current_place.val += l1.val
            current_place.val += l2.val
            if current_place.val >= 10:
                current_place.val -= 10
                current_place.next = ListNode(1)
            elif l1.next is not None or l2.next is not None:
                current_place.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            current_place = current_place.next

        # when only one list has elements
        remaining_digits = None
        if l1 is not None:
            remaining_digits = l1
        elif l2 is not None:
            remaining_digits = l2

        while remaining_digits is not None:
            current_place.val += remaining_digits.val
            if current_place.val >= 10:
                current_place.next = ListNode(1)
                current_place.val -= 10
            elif remaining_digits.next is not None:
                current_place.next = ListNode(0)
            remaining_digits = remaining_digits.next
            current_place = current_place.next

        return sum_list

    def add_multiple_numbers_iterative(self, addends):
        sum_list = ListNode(0)
        current_place = sum_list
        while len(addends) > 0:
            next_place_value_addends = list()
            carry_over = 0
            for addend in addends:
                current_place.val += addend.val
                if addend.next is not None:
                    next_place_value_addends.append(addend.next)
                while current_place.val >= 10:
                    current_place.val -= 10
                    carry_over += 1
            if carry_over > 0:
                next_place_value_addends.append(ListNode(carry_over))
            addends = next_place_value_addends
            if len(addends) > 0:
                current_place.next = ListNode(0)
            current_place = current_place.next
        return sum_list
