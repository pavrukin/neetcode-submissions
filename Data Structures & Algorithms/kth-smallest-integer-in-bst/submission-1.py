# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        self.minvalue=None

        def dfs(node):
            if not node or self.minvalue is not None:
                return

            dfs(node.left)
            # print("k", self.k)
            # print("node value", node.val)
            self.k-=1
            if self.k==0:
               self.minvalue=node.val
               return 
            
            dfs(node.right)

        dfs(root)

        return self.minvalue
            
            