# Leetcode 0002 (Medium): Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        memo = 0
        dummy = ListNode(-1)
        current = dummy
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current.next = ListNode((val1 + val2 + memo) % 10)
            memo = (val1 + val2 + memo) // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            current = current.next

        if memo > 0:
            current.next = ListNode(memo)
        
        return dummy.next
