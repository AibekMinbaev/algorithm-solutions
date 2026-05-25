# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Iterative BFS solution 
        # time: O(n) 
        # space: O(n) 

        p_q = deque([p]) 
        q_q = deque([q]) 

        while p_q and q_q: 
            p = p_q.popleft() 
            q = q_q.popleft() 

            if not p and not q: 
                continue 

            if not p or not q: 
                return False

            if p.val != q.val: 
                return False 
            
            p_q.append(p.left) 
            p_q.append(p.right) 

            q_q.append(q.left) 
            q_q.append(q.right) 

        # if p_q or q_q: 
        #     return False 
        
        return True 



        
        
        # Iterative DFS solution 
        # time: O(n) 
        # space: O(n)

        # stack = [(p, q)] 

        # while stack: 
        #     p, q = stack.pop() 

        #     if not p and not q: 
        #         continue 
                
        #     if not p or not q: 
        #         return False 
            
        #     if q.val != p.val: 
        #         return False 
            
        #     stack.append((p.left, q.left)) 
        #     stack.append((p.right, q.right)) 
        
        # return True 

        
        
        # # Recursive DFS solution 
        # # time: n
        # # space: n in worst case

        # if not p and not q: 
        #     return True 
        
        # if not p or not q: 
        #     return False 
        
        # if p.val != q.val: 
        #     return False 
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 