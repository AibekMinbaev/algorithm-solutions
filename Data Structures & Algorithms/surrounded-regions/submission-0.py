class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N, M = len(board), len(board[0]) 

        def is_on_board(r: int, c: int) -> bool: 
            return r == 0 or r == N -1 or c == 0 or c == M - 1 
        
        def is_valid(r: int, c: int) -> bool: 
            return r > -1 and r < N and c > -1 and c < M 

        on_board: List[Tuple[int, int]] = [] 
        for r in range(N): 
            for c in range(M): 
                if is_on_board(r,c) and board[r][c] == "O": 
                    on_board.append((r,c)) 
        
        visited: Set[Tuple[int, int]] = set() 
        def dfs(r: int, c: int):
            if (r, c) in visited: 
                return 
            
            visited.add((r,c)) 
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                nr, nc = r + dr, c + dc 
                if not is_valid(nr, nc) or board[nr][nc] != "O":
                    continue 
                
                dfs(nr, nc) 

        for (r, c) in on_board: 
            dfs(r, c) 
        
        for r in range(N): 
            for c in range(M): 
                if board[r][c] == "O" and (r,c) not in visited: 
                    board[r][c] = "X"


