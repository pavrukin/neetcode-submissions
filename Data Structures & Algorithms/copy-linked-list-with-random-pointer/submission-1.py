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
        if not head:
            return None
        
        current = head
        while current:
            cloned = Node(current.val)
            cloned.next = current.next
            current.next = cloned
            current = cloned.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current:
            cloned_node = current.next
            copy_tail.next = cloned_node
            copy_tail = copy_tail.next
            current.next = cloned_node.next
            current = current.next

        return dummy.next

        