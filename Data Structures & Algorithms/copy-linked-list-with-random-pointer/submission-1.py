"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None} 
        
        curr = head  
        while curr: 
            mp[curr] = Node(curr.val)  
            curr = curr.next 
        
        for k, v in mp.items(): 
            if not k: continue 
            
            v.next = mp[k.next] 
            v.random = mp[k.random]

        return mp[head]
        

