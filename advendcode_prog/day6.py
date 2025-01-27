def get_data():
    with open("d6.txt") as f:
        return f.read().splitlines()

def part1():
    full_map = []
    set_x_coordinates = set()
    direction_of_movement = ''
    can_move = True

    for line in get_data():
        full_map.append(list(line))

    current_second_index = 0
    current_first_index = 0
    for i in range(len(full_map) - 1):
        if '^' in full_map[i]:
            current_second_index = full_map[i].index('^')
            current_first_index = i
            direction_of_movement = 'up'
            full_map[i][current_second_index] = '.'
            break

    while can_move:
        if direction_of_movement == 'up':
            if current_first_index == 0:
                can_move = False
                break
            else:
                if full_map[current_first_index - 1][current_second_index] == '.':
                    set_x_coordinates.add((current_first_index, current_second_index))
                    current_first_index -= 1
                elif full_map[current_first_index - 1][current_second_index] == '#':
                    direction_of_movement = 'right'
        elif direction_of_movement == 'down':
            if current_first_index == len(full_map) - 1:
                can_move = False
                break
            else:
                if full_map[current_first_index + 1][current_second_index] == '.':
                    set_x_coordinates.add((current_first_index, current_second_index))
                    current_first_index += 1
                elif full_map[current_first_index + 1][current_second_index] == '#':
                    direction_of_movement = 'left'
        elif direction_of_movement == 'right':
            if current_second_index == len(full_map[0]) - 1:
                can_move = False
                break
            else:
                if full_map[current_first_index][current_second_index + 1] == '.':
                    set_x_coordinates.add((current_first_index, current_second_index))
                    current_second_index += 1
                elif full_map[current_first_index][current_second_index + 1] == '#':
                    direction_of_movement = 'down'
        elif direction_of_movement == 'left':
            if current_second_index == 0:
                can_move = False
                break
            else:
                if full_map[current_first_index][current_second_index - 1] == '.':
                    set_x_coordinates.add((current_first_index, current_second_index))
                    current_second_index -= 1
                elif full_map[current_first_index][current_second_index - 1] == '#':
                    direction_of_movement = 'up'
    set_x_coordinates.add((current_first_index, current_second_index))
    return len(set_x_coordinates)

def main():
    print(part1())

if __name__ == "__main__":
    main()