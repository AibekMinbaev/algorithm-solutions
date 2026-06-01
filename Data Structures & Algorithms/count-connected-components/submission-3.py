class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        adj = defaultdict(list) 

        for a, b in edges: 
            adj[a].append(b) 
            adj[b].append(a) 
        
        visited = set() 
        def dfs(node: int): 
            if node in visited: 
                return 
            
            visited.add(node) 
            for nei in adj[node]: 
                dfs(nei) 

        cnt = 0 
        for node in adj.keys(): 
            if node not in visited: 
                cnt += 1 
                dfs(node) 
        
        return n - len(visited) + cnt


