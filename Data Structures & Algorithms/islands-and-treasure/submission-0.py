class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        n, m = len(grid), len(grid[0]) 
        land = 2147483647 

        def bfs(r,c): 
            visited = set([(r,c)]) 

            cnt = 1 
            dq = deque([])
            q = deque([(r,c)])
            dq.append(q)    
            
            while dq: 

                q = dq.popleft() 
                new_q = deque()
                while q: 
                    r,c = q.popleft() 
                    for dr, dc in [[1,0], [-1,0], [0,-1], [0,1]]: 
                        nr, nc = r + dr, c + dc 
                        if (0 <= nr < n and 0 <= nc < m) and (nr,nc) not in visited and grid[nr][nc] != 0 and grid[nr][nc] != -1: 
                            if cnt < grid[nr][nc]: 
                                grid[nr][nc] = cnt 
                                new_q.append((nr,nc)) 
                                visited.add((nr,nc)) 
                if new_q:
                    dq.append(new_q) 
                cnt += 1 
        

        for r in range(n): 
            for c in range(m): 
                if grid[r][c] == 0: 
                    bfs(r,c) 
        

        