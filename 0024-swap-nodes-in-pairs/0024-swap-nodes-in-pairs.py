# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        first, prev = head, dummy

        while first and first.next:
            nextPair = first.next.next
            second = first.next

            second.next = first
            first.next = nextPair
            prev.next = second

            prev = first
            first = nextPair

        return dummy.next