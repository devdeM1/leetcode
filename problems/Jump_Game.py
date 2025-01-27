

def canssss(start, nums):
    if nums[0] == int(len(nums) - 1):
        return True
    else:
        for i in range(1, nums[start]):
            canssss(i, nums[i:])


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return canssss(0, nums)

x = Solution()

print(x.canJump(nums = [2,3,1,1,4]))