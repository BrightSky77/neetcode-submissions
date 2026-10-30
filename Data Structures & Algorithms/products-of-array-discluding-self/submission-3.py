class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        prefix[0] = 1
        suffix = [0] * (n + 1)
        suffix[n] = 1
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n,0,-1):
            suffix[i-1] = suffix[i] * nums[i-1]

        output = []
        for i in range(n):
            output.append(prefix[i]*suffix[i+1])
        return output