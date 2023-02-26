from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = head
        if new_head and new_head.next:
            new_head = new_head.next

        prev, cur = None, head
        while cur and cur.next:
            # swap pair
            next = cur.next
            nnext = next.next
            next.next = cur
            cur.next = nnext

            # after swap pair, adjust connection with previous pair
            if prev:
                prev.next = next

            # step over 2 node, with keeping previous cur
            prev = cur
            cur = nnext
        return new_head

