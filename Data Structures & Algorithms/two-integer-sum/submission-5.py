class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        nums_with_index = [(num,i) for i,num in enumerate(nums)]
        nums_with_index.sort(key = lambda x: x[0])

        while l < r:
            summation = nums_with_index[l][0] + nums_with_index[r][0]
            if summation < target:
                l += 1
            elif summation > target:
                r -= 1
            else:
                break
        
        ans = [nums_with_index[l][1],nums_with_index[r][1]]
        return sorted(ans)