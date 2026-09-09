# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode(0) 
        prev = dummy
        tmp = 0 

        while l1 and l2: 
            sm = (l1.val + l2.val + tmp)
            tmp = sm // 10 
            new_val = sm % 10
            node = ListNode(new_val) 
            prev.next = node 
            prev = node 

            l1 = l1.next 
            l2 = l2.next 
        
        l3 = l1 if l1 else l2

        while l3:  
            sm = l3.val + tmp 
            tmp = sm // 10 
            new_val = sm % 10 
            node = ListNode(new_val) 
            prev.next = node 
            prev = node 
            l3 = l3.next 
        
        if tmp: 
            prev.next = ListNode(tmp)

        return dummy.next 
    




        