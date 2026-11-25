class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        max_consec = 0
        for num in numSet:
            if num-1 not in numSet:
                temp_num = num
                count = 0
                while temp_num in numSet:
                    temp_num += 1
                    count += 1
                max_consec = max(max_consec,count)
        
        return max_consec

                    
        
