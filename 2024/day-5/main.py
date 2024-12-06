def task1(xy_dict, lists):
    sum = 0
    for list in lists:
        checked_numbers = []
        for index, number in enumerate(list):
            if number in xy_dict:
                # If there is a Y that is in front of X in the protocol
                if set(xy_dict[number]).intersection(set(checked_numbers)):
                    break
            if index == len(list)-1:
                middle = (len(list)+1) /2
                sum += list[int(middle)-1]
            checked_numbers.append(number)
    return sum

def read_lines():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Split the content into X|Y pairs and number lines
    xy_data = []
    number_lines = []
    for line in lines:
        line = line.strip()
        if '|' in line:
            xy_data.append(line)
        elif ',' in line:
            number_lines.append(line)

    # Process the X|Y pairs
    xy_dict = {}
    for pair in xy_data:
        x, y = map(int, pair.split('|'))
        if x not in xy_dict:
            xy_dict[x] = []
        xy_dict[x].append(y)

    number_arrays = [list(map(int, line.split(','))) for line in number_lines]
    return xy_dict, number_arrays

def needs_repair(xy_dict ,list):
    checked_numbers = []
    for number in list:
        if number in xy_dict:
            if set(xy_dict[number]).intersection(set(checked_numbers)):
                return True
        checked_numbers.append(number)
    return False

def find_before_index(checked_numbers, y_vals):
    for y in y_vals:
        for index, number in enumerate(checked_numbers):
            if y == number:
                return index
    return -1


def reparation(xy_dict, list):
    checked_numbers = []
    for number in list:
        if number in xy_dict:
            if set(xy_dict[number]).intersection(set(checked_numbers)):
                before_index = find_before_index(checked_numbers, xy_dict)
                list.remove(number)
                list.insert(before_index, number)
                return list
        checked_numbers.append(number)
    return list


def task2(xy_dict, lists):
    sum = 0

    for list in lists:
        repaired_list = list
        repaired = False

        while needs_repair(xy_dict, list):
            repaired = True
            repaired_list = reparation(xy_dict, repaired_list)

        if repaired:
            middle = (len(list)+1) /2
            sum += list[int(middle)-1]

    return sum



if __name__ == '__main__':
    (xy_dict, lists) = read_lines()

    print(f"Task 1: {task1(xy_dict, lists)}")
    print(f"Task 2: {task2(xy_dict, lists)}")