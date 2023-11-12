from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # making sure that fast.next is not null so we won't get
        # a null pointer error in fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev
        while second:
            (
                tmp1,
                tmp2,
            ) = (
                first.next,
                second.next,
            )
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


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
reversed = solution.reorderList(node1)
