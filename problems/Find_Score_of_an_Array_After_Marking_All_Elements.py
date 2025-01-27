class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ord = list(range(n))

        ord.sort(key=lambda x: (nums[x]))
        print(ord)
        m = [False] * n
        score = 0

        for x in ord:
            if not m[x]:
                score += nums[x]
                m[x] = True
                if x > 0: m[x - 1] = True
                if x + 1 < n: m[x + 1] = True
        return score

x = Solution()

print(x.findScore(nums = [2,3,5,1,3,2]))