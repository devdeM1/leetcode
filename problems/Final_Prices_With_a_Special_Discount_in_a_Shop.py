class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(prices) - 1:
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
            i += 1
        return prices




x = Solution()

print(x.finalPrices([8,7,4,2,8,1,7,7,10,1]))