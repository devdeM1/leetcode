from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """


        req = Counter()
        for word in words2:
            cur = Counter(word)
            for ch in cur:
                req[ch] = max(req[ch], cur[ch])

x = Solution()

print(x.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
["lo","eo"]))