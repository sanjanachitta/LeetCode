class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dict ={}
        for i in candyType:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        
        tar = len(candyType) // 2

        if tar <= len(dict):
           return tar
        else:
           return len(dict)