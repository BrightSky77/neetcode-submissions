class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for s,e in intervals[1:]:
            last_val = output[-1][1]

            if s > last_val:
                output.append([s,e])
            elif s <= last_val and e >= last_val:
                output[-1][1] = e
        return output
        