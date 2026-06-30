"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current=head
        mapping={None: None}
        while current is not None:
            mapping[current]=Node(current.val)
            current=current.next

        current=head
        while current is not None:
            mapping[current].random=mapping[current.random]
            mapping[current].next=mapping[current.next]
            current=current.next
        
        return mapping[head]
        

