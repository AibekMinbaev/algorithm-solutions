"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        



        # DFS solution 
        # time: V + E 
        # space: V
        
        if not node: 
            return None 

        seen = {}
        def dfs(node): 
            if node in seen: 
                return seen[node] 

            clone = Node(node.val) 
            seen[node] = clone
            
            clone.neighbors = [] 
            for nei in node.neighbors: 
                clone.neighbors.append(dfs(nei)) 
            return clone 

        clone = dfs(node) 
        return clone 