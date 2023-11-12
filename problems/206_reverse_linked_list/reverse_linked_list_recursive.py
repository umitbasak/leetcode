# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reversedListHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedListHead


node1 = ListNode()
node2 = ListNode()
node3 = ListNode()
node4 = ListNode()

node1.val = 1
node2.val = 2
node3.val = 3
node4.val = 4

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
reversed = solution.reverseList(node1)
