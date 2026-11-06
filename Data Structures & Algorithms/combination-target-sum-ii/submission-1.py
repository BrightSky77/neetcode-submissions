class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        cur = []
        n = len(candidates)
        def dfs(idx,total):
            if total == 0:
                output.append(cur.copy())
                return
            for i in range(idx,n):
                num = candidates[i]
                if i > idx and num == candidates[i-1]:
                    continue
                if num > total:
                    break
                cur.append(num)
                dfs(i+1,total-num)
                cur.pop()
               
        
        dfs(0,target)
        return output
            






