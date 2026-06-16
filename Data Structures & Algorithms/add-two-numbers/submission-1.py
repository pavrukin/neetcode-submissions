# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        l3 = ListNode(0)
        curr=l3
        while (l1 is not None) or (l2 is not None) :
            if l1 is None:
                addl1=0
            else:
                addl1=l1.val
                l1=l1.next

            if l2 is None:
                addl2=0
            else:
                addl2=l2.val
                l2=l2.next
            
            newval=addl1+addl2+carry
            carry = 0
            if newval>9:
                newval-=10
                carry=1
            curr.next=ListNode(newval)
            curr=curr.next
            
            
        if carry>0:
            curr.next=ListNode(carry)
            curr=curr.next
        return l3.next
             