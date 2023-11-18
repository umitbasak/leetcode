from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete the node
        left.next = left.next.next
        return dummy.next


node1 = ListNode()
node2 = ListNode()
node3 = ListNode()
node4 = ListNode()
node5 = ListNode()

node1.val = 1
node2.val = 2
node3.val = 3
node4.val = 4
node5.val = 5

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
removed = solution.removeNthFromEnd(node1, 2)
print(removed)
