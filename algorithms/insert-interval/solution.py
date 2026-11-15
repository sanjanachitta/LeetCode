class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result =[]

        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0]>newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
        result.append(newInterval)
        return result
        