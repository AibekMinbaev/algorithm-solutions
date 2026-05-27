# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        # DFS 
        # time: O(n) 
        # space: O(n) 
        def dfs(node, mn, mx): 
            if not node: 
                return True 
                
            return (mn < node.val < mx  
                and dfs(node.left, mn, node.val) 
                and dfs(node.right, node.val, mx))

        return dfs(root, float("-inf"), float("inf")) 



# left max < root.val < right min

#             5 
#    1.              2. 
#                        6 

        
        # # Brute force solution 
        # # time: n 
        # # space: n 

        # vals = [] 

        # def dfs(node): 
        #     if not node: 
        #         return 
        #     dfs(node.left) 
        #     vals.append(node.val) 
        #     dfs(node.right)  
        
        # dfs(root) 

        # for i in range(1, len(vals)): 
        #     if vals[i-1] >= vals[i]: 
        #         return False 
        # return True 



