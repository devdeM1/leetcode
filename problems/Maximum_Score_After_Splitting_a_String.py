class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        for i in range(len(s) - 1):
            score = 0
            substirng_left = s[0:i+1]
            substirng_right = s[i+1:len(s)]
            score = substirng_left.count('0') + substirng_right.count('1')
            if score > max_score: max_score = score
        return max_score

x = Solution()

print(x.maxScore(s = "00"))