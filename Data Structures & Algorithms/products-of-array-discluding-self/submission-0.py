class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        result = []
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i]:
                total_product *=nums[i]
            else:
                zero_cnt += 1

        if zero_cnt >= 2:
            result = [0 for _ in range(len(nums))]
            return result
        
        for i in range(len(nums)):
            if zero_cnt == 0:
                result.append((total_product//nums[i]))
            else:
                if nums[i] == 0:
                    result.append(total_product)
                else:
                    result.append(0)
        return result

