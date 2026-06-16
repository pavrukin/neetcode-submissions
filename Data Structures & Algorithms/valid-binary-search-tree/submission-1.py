# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, left_low, right_high):
            if not node:
                return True

            if not  left_low < node.val < right_high:
                return False

            A=validate(node.left, left_low, node.val)
            B=validate(node.right, node.val, right_high)
            return A and B
        
        return validate(root, float('-inf'), float('inf'))



        