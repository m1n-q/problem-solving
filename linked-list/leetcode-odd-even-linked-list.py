from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class EvenBox:
    def __init__(self):
        self.prev = None
        self.head = None
        self.tail = None
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNext(self, evenBox):
        if evenBox.next:
            evenBox.tail.next = evenBox.next.next
        if evenBox.prev:
            evenBox.prev.next = evenBox.next
        if evenBox.next:
            evenBox.next.next = evenBox.head
        evenBox.prev = evenBox.next
        if evenBox.tail:
            evenBox.next = evenBox.tail.next


    def appendNext(self, evenBox, afterBox):
        if not evenBox.head:
            evenBox.head = evenBox.tail = afterBox
        evenBox.tail = afterBox
        if afterBox:
            evenBox.next = afterBox.next


    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenBox = EvenBox()
        evenBox.prev = head

        ret = cur = head
        curIdx = 1
        while cur and cur.next:
            if curIdx % 2: # odd
                self.appendNext(evenBox, cur.next)
            else: # even
                self.swapNext(evenBox)
            cur = evenBox.tail
            curIdx += 1
        return ret

    # sol2
    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = odd_head = head
        even = even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return odd_head

# leetcode submit region end(Prohibit modification and deletion)
