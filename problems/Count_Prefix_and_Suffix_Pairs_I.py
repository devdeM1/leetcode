class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i != j and words[j].startswith(words[i]):
                    if i != j and words[j].endswith(words[i]):
                        ans += 1
        return ans



x = Solution()

print(x.countPrefixSuffixPairs(words = ["bb","bb"]))