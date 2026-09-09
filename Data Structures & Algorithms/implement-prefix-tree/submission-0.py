class PrefixTree:

    def __init__(self):
        self.words = set() 
        self.pref = {} 

    def insert(self, word: str) -> None: 
        self.words.add(word) 

        level = self.pref 
        for ch in word: 
            if ch not in level: 
                level[ch] = {} 
            level = level[ch] 
        
    def search(self, word: str) -> bool: 
        return True if word in self.words else False
        
    def startsWith(self, prefix: str) -> bool: 
        level = self.pref 
        for ch in prefix: 
            if ch not in level: 
                return False 
            level = level[ch] 
        return True 
        
        