class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def is_valid(r: int, c: int) -> bool: 
            return r > -1 and r < N and c > -1 and c < M 
        
        dirs = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        
        N, M = len(grid), len(grid[0]) 

        q = deque([]) 
        fruit_cnt = 0 
        for r in range(N): 
            for c in range(M): 
                if grid[r][c] == 2: 
                    q.append((r,c)) 
                elif grid[r][c] == 1: 
                    fruit_cnt += 1  

        mins = 0 
        while fruit_cnt > 0 and q: 
            for _ in range(len(q)): 
                r, c = q.popleft() 

                for d_r, d_c in dirs: 
                    new_r, new_c = r + d_r, c + d_c 
                    
                    if not is_valid(new_r, new_c) or grid[new_r][new_c] != 1: 
                        continue 
                    
                    grid[new_r][new_c] = 2 
                    fruit_cnt -= 1 
                    q.append((new_r, new_c)) 
            mins += 1 
        
        return mins if fruit_cnt == 0 else -1 






