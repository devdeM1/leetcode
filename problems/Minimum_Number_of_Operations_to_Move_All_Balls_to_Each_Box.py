class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        distance_list =[0] * len(boxes)

        for i in range(len(boxes)):
            if boxes[i] != '0':
                for j in range(len(boxes)):
                    if i != j:
                        distance_list[j] += abs(i - j)
        return distance_list



x = Solution()

print(x.minOperations(boxes = "001011"))