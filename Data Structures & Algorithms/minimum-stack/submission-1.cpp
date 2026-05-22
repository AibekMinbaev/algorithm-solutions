class MinStack {
public:
    stack<pair<int, int>> st; 
    MinStack() {
    
    }
    
    void push(int val) {
        pair<int, int> curr_pair = {val, val}; 
        if(!st.empty()){
            pair<int, int> last_pair = st.top(); 
            curr_pair.second = min(val, last_pair.second);
        }
        st.push(curr_pair);
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        pair<int, int> curr_pair = st.top();
        return curr_pair.first;
    }
    
    int getMin() {
        pair<int, int> curr_pair = st.top();
        return curr_pair.second;
        
    }
};
