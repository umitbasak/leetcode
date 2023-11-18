from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nPreviousNodes = [head]

        if not head.next and n == 1:
            return None

        headCopy = head.next
        while headCopy:
            if len(nPreviousNodes) >= n + 1:
                nPreviousNodes.pop(0)
            nPreviousNodes.append(headCopy)
            headCopy = headCopy.next

        if n > 1:
            nPreviousNodes[0].next = nPreviousNodes[2]
        else:
            nPreviousNodes[0].next = None
        return head


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
