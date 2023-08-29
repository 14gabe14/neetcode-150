# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        residue = (l1.val + l2.val) // 10
        
        current_sum = head
        current_n1 = l1.next
        current_n2 = l2.next
        
        while current_n1 or current_n2:
            val = residue
            
            if current_n1:
                val += current_n1.val
                current_n1 = current_n1.next
                
            if current_n2:
                val += current_n2.val
                current_n2 = current_n2.next
            
            current_sum.next = ListNode(val % 10)
            current_sum = current_sum.next
            residue = val // 10
            
        if residue > 0:
            current_sum.next = ListNode(residue)
        
        return head
            