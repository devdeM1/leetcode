from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = list(Counter(nums))
        return cnt[0]

x = Solution()

print(x.majorityElement(nums = [2,2,1,1,1,2,2]))