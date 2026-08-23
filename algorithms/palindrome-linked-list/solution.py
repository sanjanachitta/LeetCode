# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st=[]
        N =0
        cur=head
        while cur:
            N+=1
            cur=cur.next
        cur = head
        for i in range(N):
            st.append(cur.val)
            cur=cur.next
        cur = head
        while cur:
            if cur.val ==st[-1]:
                st.pop()
            else:
                return False
            cur = cur.next
        return True

