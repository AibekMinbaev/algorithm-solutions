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
        mp = dict() 
        dummy = Node(0)
        
        curr = head  
        prev = dummy 
        while curr: 
            new_node = Node(curr.val) 
            prev.next = new_node  
            prev = new_node
            mp[curr] = new_node 
            curr = curr.next 
        
        for k, v in mp.items(): 
            if k.random: 
                v.random = mp[k.random]

        return dummy.next 
        

