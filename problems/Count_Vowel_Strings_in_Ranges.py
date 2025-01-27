class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        set_vowels = set('aeiou')
        count_needs_words = 0
        list_pref_count = []
        for i in range(len(words)):
            if words[i][0] in set_vowels and words[i][-1] in set_vowels:
                count_needs_words += 1
            list_pref_count.append(count_needs_words)

        ans = []
        for l,r in queries:
            ans.append(list_pref_count[r] if l == 0 else list_pref_count[r] - list_pref_count[l - 1])
        return ans


cccccccc