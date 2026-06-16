# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.counter_goodNodes=0

        # we go through nodes and keeping parent value as max
        def dfs(node, current_max):
            if not node:
                return 

            if node.val>=current_max :
                self.counter_goodNodes+=1
                current_max=node.val
            
            dfs(node.left,current_max)
            dfs(node.right,current_max)
            
        dfs(root,root.val)
        
        return self.counter_goodNodes

            



