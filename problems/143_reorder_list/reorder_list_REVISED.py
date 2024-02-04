from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printLinkedList(self):
        head = self
        while head:
            print(f"{head.val} ->", end="")
            head = head.next
        print()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverseLinkedList(head):
            prev = None
            curr = head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow now points to the middle node
        reversed = reverseLinkedList(slow.next)
        slow.next = None
        # head      =   1->2->3
        # reversed  =   5->4
        first = head

        while first and reversed:
            tmp = first.next
            first.next = reversed
            tmp2 = reversed.next
            reversed.next = tmp
            first = tmp
            reversed = tmp2

        return head


# h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
h2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

solution = Solution()
# test1 = solution.reorderList(h1)
test2 = solution.reorderList(h2)
