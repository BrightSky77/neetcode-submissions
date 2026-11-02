class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = [False] * n
        # dp[-1] = True
        # for i in range(n-2,-1,-1):
        #     for j in range(n-1,i,-1):
        #         if j <= i + nums[i]:
        #             if dp[j] == True:
        #                 dp[i] = True
        # return dp[0]

        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False