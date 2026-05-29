class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        N, M = len(grid), len(grid[0]) 
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_valid(r: int, c: int) -> bool: 
            return r > -1 and r < N and c > -1 and c < M

        q = deque([])
        for r in range(N): 
            for c in range(M): 
                if grid[r][c] == 0: 
                    q.append((r,c)) 
        dist = 1 
        while q: 
            for _ in range(len(q)): 
                r, c = q.popleft() 

                for dr, dc in dirs: 
                    nr, nc = r + dr, c + dc 

                    if not is_valid(nr, nc) or grid[nr][nc] != 2147483647: 
                        continue 
                    
                    grid[nr][nc] = dist
                    q.append((nr, nc)) 
            dist +=1 
        


#         # DFS solution 
#         # does not work because of these problems 
#         # - each depth call must have dist from prev paths 
#         # - even if we pass the prev min dist, it depends on which direction is visited first
#         N, M = len(grid), len(grid[0]) 

#         dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         def is_valid(r: int, c: int) -> bool: 
#             return r > -1 and r < N and c > -1 and c < M

#         seen = set()
#         def dfs(r: int, c: int, dist: int): 
#             if grid[r][c] == 0: 
#                 return 0

#             seen.add((r, c)) 
#             dist = dist + 1 if dist < 2147483647 else 2147483647
#             for d_r, d_c in dirs: 
#                 new_r, new_c = r + d_r, c + d_c 

#                 if not is_valid(new_r, new_c) or grid[new_r][new_c] == -1 or (new_r, new_c) in seen: 
#                     continue 
                
#                 dist = min(dist, dfs(new_r, new_c, dist) + 1)

#             grid[r][c] = dist
#             return dist 
            
#         for r in range(N): 
#             for c in range(M):
#                 if grid[r][c] == 2147483647: 
#                     dfs(r, c, 2147483647)


# [2147483647,    0,        -1]
# [2147483647, 2147483647, 2147483647]
# [2147483647,    -1,     2147483647]
        