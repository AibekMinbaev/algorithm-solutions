class Node: 
    def __init__(self): 
        self.children = {}
        self.is_word = False 

class PrefixTree:

    def __init__(self):
        self.trie = {} 

    def insert(self, word: str) -> None: 

        level = self.trie 
        for i in range(len(word)): 
            ch = word[i] 

            if ch not in level: 
                level[ch] = Node() 

            if i == len(word)-1: 
                level[ch].is_word = True 

            level = level[ch].children 
        
    def search(self, word: str) -> bool: 
        level = self.trie 
        for i in range(len(word)): 
            ch = word[i] 
            if ch not in level: 
                return False 
            
            if i == len(word)-1 and not level[ch].is_word: 
                return False 

            level = level[ch].children 
        return True
        
    def startsWith(self, prefix: str) -> bool: 
        level = self.trie
        for ch in prefix: 
            if ch not in level: 
                return False 
            level = level[ch].children 
        return True 
        
        