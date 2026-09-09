# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: 
        if not head.next: 
            return 
            
        # time: n 
        # space: 1

        def get_len(head: Optional[ListNode]) -> ListNode: 
            tmp = head 
            cnt = 0 
            while tmp: 
                cnt += 1 
                tmp = tmp.next
            return cnt 
        
        def reverse(head: Optional[ListNode]) -> ListNode: 
            prev = None 
            curr = head
            while curr: 
                nxt = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nxt 
            return prev 

        # def divide(head: Optional[ListNode], n: int) -> Tuple(ListNode, ListNode):
        #     h1 = h2 = head 

        #     prev = None 
        #     cnt = 0 
        #     while cnt < n // 2: 
        #         cnt += 1 
        #         prev = h2
        #         h2 = h2.next 

        #     prev.next = None 
        #     return (h1, h2) 

        def divide(head: Optional[ListNode]) -> Tuple(ListNode, ListNode): 
            slow = fast = head 

            prev = None 
            while fast and fast.next: 
                prev = slow 
                slow = slow.next 
                fast = fast.next.next 
            
            prev.next = None 
            return (head, slow) 

        
        # ln = get_len(head) 
        # if ln <= 2: 
        #     return 

        l, r = divide(head) 
        r = reverse(r) 
        
        while l and r: 
            l_nxt = l.next
            l.next = r 
            l = l_nxt 

            r_nxt = r.next 
            if l: r.next = l 
            r = r_nxt
    
        