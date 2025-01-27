class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        while i < k:
            gifts[gifts.index(max(gifts))] = int(gifts[gifts.index(max(gifts))] ** 0.5)
            i += 1
        return sum(gifts)

x = Solution()

print(x.pickGifts([75,28,65], k = 3))