class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x,y):
            distance = abs(x)**2+abs(y)**2
            return distance
        
        dist_list = []
        
        for i in range(len(points)):
            x,y = points[i]
            dist = euclidean_distance(x,y)
            dist_list.append([dist,x,y])

        heapq.heapify(dist_list)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(dist_list)
            res.append([x,y])
            k -= 1
        return res 
        
