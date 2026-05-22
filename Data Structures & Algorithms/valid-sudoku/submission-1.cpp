class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int, unordered_set<char>> rows; 
        map<int, unordered_set<char>> cols; 
        map<pair<int, int>, unordered_set<char>> boxes; 

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.'){
                    continue;
                }
                pair<int, int> box_id= {r / 3, c / 3};
                if(rows[r].contains(board[r][c]) || cols[c].contains(board[r][c]) || boxes[box_id].contains(board[r][c])){
                    return false; 
                }
                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]); 
                boxes[box_id].insert(board[r][c]);
            }
        }
        return true;
    }
};
