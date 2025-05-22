class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return maxP


# Test
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
