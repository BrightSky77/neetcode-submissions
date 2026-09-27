class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1,len(prices)):
            sliced_price = prices[l:r+1]
            min_price = min(sliced_price[:-1])
            if sliced_price[-1] <= min_price:
                l = r
                continue
            diff = sliced_price[-1] - sliced_price[0]
            res = max(res, diff)
        return res

        l,r = 0,1
        maxPrice = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxPrice = max(diff, maxPrice)

            else:
                l = r
            r += 1
        return maxPrice
        
