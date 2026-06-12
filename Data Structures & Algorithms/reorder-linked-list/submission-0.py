# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first_half_slow=head
        second_half_fast=head
        #
        while second_half_fast and second_half_fast.next:
            first_half_slow=first_half_slow.next
            second_half_fast=second_half_fast.next.next

        # we reach with equal 1 2 3 4 
        # first_half_slow 3
        # second_half_fast None
        # we reach with unequal 1 2 3 4 5
        # second_half_fast None
        # first_half_slow 3
        # both cases beginning of the second part

        # starting reverse procedure
        curr_second=first_half_slow.next
        #cut the first part
        first_half_slow.next=None
        # to create the end of the reverse array
        prev_second = None 

        while curr_second:
            # save pointer to move ->
            nxt=curr_second.next
            # change current pointer next to <-
            curr_second.next=prev_second
            # shift prev -> to the current
            prev_second=curr_second
            # shift current  -> to the next
            curr_second=nxt

        merge_l1=head
        merge_l2=prev_second

        while merge_l2:
            # save next pointers
            nxt1=merge_l1.next
            nxt2=merge_l2.next

            #create link l1 to l2 and l2 next l1
            merge_l1.next=merge_l2
            merge_l2.next=nxt1

            # move 
            merge_l1=nxt1
            merge_l2=nxt2







