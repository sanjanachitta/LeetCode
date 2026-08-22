# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        L = 0

        # Find length
        while cur:
            L += 1
            cur = cur.next

        # If deleting the first node
        if L == n:
            return head.next

        # Go to node BEFORE the node to delete
        cur = head
        for i in range(L - n - 1):
            cur = cur.next

        # Skip the nth node from the end
        cur.next = cur.next.next

        return head