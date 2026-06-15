# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]

        def goRight(node,level):
            if not node:
                return 
            if level==len(result):
                result.append(node.val)

            goRight(node.right,level+1)
            goRight(node.left,level+1)
        
        print("result",result) 
        goRight(root,0)

        return result
