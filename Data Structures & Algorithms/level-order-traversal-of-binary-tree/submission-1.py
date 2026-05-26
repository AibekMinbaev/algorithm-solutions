# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS solution 
        if not root: 
            return [] 

        mp = defaultdict(list) 
        stack = [(root, 0)] 

        while stack: 
            node, level = stack.pop() 
            mp[level].append(node.val) 

            if node.right: 
                stack.append((node.right, level+1)) 
            
            if node.left: 
                stack.append((node.left, level+1)) 
            
        return list(mp.values())

        # # BFS solution 
        # # time: O(n) 
        # # space: O(n) 

        # if not root: 
        #     return [] 
        # q = deque([root]) 

        # res = [] 
        # while q:
        #     level = [] 
        #     for _ in range(len(q)): 
        #         node = q.popleft() 
        #         level.append(node.val) 

        #         if node.left:
        #             q.append(node.left)
                
        #         if node.right: 
        #             q.append(node.right) 
        #     res.append(level)
        # return res 
