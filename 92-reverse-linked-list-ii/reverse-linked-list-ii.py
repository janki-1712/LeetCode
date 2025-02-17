# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head == None or left ==right:
            return head

        dummy = ListNode(0)
        previous= dummy
        dummy.next = head

        for i in range(left-1):
            previous = previous.next

        current = previous.next

        for i in range(right-left):

            nex = current.next

            current.next = nex.next

            nex.next = previous.next

            previous.next = nex

        return dummy.next