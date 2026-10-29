class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sub_list = []
        def dfs(sub_list,depth):
            if depth == n:
                res.append(sub_list.copy())
                return
            
            sub_list.append(nums[depth])
            
            dfs(sub_list,depth+1)
            sub_list.pop()
            dfs(sub_list,depth+1)
        
        dfs(sub_list,0)
        return res

    
        