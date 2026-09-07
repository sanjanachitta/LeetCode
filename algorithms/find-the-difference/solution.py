class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # dict = {}
        # for char in s:
        #     if char in dict:
        #         dict[char]+=1
        #     else:
        #         dict[char]=1
        # for i in t:
        #    dict[i] = dict.get(i, 0) - 1

        #    if dict[i] == -1:
        #      return i
        # for char in t:
        #    if t.count(char) > s.count(char):
        #       return char
        for char in s:
            t = t.replace(char, '', 1)
        return t