class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return nums[len(nums) - k:len(nums)] + nums[0:nums[len(nums) - k - 1]]


x = Solution()

print(x.rotate(nums = [1,2,3,4,5,6,7], k = 10))