class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) { 
        vector<int> pref; 

        int prefix = 1;
        for(int num: nums){
            prefix *= num;
            pref.push_back(prefix);
        }; 

        vector<int> suff(nums.size()); 
        int suffix = 1; 
        for(int i=nums.size()-1; i > -1; i--){
            suffix *= nums[i];
            suff[i] = suffix;
        };

        vector<int> res; 
        for(int i=0; i<nums.size(); i++){
            int a = 1; 
            int b = 1; 
            if(i - 1 >= 0){
                a = pref[i-1];
            };
            if(i + 1 < nums.size()){
                b = suff[i+1];
            };
            res.push_back(a * b);
        }
        return res; 
    }
};

