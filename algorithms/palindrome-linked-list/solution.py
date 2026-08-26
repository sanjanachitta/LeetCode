# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow =head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new = slow
        prev = None
        while new:
            pro =new.next
            new.next=prev
            prev=new
            new=pro
        cur1=prev
        cur2=head
        while cur1 and cur2:
            if cur1.val!=cur2.val:
                return False
            cur1=cur1.next
            cur2=cur2.next
        return True
