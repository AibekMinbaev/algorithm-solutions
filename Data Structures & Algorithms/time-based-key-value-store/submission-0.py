class TimeMap:

    def __init__(self):
        self.mp = {} 

    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.mp: 
            self.mp[key] = [] 
        
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str: 
        res = "" 
        if key not in self.mp: 
            return res 
        
        values = self.mp[key] 
        l, r = 0, len(values) - 1 

        while l <= r: 
            m = (l + r) // 2 
            prev_time, value = values[m] 

            if prev_time <= timestamp: 
                res = value
                l = m + 1 
            else: 
                r = m - 1 
        return res 
        
            

        
