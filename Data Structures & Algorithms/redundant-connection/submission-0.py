class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 

        # DSU (Union Find) 
        root = {} 

        def find(x: int) -> int: 
            if root[x] != x:
                root[x] = find(root[x]) 
            return root[x] 


        for a, b in edges:
            if a not in root: 
                root[a] = a 
            
            if b not in root: 
                root[b] = b 
            
            root_a = find(a) 
            root_b = find(b) 
            if root_a == root_b: 
                return [a, b] 
            
            root[root_a] = root_b 
        

        