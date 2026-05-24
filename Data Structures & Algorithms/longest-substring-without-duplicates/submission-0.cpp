class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        unordered_set<char> seen;
        int l = 0; 
        for(int r = 0; r < s.size(); r++){
            while(seen.find(s[r]) != seen.end()){
                seen.erase(s[l]); 
                l += 1; 
            }
            seen.insert(s[r]);
            res = max(res, r - l + 1);
        }
        return res; 
    }
}; 

