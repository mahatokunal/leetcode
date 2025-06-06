# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        prev = None
        
        while(head):
            curr_next = head.next
            head.next =prev
            prev = head
            head = curr_next
        
        return prev
#         prev.   head
#                 curr_next
#None <-   1  ->      2     ->    3  ->    4  ->    5
#