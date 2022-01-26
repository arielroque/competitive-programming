# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        faster = head
        slow = head
        
        
        while (n > 0):
            faster = faster.next
            n -= 1
        
        
        if(faster is None):
            head = head.next
        
        else:
            while(faster is not None and faster.next is not None):
                faster = faster.next
                slow = slow.next
            
            slow.next = slow.next.next
        
        return head
            
                
            
        