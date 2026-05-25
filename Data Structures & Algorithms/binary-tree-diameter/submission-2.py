# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 

        mp = {None: (0, 0)} 
        stack = [root] 
        while stack: 
            node = stack[-1] 

            if node.left and node.left not in mp: 
                stack.append(node.left) 
            elif node.right and node.right not in mp: 
                stack.append(node.right) 
            else: 
                node = stack.pop() 

                leftH, leftD = mp[node.left] 
                rightH, rightD = mp[node.right] 

                h = 1 + max(leftH, rightH) 
                d = max(leftH + rightH, leftD, rightD) 
                mp[node] = (h, d) 
            
        return mp[root][1]



 


        # # Recursive DFS solution 
        # # time: O(n) 
        # # space: O(h) where h is the length of the tree 
        # res = 0 

        # def dfs(root): 
        #     nonlocal res 
        #     if not root: 
        #         return 0
        #     left = dfs(root.left) 
        #     right = dfs(root.right) 

        #     res = max(res, left + right) 
        #     return max(left, right) + 1 

        # dfs(root) 
        # return res 
    
        # # Recursive brute force solution 
        # # time: O(n^2) 
        # # space: O(n^2) 

        # def getMaxEdges(root, d=0):
        #     if not root: 
        #         return d 
        #     return max(getMaxEdges(root.left, d+1), getMaxEdges(root.right, d+1))  
            
        
        # res = 0 
        # def dfs(root): 
        #     nonlocal res
            
        #     if not root: 
        #         return 
            
        #     res = max(res, getMaxEdges(root.left) + getMaxEdges(root.right))

        #     dfs(root.left) 
        #     dfs(root.right) 
            
        # dfs(root) 
        # return res 



        
