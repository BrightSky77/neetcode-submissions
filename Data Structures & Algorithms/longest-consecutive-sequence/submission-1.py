class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 1

        if not nums:
            return 0

        for num in numSet:
            if num -1 not in numSet:
                temp = 0
                while num in numSet:
                    temp += 1
                    num += 1
                longest = max(longest,temp)
        return longest
                    
        
