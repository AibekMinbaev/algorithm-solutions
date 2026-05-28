class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N, M = len(grid), len(grid[0]) 

        dirs: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_valid(r: int, c: int) -> bool: 
            return r > -1 and r < N and c > -1 and c < M 

        seen: Set[Tuple[int, int]] = set()
        def dfs(r: int, c: int) -> None: 
            
            seen.add((r,c)) 

            for d_r, d_c in dirs: 
                new_r, new_c = r + d_r, c + d_c 
                
                if ((new_r, new_c) in seen 
                    or not is_valid(new_r, new_c) 
                    or grid[new_r][new_c] == "0"): 
                    continue 
                
                dfs(new_r, new_c) 

        res = 0 
        for r in range(N): 
            for c in range(M): 
                if grid[r][c] == "1" and (r,c) not in seen:
                    res += 1  
                    dfs(r,c) 
        return res 
        

