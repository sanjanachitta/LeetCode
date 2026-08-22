# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        dummy=ListNode(0)
        cur = head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        arr.sort()
        cur=dummy
        for i in range(len(arr)):
            cur.next=ListNode(arr[i])
            cur=cur.next
        return dummy.next
