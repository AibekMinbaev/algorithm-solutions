# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        
        def reverse_nodes(curr: Optional[ListNode], prev: Optional[ListNode]):
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt
            return curr, prev


        dummy = ListNode() 
        res = dummy
       
        prev = None 
        first_node = None 
        
        cnt = 0
        curr = head 
        while curr: 
            cnt += 1 

            if cnt == 1: 
                first_node = curr 
            
            curr, prev = reverse_nodes(curr, prev)
    
            if cnt == k: 
                dummy.next = prev 
                dummy = first_node 
                cnt = 0 
                prev = None 
            
        if prev:
            curr = prev 
            prev = None 
            while curr: 
                curr, prev = reverse_nodes(curr, prev) 
            dummy.next = prev 
            
        return res.next 



