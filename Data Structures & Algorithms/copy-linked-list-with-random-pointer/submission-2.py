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
        
        # inserting clone nodes into the original list
        # from: A -> B -> C  
        # to:   A -> A' -> B -> B' -> C -> C'
        current = head
        while current:
            cloned = Node(current.val)
            cloned.next = current.next
            current.next = cloned
            current = cloned.next
        
        #linking random pointers directly in cloned list nodes A'B'C'
        current = head
        while current:
            if current.random:
                # current.next is a cloned node.
                current.next.random = current.random.next
            # from here A -> A' -> to here  B -> B' ->  to here  C -> C'
            current = current.next.next
        
        dummy = Node(0)
        # point to the end of our new cloned list
        copy_tail = dummy

        current = head
        #unlink from original list
        while current:
            cloned_node = current.next
            copy_tail.next = cloned_node
            copy_tail = copy_tail.next
            current.next = cloned_node.next
            current = current.next

        return dummy.next

        