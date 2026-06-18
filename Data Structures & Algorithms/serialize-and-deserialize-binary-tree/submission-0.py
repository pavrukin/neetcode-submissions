# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec: 
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        results=[]

        def dfs(node):
            if not node:
                results.append("N")
                return 

            results.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        string_r=",".join(results)
        print("string_r",string_r)
        return string_r

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return TreeNode([])

        self.values = data.split(",")
        self.pointer=0

        def build_dfs():
            node_val=self.values[self.pointer]
            self.pointer+=1

            if node_val=="N":
                return None

            node=TreeNode(int(node_val))
            node.left=build_dfs()
            node.right=build_dfs()

            return node
        
        return build_dfs()






