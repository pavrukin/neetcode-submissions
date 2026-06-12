# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = leftself
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced=True
        def deep_dist(node):
            if not node:
                return 0

            deep_left=deep_dist(node.left)
            deep_right=deep_dist(node.right)
            
            if abs(deep_left-deep_right)>1:
                self.isBalanced=False

            return max(deep_right,deep_left)+1
        
        deep_dist(root)
    
        return self.isBalanced