class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        top_k_list = sorted(nums_dict.items(), key=lambda x : x[1],reverse=True)[:k]
        result = []
        for top_key in top_k_list:
            result.append(top_key[0])
        
        return result