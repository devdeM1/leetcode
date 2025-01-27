class Solution(object):
    def found_safe(self):
        total_safe = 0
        f = open('d2.txt', 'r')
        str = f.read()
        str = str.split('\n')

        list_with_true_lines = []
        for line in str:
            decreasing = False
            increasing = False
            i = 1
            list_digits = line.split((' '))
            if abs(int(list_digits[0]) - int(list_digits[1])) <= 3:
                    if int(list_digits[0]) < int(list_digits[1]):increasing = True
                    elif int(list_digits[0]) > int(list_digits[1]): decreasing = True
            while increasing and i < len(list_digits) - 1:
                if int(list_digits[i]) < int(list_digits[i+1]) and int(list_digits[i+1]) - int(list_digits[i]) <= 3:
                    i += 1
                else: increasing = False
            while decreasing and i < len(list_digits) - 1:
                if int(list_digits[i]) > int(list_digits[i+1]) and int(list_digits[i]) - int(list_digits[i+1]) <= 3:
                    i += 1
                else: decreasing = False
            if increasing and decreasing:
                total_safe += 1

        return total_safe

x = Solution()

f1 = open('output.txt', 'r')
str1 = f1.read()
str1 = str1.split('\n')

f2 = open('d2.txt', 'r')
str2 = f2.read()
str2 = str2.split('\n')

file = open("otus.txt", "r")
str3 = file.read()
str3 = str3.split('\n')

print (len(str1), len(str2), len(str3))


