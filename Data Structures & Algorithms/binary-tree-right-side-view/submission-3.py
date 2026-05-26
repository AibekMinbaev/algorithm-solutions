# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        # BFS recursive, with a trick 

        res = [] 

        def dfs(node, depth): 
            if not node: 
                return 
            
            if len(res) == depth: 
                res.append(node.val) 
            
            dfs(node.right, depth + 1) 
            dfs(node.left, depth + 1) 

        dfs(root, 0) 
        return res 
        
        # Iterative BFS 
        # time: O(n) 
        # space: O(n) 

        # if not root: 
        #     return [] 
        
        # mp = defaultdict(int) 
        # stack = [(root, 0)] 

        # while stack: 
        #     node, level = stack.pop() 
        #     mp[level] = node.val 

        #     if node.right: 
        #         stack.append((node.right, level+1)) 
            
        #     if node.left: 
        #         stack.append((node.left, level+1)) 
            
        # res = sorted(mp.items(), key=lambda k: k[0]) 
        # res = [val for key, val in res] 
        # return res 


        # BFS solution 
        # time:  O(n) 
        # space: O(n) 
        # if not root: 
        #     return [] 

        # q = deque([root]) 

        # res = [] 

        # while q: 
        #     right_val = None 
        #     for _ in range(len(q)): 
        #         node = q.popleft()
        #         right_val = node.val 

        #         if node.left: 
        #             q.append(node.left) 
        #         if node.right: 
        #             q.append(node.right) 
            
        #     res.append(right_val) 
        # return res 

