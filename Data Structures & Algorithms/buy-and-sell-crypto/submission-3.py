class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxi = 0

        while l < len(prices) - 1:
            if prices[r] > prices[l]:
                diff = prices[r] - prices[l]
                maxi = max(diff, maxi)

            r = r + 1

            if r == len(prices):
                l += 1
                r = l + 1

        return maxi