# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001 

        def helper(root): 
            nonlocal res 

            if not root: 
                return -1001 
            
            left = helper(root.left) 
            right = helper(root.right) 
            val = max(root.val, root.val + left, root.val + right)
            res = max(res, val, root.val + left + right)
            return val 
        helper(root) 
        return res 



