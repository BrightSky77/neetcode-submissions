class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        n = len(intervals)
        for i in range(1,n):
            s,e = intervals[i]
            prev_s,prev_e = output[-1]

            if s > prev_e:
                output.append([s,e])
            elif s <= prev_e:
                if e >=prev_e:
                    output[-1][1] = e
        return output
        