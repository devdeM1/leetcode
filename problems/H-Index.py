class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_citations = sorted(citations,reverse=True)
        h = 0
        for i in range(0,len(citations)):
            if sorted_citations[i]>=i+1:
                h+=1
        return h


x = Solution()

print(x.hIndex(citations = [1,3,1]))