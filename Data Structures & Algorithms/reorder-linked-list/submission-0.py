# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = [] 
        while head: 
            arr.append(head) 
            head = head.next 
        
        l, r = 0, len(arr) - 1 
        while l < r: 
            arr[l].next = arr[r] 
            l += 1 
            if arr[l] == arr[r]: 
                arr[r].next = None 
                break 
            arr[r].next = arr[l]
            r -= 1 
        
        arr[r].next = None 
        
        