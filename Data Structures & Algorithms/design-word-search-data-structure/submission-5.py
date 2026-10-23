class WordDictionary:

    def __init__(self): 
        self.top_level = {}

    def addWord(self, word: str) -> None:
        curr_level = self.top_level
        for ch in word: 
            if ch not in curr_level: 
                curr_level[ch] = {} 
            curr_level = curr_level[ch] 
        curr_level["*"] = {}
    
    def dfs(self, word, idx, d): 
        if idx == len(word): 
            if "*" not in d: 
                return False 
            return True 
        
        if word[idx] == ".": 
            for key in d.keys(): 
                if self.dfs(word, idx + 1, d[key]): 
                    return True 
            return False 

        if word[idx] not in d: 
            return False 
        return self.dfs(word, idx + 1, d[word[idx]])


    def search(self, word: str) -> bool: 
        return self.dfs(word, 0, self.top_level)

            


