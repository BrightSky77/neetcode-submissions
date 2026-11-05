class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        cur = []
        def dfs(i,total,cur):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target or i > n-1:
                return
            num = nums[i]
            total += num
            cur.append(num)
            dfs(i,total,cur)

            total -= num
            cur.pop()
            dfs(i+1,total,cur)
        dfs(0,0,cur)
        return res
        


        


        