"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)
        end_list = [intervals[0].end]
        for interval in intervals[1:]:
            s = interval.start
            e = interval.end
            if end_list[0] <= s:
                heapq.heappop(end_list)
            heapq.heappush(end_list,e)
        return len(end_list)

        #Time Complexity(O(NlogN + NLogN + NlogN) = O(NlogN))
        #Space Complexity = O(N)




            
        