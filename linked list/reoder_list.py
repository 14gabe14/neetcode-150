# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        stack = []

        while slow != None:
            stack.append(slow)
            slow = slow.next
            stack[-1].next = None

        current = head

        while current and current.next and stack:
            nextNode = current.next
            current.next = stack.pop()
            current.next.next = nextNode
            current = nextNode

        current.next = None
        
        return head