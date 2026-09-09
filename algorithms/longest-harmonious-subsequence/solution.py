class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict ={}
        min =0
        maxi=0
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for key in dict:
            if key+1 in dict:
                min=dict[key]+dict[key+1]
                maxi = max(maxi,min)
        return maxi

