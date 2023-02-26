from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur, cur_idx = None, head, 1
        while cur:
            if cur_idx == left:
                before_left, new_tail = prev, cur
                while cur and cur_idx <= right:
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    cur_idx += 1

                if before_left:
                    before_left.next = prev  # right-end
                else:
                    head = prev  # right-end goes to head of list
                new_tail.next = cur  # was_right.next
                break

            prev, cur = cur, cur.next
            cur_idx += 1
        return head
# leetcode submit region end(Prohibit modification and deletion)
