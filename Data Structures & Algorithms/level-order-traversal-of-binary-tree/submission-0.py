# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result=[]
        queue=deque([root])
        
        while queue:
            level_amount=len(queue)
            current_result=[]

            for _ in range(level_amount): 
                current=queue.popleft()
                current_result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            result.append(current_result)
        
        return result
            

