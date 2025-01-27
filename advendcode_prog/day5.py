def get_data():
    with open("d5.txt") as f:
        return f.read()

def part1():
    sum = 0
    rules, updates = get_data().split('\n\n')
    rules_list = []
    for rule in rules.split():
        before, after = rule.split('|')
        rules_list.append((int(before), int(after)))

    updates_list = []
    for update_raw in updates.split('\n'):
        inner_list = []
        for digit in update_raw.split(','):
           inner_list.append(digit)
        updates_list.append(inner_list)


    for update in updates_list:
        does_correct_rule = True
        for i in range(len(update)):
            for j in range(1, len(update) - i):
                if (int(update[j+i]),int(update[i])) in rules_list:
                    does_correct_rule = False
        if does_correct_rule: sum += int(update[(int(len(update)/2))])
    return sum

def part2():
    sum = 0
    rules, updates = get_data().split('\n\n')
    rules_list = []
    for rule in rules.split():
        before, after = rule.split('|')
        rules_list.append((int(before), int(after)))


    updates_list = []
    for update_raw in updates.split('\n'):
        inner_list = []
        for digit in update_raw.split(','):
            inner_list.append(digit)
        updates_list.append(inner_list)

    non_correct_updates_list = []
    for update in updates_list:
        does_correct_rule = True
        for i in range(len(update)):
            for j in range(1, len(update) - i):
                if (int(update[j+i]),int(update[i])) in rules_list:
                    does_correct_rule = False
        if not does_correct_rule: non_correct_updates_list.append(update)
    for update in non_correct_updates_list:
        i = 0
        while i < len(update):
            j = 1
            while j < len(update) - i:
                if (int(update[j + i]), int(update[i])) in rules_list:
                    update[i], update[j + i] =  update[j + i], update[i]
                    j = 0
                j += 1
            i += 1
        sum += int(update[(int(len(update)/2))])
    return sum
def main():
    # print(part1())
    print(part2())

if __name__ == "__main__":
    main()