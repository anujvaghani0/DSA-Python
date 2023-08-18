# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # @staticmethod
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist = ListNode()
        blist = ListNode()
        small, big = slist, blist

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next

        small.next = blist.next
        big.next = None  # prevent cycle

        return slist.next


sol = Solution()
linked_list = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
sol.partition(linked_list, 3)


def print_list(linked_list: Optional[ListNode]):
    current = linked_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


print_list(linked_list)
