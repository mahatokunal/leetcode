# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while (fast and slow):
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast==slow:
                return True