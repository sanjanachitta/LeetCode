# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        if not head or not head.next:
            return head

        # Find length and tail
        n = 1
        cur = head

        while cur.next:
            cur = cur.next
            n += 1

        k = k % n

        if k == 0:
            return head

        # Make circular
        cur.next = head

        # Find new tail
        steps = n - k
        cur = head

        for _ in range(steps - 1):
            cur = cur.next

        # New head
        head = cur.next

        # Break circle
        cur.next = None

        return head
            
