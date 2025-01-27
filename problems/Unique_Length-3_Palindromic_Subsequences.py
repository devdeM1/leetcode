class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_symbol = set()
        sum = 0
        for i in range(len(s)):
            if s[i] not in set_symbol and s.count(s[i]) >= 2:
                set_symbol.add(s[i])
                s2 = s[::-1]
                index_symbol_second = len(s) - 1 - s2.index(s[i])
                set_polind = set()
                for j in range(i + 1 , index_symbol_second):
                    set_polind.add(s[j])
                sum += len(set_polind)
        return sum
#

x = Solution()

print(x.countPalindromicSubsequence(s = "bbcbaba"))