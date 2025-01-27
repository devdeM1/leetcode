def get_data():
    with open("d8.txt") as f:
        return f.read().splitlines()

def part1():
    full_list_antenn = []
    set_with_antinodes  = set()
    for line in get_data():
        full_list_antenn.append(list(line))
    for i in range(len(full_list_antenn)):
        for j in range(len(full_list_antenn[i])):
            if full_list_antenn[i][j] != '.':
                for l in range(i + 1, len(full_list_antenn)):
                    if full_list_antenn[i][j] in full_list_antenn[l]:
                        q = full_list_antenn[l].index(full_list_antenn[i][j])
                        distance_vertical = l - i
                        distance_horizontal = abs(j - q)
                        # When the second antenna is to the left of the first
                        if j > q:
                            # Before first antenna
                            if ((0 <= i - distance_vertical and i - distance_vertical < len(full_list_antenn))
                                    and (0 <= j + distance_horizontal and j + distance_horizontal < len(
                                        full_list_antenn[i]))):
                                set_with_antinodes.add((i - distance_vertical, j + distance_horizontal))
                            # Under second antenna
                            if ((0 <= l + distance_vertical and l + distance_vertical < len(full_list_antenn))
                                    and (0 <= q - distance_horizontal and q - distance_horizontal < len(
                                        full_list_antenn[i]))):
                                set_with_antinodes.add((l + distance_vertical, q - distance_horizontal))
                        # When the second antenna is to the right of the first
                        else:
                            # Before first antenna
                            if ((0 <= i - distance_vertical and i - distance_vertical < len(full_list_antenn))
                                    and (0 <= j - distance_horizontal and j - distance_horizontal < len(
                                        full_list_antenn[i]))):
                                set_with_antinodes.add((i - distance_vertical, j - distance_horizontal))
                            # Under second antenna
                            if ((0 <= l + distance_vertical and l + distance_vertical < len(full_list_antenn))
                                    and (0 <= q + distance_horizontal and q + distance_horizontal < len(
                                        full_list_antenn[i]))):
                                set_with_antinodes.add((l + distance_vertical, q + distance_horizontal))
    return len(set_with_antinodes)

def part2():
    full_list_antenn = []
    set_with_antinodes  = set()
    for line in get_data():
        full_list_antenn.append(list(line))
    for i in range(len(full_list_antenn)):
        for j in range(len(full_list_antenn[i])):
            if full_list_antenn[i][j] != '.':
                for l in range(i + 1, len(full_list_antenn)):
                    if full_list_antenn[i][j] in full_list_antenn[l]:
                        q = full_list_antenn[l].index(full_list_antenn[i][j])
                        distance_vertical = l - i
                        distance_horizontal = abs(j - q)

                        i1 = i
                        j1 = j
                        l1 = l
                        q1 = q
                        # When the second antenna is to the left of the first
                        if j > q:
                            # Before first antenna
                            while ((0 <= i1 and i1 < len(full_list_antenn))
                                    and (0 <= j1 and j1 < len(full_list_antenn[0]))):
                                set_with_antinodes.add((i1, j1))
                                i1 -= distance_vertical
                                j1 += distance_horizontal
                            # Under second antenna
                            while ((0 <= l1 and l1 < len(full_list_antenn))
                                    and (0 <= q1 and q1 < len(full_list_antenn[i]))):
                                set_with_antinodes.add((l1, q1))
                                l1 += distance_vertical
                                q1 -= distance_horizontal
                        # When the second antenna is to the right of the first
                        else:
                            # Before first antenna
                            while ((0 <= i1 and i1 < len(full_list_antenn))
                                    and (0 <= j1 and j1 < len(full_list_antenn[i]))):
                                set_with_antinodes.add((i1, j1))
                                i1 -= distance_vertical
                                j1 -= distance_horizontal
                            # Under second antenna
                            while 0 <= l1 and l1 < len(full_list_antenn) and 0 <= q1 and q1 < len(full_list_antenn[i]):
                                set_with_antinodes.add((l1, q1))
                                l1 += distance_vertical
                                q1 += distance_horizontal
    return len(set_with_antinodes)

def main():
    # print(part1())
    print(part2())



if __name__ == "__main__":
    main()