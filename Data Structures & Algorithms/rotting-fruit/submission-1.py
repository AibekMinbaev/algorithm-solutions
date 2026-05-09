class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid) 
        M = len(grid[0]) 

        q = collections.deque([])

        f = 0 
        for i in range(N): 
            for j in range(M): 
                if grid[i][j] == 1: 
                    f += 1 
                elif grid[i][j] == 2: 
                    q.append((i,j)) 
        
        if f == 0: 
            return 0 
            
        def is_valid(i,j): 
            return i > -1 and i < N and j > -1 and j < M


        seen = set() 
        mins = 0 
        while q: 
            mins += 1 
            ln = len(q)
            for _ in range(ln): 
                i,j = q.popleft() 
                seen.add((i,j)) 

                if is_valid(i+1,j) and (i+1, j) not in seen and grid[i+1][j] == 1: 
                    q.append((i+1, j))
                    seen.add((i+1,j))
                    f -= 1 

                if is_valid(i-1,j) and (i-1, j) not in seen and grid[i-1][j] == 1: 
                    q.append((i-1, j)) 
                    seen.add((i-1,j))
                    f -= 1 
                
                if is_valid(i,j+1) and (i,j+1) not in seen and grid[i][j+1] == 1: 
                    q.append((i, j+1))
                    seen.add((i,j+1)) 
                    f -= 1 

                if is_valid(i,j-1) and (i, j-1) not in seen and grid[i][j-1] == 1: 
                    q.append((i, j-1)) 
                    seen.add((i,j-1))
                    f -= 1 
        return mins-1 if f == 0 else -1 




