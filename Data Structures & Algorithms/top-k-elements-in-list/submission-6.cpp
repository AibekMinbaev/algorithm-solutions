class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mp; 
        vector<vector<int>> bucket(nums.size()+1); 

        for(const auto& num: nums){
            mp[num]++;
        };

        for(const auto& e: mp){
            bucket[e.second].push_back(e.first);
        } 

        vector<int> res; 
        for(int i = bucket.size()-1; i > -1; i--){
            for(int n: bucket[i]){
                res.push_back(n);
                if(res.size() == k){
                    return res;
                };
            };
        }
        return res; 
    }
};
