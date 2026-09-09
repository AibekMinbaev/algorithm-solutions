# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] 

        for idx, node in enumerate(lists): 
            if not node: 
                continue 
                
            heapq.heappush(heap, (node.val, idx, node)) 
        
        dummy = ListNode() 
        curr = dummy 
        while heap: 
            val, idx, node = heapq.heappop(heap) 

            if node.next: 
                heapq.heappush(heap, (node.next.val, idx, node.next))

            node.next = None 
            curr.next = node 
            curr = curr.next  

        return dummy.next 


