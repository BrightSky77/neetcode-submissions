class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        #case1
        #newInterval < intervals

        #case2 
        # newInterval overlaps with intervals
        
        #case3
        # newintervals > intervals
        
        res = []
        for i in range(len(intervals)):
            s,e = intervals[i]
            if newInterval[0] > e:
                res.append(intervals[i])

            elif newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]

            else:
                newInterval[0] = min(newInterval[0],s)
                newInterval[1] = max(newInterval[1],e)
        res.append(newInterval)
        return res
            