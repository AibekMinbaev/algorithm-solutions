# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        # Optimized on the fly solution 
        # time: h + k, worst case n  
        # space: h, worst case n
        
        res = None 

        def dfs(node: TreeNode) -> None: 
            nonlocal res, k
            if not node: 
                return 

            if res: 
                return 
                
            dfs(node.left) 
            k -= 1 
            if k == 0: 
                res = node 
                return 
            dfs(node.right)

        dfs(root) 
        return res.val
        


        # Brute Force
        # time: O(n) 
        # space: n (for vals and recursion stack) 
        vals = [] 

        def dfs(node):
            if not node: 
                return 
            
            dfs(node.left)
            vals.append(node.val) 
            dfs(node.right) 
        
        dfs(root) 

        return vals[k-1]
            