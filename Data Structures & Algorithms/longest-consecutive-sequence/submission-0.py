class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num -1 not in numSet:
                temp_num = num
                long = 0
                while temp_num in numSet:
                    long += 1
                    temp_num += 1
                longest = max(longest,long)
        return longest
        
