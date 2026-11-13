class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n= len(g)
        m = len(s)
        i=0
        j=0
        count =0
        while i<n and j<m:
            if s[j]>=g[i]:
               count+=1
               i+=1
               j+=1
            else:
              j+=1
        return count