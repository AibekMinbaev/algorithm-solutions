# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative solution 
        stack = [root] 

        while stack: 
            r = stack.pop() 
            if not r:
                continue 

            r.left, r.right = r.right, r.left 
            stack.append(r.left) 
            stack.append(r.right) 
        
        return root 

        # # recursive solution
        # def helper(root): 
        #     if not root: 
        #         return 

        #     root.left, root.right = root.right, root.left
        #     helper(root.left) 
        #     helper(root.right)  

        # helper(root) 
        # return root 

        # # time: O(n) 
        # # space: O(n) because function stack 
        