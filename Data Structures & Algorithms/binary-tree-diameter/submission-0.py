# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getMaxEdges(root, d=0):
            if not root: 
                return d 
            return max(getMaxEdges(root.left, d+1), getMaxEdges(root.right, d+1))  
            
        
        res = 0 
        def dfs(root): 
            nonlocal res
            
            if not root: 
                return 
            
            res = max(res, getMaxEdges(root.left) + getMaxEdges(root.right))

            dfs(root.left) 
            dfs(root.right) 
            
        dfs(root) 
        return res 

        
