# https://leetcode.com/problems/reverse-linked-list/
# linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        return prev