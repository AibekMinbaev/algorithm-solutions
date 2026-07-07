class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        root = [i for i in range(n)] 

        def find(x: int) -> int: 
            if root[x] == x: 
                return x 
            return find(root[x]) 
             
        for a, b in edges: 
            root[find(a)] = find(b) 
        
        res = 0 
        for node in range(n): 
            if root[node] == node: 
                res += 1 

        return res  


        # # DFS solution 
        # # time: O(V + E)
        # # space: O(V + E) 
        
        # adj = defaultdict(list) 

        # for a, b in edges: 
        #     adj[a].append(b) 
        #     adj[b].append(a) 
        
        # visited = set() 
        # def dfs(node: int): 
        #     if node in visited: 
        #         return 
            
        #     visited.add(node) 
        #     for nei in adj[node]: 
        #         dfs(nei) 

        # cnt = 0 
        # for node in range(n): 
        #     if node not in visited: 
        #         cnt += 1 
        #         dfs(node) 
        
        # return cnt


