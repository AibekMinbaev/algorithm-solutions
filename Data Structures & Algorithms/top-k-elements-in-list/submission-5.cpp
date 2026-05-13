class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mp; 
        for(auto const& num: nums){
            mp[num]++;
        };

        vector<vector<int>> bucket; 
        for(int i = 0; i < nums.size()+1; i++){ 
            vector<int> s_bucket; 
            bucket.push_back(s_bucket);
        }

        for(auto const& [key, val]: mp){
            bucket[val].push_back(key);
        } 

        vector<int> res; 
        for(int i = bucket.size()-1; i > -1; i --){
            for(auto const& v: bucket[i]){
                res.push_back(v);
            };
            if(res.size() == k){
                break;
            }
        }
        return res; 
    }
};
