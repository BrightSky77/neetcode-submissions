class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        for mask in range(1<<n):
            sub_list = []
            for i in range(n):
                if mask & (1<<i):
                    sub_list.append(nums[i])
            res.append(sub_list)
        return res
                
        