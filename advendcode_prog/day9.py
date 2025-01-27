def get_data():
    with open("d9.txt") as f:
        return f.read().splitlines()

def merging_empty_blocks(map):
    i = 0
    while i <= len(map) - 2:
        try:
            map[i][0] == map[i + 1][0]
        except IndexError:
            pass
        if map[i][0] == map[i+1][0] == '.':
            map[i] += map[i + 1]
            map.pop(i + 1)
            i -= 1
        i += 1
    return map

def part1():
    full_list_disk_map = ''
    new_map = []
    sum = 0
    for line in get_data():
        full_list_disk_map+=(line)
    for i in range(int(len(full_list_disk_map) / 2) + 1):
        i *= 2
        j = i + 1
        for l in range(1, int(full_list_disk_map[i]) + 1):
            new_map.append(int(i/2))
        if j != len(full_list_disk_map):
            for q in range(1, int(full_list_disk_map[j]) + 1):
                new_map.append('.')
    while '.' in new_map:
        mark_find = False
        i = len(new_map) - 1
        while not mark_find and i >= 0:
            if new_map[i] != '.':
                mark_find = True
                break
            i -= 1
        new_map[new_map.index('.')] = new_map[i]
        new_map.pop(i)
    for i in range(len(new_map)):
        sum += i * new_map[i]
    return sum

def part2():
    full_list_disk_map = ''
    new_map = []
    sum = 0
    for line in get_data():
        full_list_disk_map += (line)
    for i in range(int(len(full_list_disk_map) / 2) + 1):
        i *= 2
        j = i + 1
        inner_list = []
        for l in range(1, int(full_list_disk_map[i]) + 1):
            inner_list.append(int(i / 2))
        new_map.append(inner_list)
        inner_list = []
        if j != len(full_list_disk_map):
            for q in range(1, int(full_list_disk_map[j]) + 1):
                inner_list.append('.')
        new_map.append(inner_list)
    i = 0
    while i < len(new_map):
        if len(new_map[i]) == 0:
            new_map.pop(i)
            i -= 2
        i += 1
    i = len(new_map) - 1
    while i >= 0:
        if len(new_map[i]) != 0 and new_map[i][0] != '.':
            for j in range(i):
                if len(new_map[j]) >= len(new_map[i]) and new_map[j][0] == '.':
                    distance = len(new_map[j]) - len(new_map[i])
                    new_map.insert(j, new_map[i])
                    new_map.pop(j + 1)
                    inner_list = []
                    for q in range(len(new_map[i])):
                        inner_list.append('.')
                    new_map.insert(i, inner_list)
                    new_map.pop(i + 1)
                    if distance != 0:
                        inner_list = []
                        for r in range(distance):
                            inner_list.append('.')
                        new_map.insert(j+1, inner_list)
                        i += 1
                    merging_empty_blocks(new_map)
                    break
        i -= 1
    my_index = 0
    for block in new_map:
        if block[0] != '.':
            for item in block:
                sum += my_index * item
                my_index += 1
        else:
            my_index += len(block)


    return sum

def main():
    # print(part1())

    print(part2())

if __name__ == "__main__":
    main()