class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict ={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        length =0
        odd = False
        for i in dict:
            if dict[i]%2==0:
                length+=dict[i]
            else :
                length+=dict[i]-1
                odd=True
        if odd:
            length+=1
        return length
