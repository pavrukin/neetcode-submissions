# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter=0

        def deepest_distance(node):
            if not node:
                return 0
        
            leftdepth=deepest_distance(node.left)
            rightdepth=deepest_distance(node.right)

            self.maxdiameter= max(self.maxdiameter,leftdepth+rightdepth)
            return max(leftdepth,rightdepth)+1

        deepest_distance(root)

        return self.maxdiameter