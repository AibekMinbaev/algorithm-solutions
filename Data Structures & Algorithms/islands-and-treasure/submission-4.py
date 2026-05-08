class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        n, m = len(grid), len(grid[0]) 

        cur_lvl = deque()
        for r in range(n): 
            for c in range(m): 
                if grid[r][c] == 0:
                    cur_lvl.append((r,c)) 
        
        dist = 1 
        while True: 
            new_lvl = deque()

            while cur_lvl: 
                r,c = cur_lvl.popleft() 

                for dr, dc in [[1,0], [-1,0], [0,-1], [0,1]]: 
                    nr, nc = r + dr, c + dc 
                    if (0 <= nr < n and 0 <= nc < m) and grid[nr][nc] != -1: 
                        if dist < grid[nr][nc]: 
                            grid[nr][nc] = dist 
                            new_lvl.append((nr,nc)) 
            if not new_lvl: 
                return 
            cur_lvl = new_lvl 
            dist += 1 



        # # a little differnt multi-source solution 
        # def bfs(r,c): 
        #     dist = 1 
        #     cur_lvl = deque([(r,c)])  
            
        #     while True: 
        #         new_lvl = deque()
                
        #         while cur_lvl:                 
        #             r,c = cur_lvl.popleft() 
        #             for dr, dc in [[1,0], [-1,0], [0,-1], [0,1]]: 
        #                 nr, nc = r + dr, c + dc 
        #                 if (0 <= nr < n and 0 <= nc < m) and grid[nr][nc] != -1: 
        #                     if dist < grid[nr][nc]: 
        #                         grid[nr][nc] = dist 
        #                         new_lvl.append((nr,nc)) 
                    
        #         if not new_lvl:
        #             return 
        #         cur_lvl = new_lvl 
        #         dist += 1 
                
        # for r in range(n): 
        #     for c in range(m): 
        #         if grid[r][c] == 0: 
        #             bfs(r,c) 
        

        