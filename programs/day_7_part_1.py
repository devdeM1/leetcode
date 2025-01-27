from itertools import product

def get_data():
    with open("d7.txt") as f:
        return f.read().splitlines()

def take_result_with_current_operators(operators, digits):
    result = int(digits[0])
    for i in range(len(operators)):
        a = int(digits[i+1])
        result_str = 'result {} a'.format(operators[i])
        result = eval(result_str)
    return result

def part1():
    sum = 0
    for line in get_data():
        need_result, digits = int(line.split(': ')[0]), line.split(': ')[1].split(' ')
        list_operators = list(product('+*', repeat=len(digits)-1))
        for operators in list_operators:
            if need_result == take_result_with_current_operators(operators, digits):
                sum += need_result
                break
    return sum

def main():
    print(part1())


if __name__ == "__main__":
    main()