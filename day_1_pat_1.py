class Solution(object):
    def total_distance(self):
        total_distance = 0
        first_list = []
        second_list = []
        f = open('d1.txt', 'r')
        str =  f.read()
        str = str.split('\n')
        for line in str:
            two_digits = line.split(('   '))
            first_list.append(int(two_digits[0]))
            second_list.append(int(two_digits[1]))
        while len(first_list) > 1:
            total_distance += abs(min(first_list) - min(second_list))
            first_list.remove(min(first_list))
            second_list.remove(min(second_list))

        return total_distance

x = Solution()
print(x.total_distance())

