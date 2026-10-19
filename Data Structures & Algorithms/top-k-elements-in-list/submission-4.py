class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        ans = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key,value in count.items():
            freq[value].append(key)
        
        for idx in range(len(freq)-1,-1,-1):
            for num in freq[idx]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        