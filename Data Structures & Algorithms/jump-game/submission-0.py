class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                if j <= i + nums[i]:
                    if dp[j] == True:
                        dp[i] = True
        return dp[0]