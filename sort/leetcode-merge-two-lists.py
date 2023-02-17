# https://leetcode.com/problems/merge-two-sorted-lists/
# merge-sort
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None: return list2
        elif list2 == None: return list1

        cur1 = list1
        cur2 = list2

        head = new = ListNode() # Dummy head

        while cur1 and cur2:
            new.next = ListNode()

            if cur1.val < cur2.val:
                new.next.val = cur1.val
                cur1 = cur1.next
            else:
                new.next.val = cur2.val
                cur2 = cur2.next
            new = new.next


        if cur1 == None and cur2:
            new.next = cur2
        elif cur2 == None and cur1:
            new.next = cur1
        return head.next # Except dummy head

