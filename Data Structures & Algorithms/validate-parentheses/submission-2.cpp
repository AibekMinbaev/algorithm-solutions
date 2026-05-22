class Solution {
public:
    bool isValid(string s) {
        stack<char> st; 
        unordered_map<char, char> mp= {
            {')', '('}, 
            {'}', '{'}, 
            {']', '['}, 
        }; 

        for(char ch: s){
            if(!mp.contains(ch)){
                st.push(ch); 
            } else{
                if(!st.empty() && st.top() == mp[ch]){
                    st.pop(); 
                } else {
                    return false;
                }
            }
        }
        return st.empty();
    }
};
