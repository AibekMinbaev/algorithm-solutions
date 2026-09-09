class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0]) 


        seen = set() 
        def dfs(r: int, c: int) -> None: 
            if (r,c) in seen: 
                return 
            
            seen.add((r,c)) 
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0,1]]: 
                nr, nc = r + dr, c + dc 

                if nr < 0 or nr >= R or nc < 0 or nc >= C: 
                    continue 
                
                if grid[nr][nc] == "0": 
                    continue 
                
                if (nr, nc) in seen:  
                    continue 
                
                dfs(nr, nc) 
            
        cnt = 0 
        for r in range(R): 
            for c in range(C): 
                if grid[r][c] == "1" and (r,c) not in seen: 
                    cnt += 1
                    dfs(r,c) 
        return cnt 

