from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()

        cur = head
        carry = 0
        prev = ListNode()
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            cur.val = sum % 10 + carry
            carry = 0
            if cur.val > 9:
                cur.val -= 10
                carry += 1
            cur.next = ListNode()
            prev = cur
            cur = cur.next
            carry += sum // 10

        if carry > 0:
            cur.val = carry
        else:
            prev.next = None

        return head
