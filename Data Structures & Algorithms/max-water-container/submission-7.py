class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = float("-inf")
        while l<r:
            area = (min(heights[l],heights[r]) * (r-l))
            max_area = max(area,max_area)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return max_area

                


        
        
        
        
        
        #brute force
        # max_area = float("-inf")
        # length_heigths = len(heights)
        # for i in range(length_heights):
        #     for j in range(i+1,length_heights)
        #         area = (j-i) * min(heights[i],heights[j])
        #         max_area = max(area, max_area)
        # return max_area
            