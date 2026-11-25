class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for idx, num in enumerate(nums):
            indices[num] = idx


        for i in range(len(nums)):
            sub_target = target - nums[i]
            if sub_target in indices and indices[sub_target] != i:
                # sort_ans = sorted([i,indices[sub_target]])
                # return sort_ans
                return [i,indices[sub_target]]
