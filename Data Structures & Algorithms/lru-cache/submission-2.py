class Node: 
    def __init__(self, key: int, val: int, prev = None, next = None): 
        self.key = key 
        self.val = val 
        self.prev = prev 
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int): 
        self.capacity = capacity 
        self.mp = {} 
        self.lru = None
        self.curr = None

    def get(self, key: int) -> int: 
        if key not in self.mp: 
            return -1 
        
        node = self.mp[key] 

        # update self.lru 
        if node == self.lru and self.lru.next: 
            self.lru = self.lru.next 
        
        if node != self.curr: 
            if node.next: node.next.prev = node.prev  
            if node.prev: node.prev.next = node.next 

            self.curr.next = node 
            node.prev = self.curr 

            node.next = self.curr.next 
            self.curr = node 
        
        return node.val 
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp: 
            node = self.mp[key] 
            node.val = value 
        
             # update self.lru 
            if node == self.lru and self.lru.next: 
                self.lru = self.lru.next 
            
            if node != self.curr: 
                if node.next: node.next.prev = node.prev  
                if node.prev: node.prev.next = node.next 

                self.curr.next = node
                node.prev = self.curr 
                node.next = self.curr.next 
                self.curr = node 
        else: 
            if len(self.mp) >= self.capacity: 
                #cleanup first 
                lru = self.lru 

                self.lru = self.lru.next 
                if lru == self.curr: 
                    self.curr = None 

                del self.mp[lru.key]

                if lru.prev: lru.prev.next = lru.next 
                if lru.next: lru.next.prev = lru.prev

                lru.prev = lru.next = None 
            
            new_node = Node(key, value) 
            self.mp[key] = new_node 

            if self.curr: 
                self.curr.next = new_node 
                new_node.prev = self.curr 
            self.curr = new_node 

            if not self.lru: 
                self.lru = new_node 
        