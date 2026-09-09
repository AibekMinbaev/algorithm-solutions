# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: 
        # time: n 
        # space: 1
        if not head.next: 
            return 

        def reverse(head: Optional[ListNode]) -> ListNode: 
            prev = None 
            curr = head
            while curr: 
                nxt = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nxt 
            return prev 

        def divide(head: Optional[ListNode]) -> Tuple(ListNode, ListNode): 
            slow = fast = head 

            prev = None 
            while fast and fast.next: 
                prev = slow 
                slow = slow.next 
                fast = fast.next.next 
            
            prev.next = None 
            return (head, slow) 

        l, r = divide(head) 
        r = reverse(r) 
        
        while l and r: 
            l_nxt = l.next
            l.next = r 
            l = l_nxt 

            r_nxt = r.next 
            if l: r.next = l 
            r = r_nxt
    
        