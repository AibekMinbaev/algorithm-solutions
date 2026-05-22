class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        rows = collections.defaultdict(set) 
        cols = collections.defaultdict(set) 
        big_matrix = collections.defaultdict(set) 

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                num = board[r][c] 
                if not num.isnumeric(): 
                    continue 
                    
                n_r, n_c = r // 3, c // 3
                if num in rows[r] or num in cols[c] or num in big_matrix[(n_r, n_c)]: 
                    print(rows, cols, big_matrix)
                    return False
                rows[r].add(num) 
                cols[c].add(num)
                big_matrix[(n_r, n_c)].add(num)
        return True 