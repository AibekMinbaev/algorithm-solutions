class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q; 
        int fresh = 0; 
        int time = 0; 

        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 1){
                    fresh++; 
                } 

                if(grid[i][j] == 2){
                    q.push({i, j});
                }
            }
        } 

        vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; 

        while (fresh > 0 && !q.empty()){
            int ln = q.size(); 
            for (int _ = 0; _ < ln; _++){
                pair<int, int> curr = q.front(); 
                q.pop(); 
                int i = curr.first; 
                int j = curr.second; 

                for (pair<int, int>& dir: dirs){
                    int row = i + dir.first; 
                    int col = j + dir.second; 
                    if (row >= 0 && row < grid.size() && col >= 0 && col < grid[0].size()
                    && grid[row][col] == 1){
                        grid[row][col] = 2;
                        q.push({row, col});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time: -1;
    }
};
