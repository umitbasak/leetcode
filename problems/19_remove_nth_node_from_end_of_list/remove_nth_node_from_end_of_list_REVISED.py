from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        headCopy = head
        while headCopy:
            length += 1
            headCopy = headCopy.next
        print(length)

        fromStart = length - n

        prev = None
        curr = head
        for _ in range(fromStart):
            prev = curr
            curr = curr.next

        if prev is None:
            return None

        # print(prev.val, curr.val)
        tmp = curr.next
        curr.next = None
        prev.next = tmp

        return head


solution = Solution()
# h2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
h1 = ListNode(1, None)
test1 = solution.removeNthFromEnd(h1, 1)
# test2 = solution.removeNthFromEnd(h2, 2)
