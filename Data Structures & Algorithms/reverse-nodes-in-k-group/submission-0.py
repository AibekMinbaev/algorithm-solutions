# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        dummy = ListNode() 
        res = dummy 
       
        prev_node = None 
        first_node = None 
        
        cnt = 0
        curr = head 
        while curr: 
            cnt += 1 

            if cnt == 1: 
                first_node = curr 
            
            next_node = curr.next 
            curr.next = prev_node 
            prev_node = curr 
            curr = next_node 

            if cnt == k: 
                dummy.next = prev_node 
                dummy = first_node 
                cnt = 0 
                prev_node = None 
            
        if prev_node:
            curr = prev_node 
            prev_node = None 
            while curr: 
                next_node = curr.next 
                curr.next = prev_node 
                prev_node = curr 
                curr = next_node 
            dummy.next = prev_node 
            
        return res.next 


        
