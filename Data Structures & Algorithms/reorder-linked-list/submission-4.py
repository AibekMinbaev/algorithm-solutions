# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: 
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

        def divide(head: Optional[ListNode], n: int) -> Tuple(ListNode, ListNode):
            h1 = h2 = head 

            prev = None 
            cnt = 0 
            while cnt < n // 2: 
                cnt += 1 
                prev = h2
                h2 = h2.next 

            prev.next = None 
            return (h1, h2) 
        
        ln = get_len(head) 
        if ln <= 2: 
            return 

        l, r = divide(head, ln) 
        r = reverse(r) 
        
        while l and r: 
            l_nxt = l.next
            l.next = r 
            l = l_nxt 

            r_nxt = r.next 
            if l: r.next = l 
            r = r_nxt
    
        # # Brute Force:
        # # time: n 
        # # space: n 

        # arr = [] 
        # while head: 
        #     arr.append(head) 
        #     head = head.next 
        
        # l, r = 0, len(arr) - 1 
        # while l < r: 
        #     arr[l].next = arr[r] 
        #     l += 1 
        #     arr[r].next = arr[l]
        #     r -= 1 
        
        # arr[l].next = None 
        
        