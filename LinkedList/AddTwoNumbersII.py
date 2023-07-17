# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        num = num1 + num2
        head = None

        if num == 0:
            return ListNode(0)

        while num:
            digit = num % 10
            num = num // 10
            node = ListNode(digit)
            node.next = head
            head = node

        return head


sol = Solution()
print(sol.addTwoNumbers([7, 2, 4, 3], [5, 6, 4]))
