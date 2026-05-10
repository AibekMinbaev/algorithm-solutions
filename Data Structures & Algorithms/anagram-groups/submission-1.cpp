class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> mp; 

        for(const string& s: strs){
            array<int, 26> freq = getFreq(s); 
            mp[freq].push_back(s); 
        }

        vector<vector<string>> res; 
        for(auto const& [key, val]: mp){
            res.push_back(val);
        }

        return res;
    }

    array<int, 26> getFreq(const string& s){
        array<int, 26> freq = {};
        
        for(auto ch: s){
            freq[ch - 'a']++;
            // int ord = (int)ch - 97;
            // freq[ord]++;
        }
        return freq; 
    }
};
