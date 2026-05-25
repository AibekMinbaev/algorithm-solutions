# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 

        # Iterative DFS solution 
        # time: O(n) 
        # space: O(n) 
        
        if not root: 
            return True 

        # Iterative DFS 
        mp = {None: 0}

        stack = [root] 
        while stack: 
            node = stack[-1] 

            if node.left and node.left not in mp: 
                stack.append(node.left) 
            elif node.right and node.right not in mp: 
                stack.append(node.right) 
            else: 
                node = stack.pop()
                if abs(mp[node.left] - mp[node.right]) > 1: 
                    return False 
                
                mp[node] = 1 + max(mp[node.left], mp[node.right])

        return True 
                
        # # Recursive DFS 
        # # time: O(n) 
        # # space: O(h) h is the height of the tree, recursion stack 
        # res = True 
        # def dfs(root): 
        #     nonlocal res; 

        #     if not root: 
        #         return 0 
            
        #     left = dfs(root.left) 
        #     right = dfs(root.right) 

        #     res = res and abs(left - right) <= 1
        #     return 1 + max(left, right)
        
        # dfs(root)
        # return res 
