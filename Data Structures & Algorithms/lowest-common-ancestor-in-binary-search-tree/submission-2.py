# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        
        # Iterative solution 
        
        stack = [root] 

        while stack: 
            r = stack.pop() 

            if r.val == p.val or r.val == q.val: 
                return r 
            
            if min(p.val, q.val) < r.val < max(p.val, q.val): 
                return r 
            
            if r.left and max(p.val, q.val) < r.val: 
                stack.append(r.left) 
            elif r.right and min(p.val, q.val) > r.val: 
                stack.append(r.right) 
        
        
        
        # # Recursive solution 
        # # time: h 
        # # space: h 
        # if root.val == p.val or root.val == q.val: 
        #     return root 
        
        # if  min(p.val, q.val) < root.val < max(p.val, q.val): 
        #     return root 
        
        # if max(p.val, q.val) < root.val and root.left: 
        #     return self.lowestCommonAncestor(root.left, p, q) 
        # elif min(p.val, q.val) > root.val and root.right: 
        #     return self.lowestCommonAncestor(root.right, p, q) 
        


