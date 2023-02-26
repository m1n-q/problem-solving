# https://leetcode.com/problems/palindrome-linked-list/solutions/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        # 중간 찾기
        half, tail = head, head
        while tail and tail.next:
            tail = tail.next.next
            half = half.next

        # 중간 ~ 맨뒤 연결방향 바꾸기. 포인터 세 개 필요!
        pprev, prev, cur = None, None, half
        while cur:
            pprev = prev
            prev = cur
            cur = cur.next
            prev.next = pprev

        # 처음 ~ 중간 | 맨뒤 ~ 중간 비교하기
        left, right = head, prev
        while left and right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True
