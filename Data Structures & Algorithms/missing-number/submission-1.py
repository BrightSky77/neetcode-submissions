class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        nums_set = set(nums)
        for i in range(max_num+1):
            if i not in nums_set:
                return i