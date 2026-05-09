class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen; 

        for(int i=0; i < nums.size(); i++){
            int a = nums[i];
            int b = target - a;
            cout<<a<<endl;
            if(seen.contains(b)){
                int j = seen[b];
                return {j, i};
            }
            seen[a] = i;
        }
    }
};
