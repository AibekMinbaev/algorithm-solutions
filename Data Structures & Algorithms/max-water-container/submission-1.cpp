class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1; 
        int res = 0; 
        while(l < r){
            int h = min(heights[l], heights[r]); 
            int w = r - l; 
            res = max(res, h * w); 

            if(heights[l] <= heights[r]){
                l++; 
            }else{
                r--; 
            }
        }
        return res; 
    }
};
