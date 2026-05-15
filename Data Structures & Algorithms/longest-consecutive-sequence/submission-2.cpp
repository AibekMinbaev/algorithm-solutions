class Solution {
public:
    int longestConsecutive(vector<int>& nums) { 
        set<int> mySet(nums.begin(), nums.end()); 

        int res = 0; 
        for(int num: nums){
            if(!mySet.contains(num-1)){
                int curr = 1; 
                while(mySet.contains(num+1)){
                    curr++;
                    num++;
                }
                res = max(res, curr);
            }
        }
        return res; 
    }
};
