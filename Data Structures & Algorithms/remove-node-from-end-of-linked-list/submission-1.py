# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_n=head
        pointer_c=head
        for _ in range(n):
            pointer_n=pointer_n.next

        # edge case if n equals the whiole array    
        if not pointer_n:
            return head.next 

        # we go till the end while c does exactly to the right position
        # here we move but don't change values
        while pointer_n.next:
            pointer_n=pointer_n.next
            pointer_c=pointer_c.next
        
        # we rearrange only this pointer as others are set up
        pointer_c.next=pointer_c.next.next
        
        return head
            


