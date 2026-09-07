class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                continue
            else:
                res = max(res, prices[right] - prices[left])
                right += 1
        
        return res