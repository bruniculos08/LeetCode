# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        aux = result
        while(aux != None and (l1 != None or l2 != None)):
            if(l1 != None):
                aux.val += l1.val
            if(l2 != None):
                aux.val += l2.val
            if aux.val >= 10:
                aux.next = ListNode()
                aux.next.val += 1
                aux.val = aux.val-10
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next
            if aux.next == None and (l1 != None or l2 != None):
                aux.next = ListNode()
            aux = aux.next
        return result