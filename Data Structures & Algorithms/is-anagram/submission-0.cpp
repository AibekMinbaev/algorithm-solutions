class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        map<char, int> freq; 
        for(auto ch: s){
            freq[ch]++; 
        }

        for(auto ch: t){
            if(!freq.contains(ch)){
                return false; 
            }
            freq[ch]--;
            if(freq[ch] < 0){
                return false; 
            }
        }
        return true;
    }
};
