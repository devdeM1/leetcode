from collections import Counter

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k > len(s):
            return False
        else:
            req = Counter(s)
            count_dooble = 0
            count_alone = 0
            for symbol, count in req.items():
                if count %2 == 0 :
                 count_dooble += count/2
                elif count > 1:
                    count_dooble += int(count / 2)
                    count_alone += 1
                else:
                    count_alone += 1
            if count_alone - 1 < k <= len(s):
                return True
            else:
                return False

x = Solution()

print(x.canConstruct(s = "leetcode", k = 3))