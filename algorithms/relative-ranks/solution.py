from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur=0
        maxi=0
        n = len(s)
        q = deque()
        for i in range(n):
            if s[i] not in q:
                q.append(s[i])
                cur= len(q)
                
            else:
                while s[i] in q:
                    q.popleft()
                q.append(s[i])
                cur = len(q)
            maxi = max(maxi,cur)
        return maxi
                

