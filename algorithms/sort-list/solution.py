# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        N=0
        while cur:
            N+=1
            cur =cur.next
        cur=head
        if N == 1:
           return None
        for i in range(N//2-1):
            cur=cur.next
        cur.next=cur.next.next
        return head

