class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 




        # Reverse the idea 
        # DFS 
        # time: n * m 
        # space: n * m

        N, M = len(heights), len(heights[0]) 
        pacific = set() 
        atlantic = set() 

        def dfs(r: int, c: int, ocean: Set[Tuple[int, int]]): 
            if (r,c) in ocean: 
                return 
            
            ocean.add((r,c))

            for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]: 
                nr, nc = r + dr, c + dc 

                if not (nr > -1 and nr < N and nc > -1 and nc < M): 
                    continue 
                
                if heights[nr][nc] < heights[r][c]: 
                    continue 
                
                dfs(nr, nc, ocean) 

        for r in range(N): 
            dfs(r, 0, pacific) 
            dfs(r, M - 1, atlantic) 

        for c in range(M): 
            dfs(0, c, pacific) 
            dfs(N - 1, c, atlantic) 
        
        res = [[r,c] for r,c in pacific & atlantic]
        return res 

        
        # # Brute Force DFS solution solution
        # N, M = len(heights), len(heights[0]) 

        # mp = {} 

        # visited = set() 
        # def dfs(r: int, c: int): 
        #     if (r,c) in mp: 
        #         return mp[(r,c)] 
            
        #     pacific, atlantic = False, False 

        #     if r == 0 or c == 0: 
        #         pacific = True 
            
        #     if r == N - 1 or c == M - 1: 
        #         atlantic = True 
            
        #     visited.add((r,c))
        #     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
        #         nr, nc = r + dr, c + dc 

        #         if not (nr > -1 and nr < N and nc > -1 and nc < M): 
        #             continue 
                
        #         if (nr, nc) in visited: 
        #             continue 
                
        #         if heights[r][c] < heights[nr][nc]: 
        #             continue 

        #         p, a = dfs(nr, nc) 
        #         if p: pacific = True 

        #         if a: atlantic = True 

        #         if pacific and atlantic: 
        #             break 

        #     visited.remove((r,c)) 
        #     return (pacific, atlantic)

        # for r in range(N): 
        #     for c in range(M): 
        #         mp[(r, c)] = dfs(r, c)
        
        # res = [] 
        # for (r, c), (p, a) in mp.items(): 
        #     if p and a: 
        #         res.append([r, c]) 
        # return res 
