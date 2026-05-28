class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0]) 
        dirs: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0,1)]
        seen: List[Tuple[int, int]] = set()
        
        def is_valid(r: int, c: int) -> bool: 
            return r > -1 and r < N and c > -1 and c < M 

        def dfs(r: int, c: int, area: int = 1): 
            if grid[r][c] == 0: 
                return 0
    
            seen.add((r,c)) 
            area = 1 
            for d_r, d_c in dirs: 
                new_r, new_c = r + d_r, c + d_c 
                if (not is_valid(new_r, new_c) 
                    or (new_r, new_c) in seen):
                    continue 
                
                area += dfs(new_r, new_c)
            return area
                
        res = 0 
        for r in range(N): 
            for c in range(M): 
                if grid[r][c] == 1 and (r,c) not in seen: 
                    area = dfs(r,c)
                    res = max(res, area) 
        return res  
