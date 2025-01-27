class Solution(object):
    def found_not_safe_with_only_one_problem(self):
        total_safe = 0
        file = open("otus.txt", "w")
        f = open('output.txt', 'r')
        str = f.read()
        str = str.split('\n')
        for line in str:
            list_digits = line.split((' '))
            list_with_comparison_signs = []
            for i in range(len(list_digits)-1):
                if abs(int(list_digits[i]) - int(list_digits[i + 1])) > 3:list_with_comparison_signs.append('3')
                elif int(list_digits[i]) < int(list_digits[i + 1]):list_with_comparison_signs.append('<')
                elif int(list_digits[i]) > int(list_digits[i + 1]): list_with_comparison_signs.append('>')
                elif int(list_digits[i]) == int(list_digits[i + 1]): list_with_comparison_signs.append('=')
            if list_with_comparison_signs.count('3') == 1:
                new_list_digits = list_digits.copy()
                del new_list_digits[list_with_comparison_signs.index('3')]
                file.write(' '.join(new_list_digits) + '\n')

                del list_digits[list_with_comparison_signs.index('3') + 1]
                file.write(' '.join(list_digits) + '\n')
            elif list_with_comparison_signs.count('<') == 1:
                new_list_digits = list_digits.copy()
                del new_list_digits[list_with_comparison_signs.index('<')]
                file.write(' '.join(new_list_digits) + '\n')

                del list_digits[list_with_comparison_signs.index('<') + 1]
                file.write(' '.join(list_digits) + '\n')
            elif list_with_comparison_signs.count('>') == 1:
                new_list_digits = list_digits.copy()
                del new_list_digits[list_with_comparison_signs.index('>')]
                file.write(' '.join(new_list_digits) + '\n')

                del list_digits[list_with_comparison_signs.index('>') + 1]
                file.write(' '.join(list_digits) + '\n')
            elif list_with_comparison_signs.count('=') == 1:
                new_list_digits = list_digits.copy()
                del new_list_digits[list_with_comparison_signs.index('=')]
                file.write(' '.join(new_list_digits) + '\n')

                del list_digits[list_with_comparison_signs.index('=') + 1]
                file.write(' '.join(list_digits) + '\n')
        file.close()
        f.close()
        return total_safe

x = Solution()
print(x.found_not_safe_with_only_one_problem())

