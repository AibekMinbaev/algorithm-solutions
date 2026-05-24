# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(r, d): 
            if not r: return 0
            return 1 + max(helper(r.left, 0), helper(r.right, 0)) 
        return helper(root, 0)