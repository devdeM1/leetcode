from itertools import product

def get_data():
    with open("d4.txt") as f:
        return f.read().splitlines()

def get_data_for_dig():
    with open("d4_dig.txt") as f:
        return f.read().splitlines()

def count_xmas(str):
    sum = 0
    sum += str.count('XMAS')
    sum += str.count('SAMX')
    return sum

def create_inv_file():
    for line in get_data():
        with open('d4_dig.txt', 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(line+ '\n'+content)

def count_dig_xmas(total_lines, n, a):
    sum = 0
    diagonals_l = ['' for i in range(total_lines + n - 1)]
    for i in range(-(total_lines - 1), n):
        for j in range(total_lines):
            row, col = j, i + j
            if 0 <= row < len(a) and 0 <= col < len(a[0]):
                diagonals_l[i + len(a) - 1] += (a[row][col])
    for dig in diagonals_l:
        sum += count_xmas(dig)
    return sum

def part1():
    create_inv_file()

    columns_list = []
    mark_created_list = False
    sum = 0
    total_lines = 0

    for line in get_data():
        total_lines += 1
        sum += count_xmas(line)
        if not mark_created_list:
            mark_created_list = True
            for i in range(len(line)):
                columns_list.append('')
        for i in range(len(line)):
            columns_list[i] += line[i]
    for item in columns_list:
        sum += count_xmas(item)

    all_data = get_data()
    sum += count_dig_xmas(total_lines = total_lines, n = len(line), a = all_data)

    data_with_swaped_lines = get_data_for_dig()
    sum += count_dig_xmas(total_lines = total_lines, n = len(line), a=data_with_swaped_lines)

    return sum

def main():
    print(part1())


if __name__ == "__main__":
    main()