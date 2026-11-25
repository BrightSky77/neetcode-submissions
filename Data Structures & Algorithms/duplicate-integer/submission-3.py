class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = Counter(nums)
        for value in num_dict.values():
            if value > 1:
                return True
        return False
        