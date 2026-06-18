# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        results=[]   
        queue=deque([root])

        while queue:
            node = queue.popleft()

            if node:
                results.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                results.append("N")
            
        while results and results[-1] == "N":
            results.pop()

        return ",".join(results)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values=data.split(",")
        root=TreeNode(int(values[0]))
        pointer=1

        queue=deque([root])

        while queue and pointer<len(values):
            parent=queue.popleft()

            if values[pointer] != "N":
                left_child=TreeNode(int(values[pointer]))
                parent.left=left_child
                queue.append(left_child)
            pointer+=1

            if pointer<len(values):
                if values[pointer] != "N":
                    right_child=TreeNode(int(values[pointer]))
                    parent.right=right_child
                    queue.append(right_child)
                pointer+=1
        
        return root




            