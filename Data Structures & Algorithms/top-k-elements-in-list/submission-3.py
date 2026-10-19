class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        count = sorted(count,key=lambda x : count[x], reverse=True)
        ans = []
        for i in range(k):
            ans.append(count[i])
        return ans