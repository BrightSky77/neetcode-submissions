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
        end_time_heap = [intervals[0].end]

        n = len(intervals)
        ans = 1
        for i in range(1,n):
            if end_time_heap[0] > intervals[i].start:
                ans += 1
            else:
                heapq.heappop(end_time_heap)
            heapq.heappush(end_time_heap,intervals[i].end)
        return ans
                



        





            
        