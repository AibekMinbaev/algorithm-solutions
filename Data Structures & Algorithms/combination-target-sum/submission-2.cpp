class Solution {
public:
    vector<vector<int>> res; 
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> arr; 
        dfs(nums, 0, arr, target); 
        return res; 
    }

public: 
    void dfs(vector<int>& nums, int i, vector<int> arr, int t){
        if(t == 0){
            res.push_back(arr); 
            return; 
        } 

        if(i >= nums.size() || t < 0){
            return; 
        } 

        arr.push_back(nums[i]); 
        dfs(nums, i, arr, t - nums[i]); 
        arr.pop_back();
        dfs(nums, i+1, arr, t);
    } 
};
