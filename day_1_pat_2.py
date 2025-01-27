class Solution(object):
    def total_similarity_score(self):
        total_similarity_score = 0
        first_list = []
        second_list = []
        f = open('adventofcode.txt', 'r')
        str =  f.read()
        str = str.split('\n')
        for line in str:
            two_digits = line.split(('   '))
            first_list.append(int(two_digits[0]))
            second_list.append(int(two_digits[1]))
        for i in range(len(first_list)):
            total_similarity_score += first_list[i] * second_list.count(first_list[i])
        return total_similarity_score

x = Solution()
print(x.total_similarity_score())

