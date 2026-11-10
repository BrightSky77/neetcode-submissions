class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        def expand(l,r):
            nonlocal cnt
            while 0<=l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1

        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return cnt

        