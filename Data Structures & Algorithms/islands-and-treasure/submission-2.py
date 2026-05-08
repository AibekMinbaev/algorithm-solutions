class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        n, m = len(grid), len(grid[0]) 

        def bfs(r,c): 
            dist = 1 
            dq = deque([deque([(r,c)])])  
            
            while dq: 

                cur_level = dq.popleft() 
                new_level = deque()
                while cur_level: 
                    r,c = cur_level.popleft() 
                    for dr, dc in [[1,0], [-1,0], [0,-1], [0,1]]: 
                        nr, nc = r + dr, c + dc 
                        if (0 <= nr < n and 0 <= nc < m) and grid[nr][nc] != -1: 
                            if dist < grid[nr][nc]: 
                                grid[nr][nc] = dist 
                                new_level.append((nr,nc)) 
                if new_level:
                    dq.append(new_level) 
                dist += 1 
        

        for r in range(n): 
            for c in range(m): 
                if grid[r][c] == 0: 
                    bfs(r,c) 
        

        