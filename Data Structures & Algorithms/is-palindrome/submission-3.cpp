class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0; 
        int r = s.size() - 1; 

        while (l < r){
            while(l < r && !alphaNum(s[l])){
                l++; 
            }
            while(l < r && !alphaNum(s[r])){
                r--; 
            }
            if(tolower(s[l]) != tolower(s[r])){
                return false; 
            }
            l++; 
            r--; 
        }
        return true; 
    }

    bool alphaNum(char c){
        return ('A' <= c && c <= 'Z' ||  'a' <= c && c <= 'z' || '0' <= c && c <= '9');
    }

};
