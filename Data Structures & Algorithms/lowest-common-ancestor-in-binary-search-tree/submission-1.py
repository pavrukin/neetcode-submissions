# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode, depth=0) -> TreeNode:
        
        indent = "  " * depth

        if not root:
            return root  

        print(f"{indent}Visiting Node({root.val})")

        if root.val == p.val or root.val == q.val: 
            print(f"{indent}--> Found target! Returning Node({root.val})")
            return root
     
        left_side=self.lowestCommonAncestor(root.left,p,q,depth + 1)
        right_side=self.lowestCommonAncestor(root.right,p,q,depth + 1)

        left_val = left_side.val if left_side else "None"
        right_val = right_side.val if right_side else "None"
        print(f"{indent}Node({root.val}) results -> left_side: {left_val}, right_side: {right_val}")

        if left_side and right_side:
            print(f"{indent}--> Split point found at Node({root.val})!")
            return root
        
        if left_side: 
            print(f"{indent}--> Bubbling up Left Result: Node({left_val})")
            return left_side
        else: 
            print(f"{indent}--> Bubbling up Right/None Result: Node({right_val})")
            return right_side
        
