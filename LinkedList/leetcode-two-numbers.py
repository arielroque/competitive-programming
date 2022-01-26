# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        arr1 = []
        arr2 = []
        
        while(l1 != None):
            arr1.append(str(l1.val))
            l1 = l1.next
            
        while(l2 != None):
            arr2.append(str(l2.val))
            l2 = l2.next
        
        arr1.reverse()
        arr2.reverse()
        
        v1 = int("".join(arr1))
        v2 = int("".join(arr2))
        
        s = list(str(v1+v2))
        s.reverse()
        
        head = ListNode(0)
        result = head
        
        for i in s:
            head.next = ListNode(i)
            head = head.next
        
        result = result.next
                 
        return result 
                 