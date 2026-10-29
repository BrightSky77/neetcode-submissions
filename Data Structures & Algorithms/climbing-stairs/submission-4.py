class Solution:
    def climbStairs(self, n: int) -> int:
        stair_length = n
        dp = [0] * (stair_length+1)
        # [0,0,0,0,0]
        dp[1] = 1
        dp[0] = 0
        if stair_length >= 2:
            dp[2] = 2
            #[0,1,2,0,0]
            for i in range(3,stair_length+1):
                # i = 3,4
                # dp[3] = 2+ 1. = 3
                # dp[4] = dp[3] + dp[2] = 3 + 2 = 5
                dp[i] = dp[i-1] + dp[i-2]
        

        
        return dp[stair_length]