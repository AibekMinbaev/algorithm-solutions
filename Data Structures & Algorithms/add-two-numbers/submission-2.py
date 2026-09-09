# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        prev = dummy = ListNode(0)
        
        carry = 0 
        while l1 or l2 or carry: 
            sm = carry 

            if l1:sm += l1.val 
            if l2: sm += l2.val 

          
            node = ListNode(sm % 10)
            carry = sm // 10  

            prev.next = node 
            prev = node 

            if l1: l1 = l1.next 
            if l2: l2 = l2.next 

        return dummy.next 
    




        