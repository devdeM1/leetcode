from collections import Counter


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 1:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return nums



x = Solution()

print(x.removeDuplicates(nums = [1,1,2]))