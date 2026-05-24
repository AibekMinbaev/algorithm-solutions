# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative 
        stack = [(root, 0)] 

        res = 0 
        while stack: 
            r, d = stack.pop() 
            if not r: 
                continue 
            
            res = max(res, d+1)
            stack.append((r.left, d+1))
            stack.append((r.right, d+1))

        return res 




        # # recursive 
        # # time: n 
        # # space: n 
        # def helper(r, d): 
        #     if not r: return 0
        #     return 1 + max(helper(r.left, 0), helper(r.right, 0)) 
        # return helper(root, 0)