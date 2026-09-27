class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key_value = {}
        for num in nums:
            if num not in key_value:
                key_value[num] = 1
            else:
                key_value[num] += 1
        
        for k,v in key_value.items():
            if v >= 2:
                return True
        
        return False

        