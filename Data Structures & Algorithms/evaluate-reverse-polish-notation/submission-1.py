class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        st = [] 

        for t in tokens: 
            if t == "+": 
                b = st.pop() 
                a = st.pop() 
                st.append(a + b)
            elif t == "-": 
                b = st.pop() 
                a = st.pop() 
                st.append(a - b) 
            elif t == "*": 
                b = st.pop() 
                a = st.pop() 
                st.append(a * b) 
            elif t == "/": 
                b = st.pop() 
                a = st.pop() 
                st.append(int(a / b)) 
            else: 
                st.append(int(t)) 
        return st[0]