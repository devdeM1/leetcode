class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[j].find(words[i]) >= 0:
                    ans.add(words[i])
        return list(ans)


x = Solution()

print(x.stringMatching(words = ["mass","as","hero","superhero"]))