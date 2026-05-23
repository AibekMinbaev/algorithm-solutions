class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pos_sp;
        int n = position.size(); 
        for(int i = 0; i < n; i++){
            pos_sp.push_back({position[i], speed[i]});
        }

        sort(pos_sp.begin(), pos_sp.end());

        stack<double> res; 
        for(auto elem: pos_sp){
            int pos = elem.first; 
            int sp = elem.second; 
            int miles = target - pos; 
            double time = (double)miles / sp; 
            while(!res.empty() && res.top() <= time){
                res.pop();
            }
            res.push(time);
        }
        return res.size();
    }
};
