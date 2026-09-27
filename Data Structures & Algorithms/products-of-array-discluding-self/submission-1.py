class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        pref = [0 for _ in range(n)] 
        suff = [0 for _ in range(n)]

        pref[0] = suff[n-1] = 1
        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

       

