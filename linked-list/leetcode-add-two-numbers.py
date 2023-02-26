# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        def reverse_concat(ll):
            digit_str = ''
            cur = ll
            while cur:
                digit_str = str(cur.val) + digit_str
                cur = cur.next
            return digit_str

        digit_str = str(int(reverse_concat(l1)) + int(reverse_concat(l2)))
        prev, cur = None, ListNode(int(digit_str[-1]))
        head = cur
        for i in range(len(digit_str)-2,-1,-1):
            prev = cur
            cur = ListNode(int(digit_str[i]))
            prev.next = cur
        return head