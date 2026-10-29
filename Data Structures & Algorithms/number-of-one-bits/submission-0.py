class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        binary = []
        while num != 0:
            rem = num % 2
            binary.append(str(rem))
            num = num//2
        binary_num = "".join(reversed(binary))
        ans_cnt = 0
        for num in binary_num:
            if num == "1":
                ans_cnt += 1
        return ans_cnt

            
