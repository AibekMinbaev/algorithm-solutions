class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 

        adj_list = [[] for i in range(n)]
        for n1, n2 in edges: 
            adj_list[n1].append(n2) 
            adj_list[n2].append(n1) 

        # dfs  
        visited = set() 
        def dfs(par, node): 
            if node in visited: 
                return False 

            visited.add(node) 
            for nei in adj_list[node]:
                if nei != par and not dfs(node, nei): 
                    return False   
            
            return True 

        # if cycle
        if not dfs(-1, 0): 
            return False 

        return len(visited) == n 
























        # # Union Find algo 
        # # 1st check 
        # if len(edges) != n - 1: 
        #     return False 

        # # 2nd check union find 
        # par = [i for i in range(n)] 
        # rank = [0] * n 
        # def find(n): 
        #     while par[n] != n: 
        #         n = par[n] 
        #     return n 
        
        # def union(n1, n2): 
        #     p1, p2 = find(n1), find(n2) 

        #     if p1 == p2:
        #         return False 

        #     if rank[p1] > rank[p2]: 
        #         par[p2] = p1 
        #         rank[p1] += rank[p2] 
        #     else:
        #         par[p1] = p2 
        #         rank[p2] += rank[p1] 

        #     return True 

        # for n1, n2 in edges: 
        #     if not union(n1, n2):
        #         return False 

        # return True  
        