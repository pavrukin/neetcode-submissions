# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def inordermap(inorder):
            inordermapdict={}
            for index, value in enumerate(inorder):
                inordermapdict[value]=index 
            return inordermapdict
            # or return {value: index for index, value in enumerate(inorder)}

        inorder_dict=inordermap(inorder)

        self.pre_ind=0

        def dfs(left,right):
            if left>right:
                return None
            
            root_val=preorder[self.pre_ind]
            root=TreeNode(root_val)

            self.pre_ind+=1

            mid=inorder_dict[root_val]

            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)

            return root
        
        return dfs(0, len(inorder)-1)

            


            


            
             



        

           

