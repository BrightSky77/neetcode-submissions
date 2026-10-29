class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            num_binary_cnt = 0
            while num:
                num &= num - 1
                num_binary_cnt += 1
            ans.append(num_binary_cnt)
        return ans
        