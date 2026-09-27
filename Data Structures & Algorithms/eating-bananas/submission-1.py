class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = r 
        while l <= r:
            mid = (l+r)//2
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile/mid)
            if cnt > h:
                l = mid + 1
            elif cnt <= h:
                r = mid - 1
                ans = mid

        return ans
