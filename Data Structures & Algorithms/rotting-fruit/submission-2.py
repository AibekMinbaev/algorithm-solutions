class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid) 
        M = len(grid[0]) 

        q = collections.deque([])

        fresh = 0 
        for i in range(N): 
            for j in range(M): 
                if grid[i][j] == 1: 
                    fresh += 1 
                elif grid[i][j] == 2: 
                    q.append((i,j)) 
    
        def is_valid(i,j): 
            return i > -1 and i < N and j > -1 and j < M
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        time = 0 
        while fresh > 0 and q: 
            ln = len(q)
            for _ in range(ln): 
                i,j = q.popleft() 

                for d_i, d_j in dirs: 
                    new_i = i + d_i 
                    new_j = j + d_j 

                    if is_valid(new_i, new_j) and grid[new_i][new_j] == 1: 
                        # if allowed to modify the grid, else must use seen set 
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j)) 
                        fresh -= 1 
            time += 1 
        return time if fresh == 0 else -1 

        # BFS solution 
        # T: O(m * n) 
        # S: O(m * n) 



