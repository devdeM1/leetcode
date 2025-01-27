class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_right = 0
        sum_left = 0
        for i in range(len(nums)):
            sum_right += nums[i]

        i = 0
        total_valid = 0
        while i < len(nums) - 1:
            sum_left += nums[i]
            sum_right -= nums[i]
            if sum_left >= sum_right:
                total_valid += 1
            i += 1
        return total_valid

x = Solution()

print(x.waysToSplitArray(nums = [10,4,-8,7]))