from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = []
        stack = []
        listLength = 0
        # populating the stack and the queue
        headCopy = head.copy()
        while headCopy is not None:
            queue.append(headCopy)
            stack.append(headCopy)
            headCopy = headCopy.next
            listLength += 1

        for i in range(listLength):
            if i % 2 == 0:
                head = queue.pop(0)
            else:
                head = stack.pop()
            head = head.next
