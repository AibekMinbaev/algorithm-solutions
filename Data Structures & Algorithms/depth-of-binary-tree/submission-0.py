# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0 
        def helper(r, d): 
            nonlocal res
            
            if not r: 
                res = max(res, d) 
                return 
            
            helper(r.left, d+1) 
            helper(r.right, d+1) 

        
        helper(root, 0)
        return res 