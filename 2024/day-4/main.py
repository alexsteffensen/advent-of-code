import re
import numpy as np

def task1(lines):
    sum = 0
    # horizontal
    sum += get_xmases(lines)

    # vertically
    columns_as_strings = [''.join(line[i] for line in lines) for i in range(len(lines[0]))]
    sum += get_xmases(columns_as_strings)

    #diagonally
    sum += get_diagonal_xmases(np.array([list(subarray) for subarray in lines]))
    return sum

def get_xmases(lines):
    sum = 0
    for line in lines:
        sum += len([match.group(1) for match in re.finditer(r"(?=(XMAS|SAMX))", line)])
    return sum

def get_diagonal_xmases(lines):
    return get_xmases(calc_diagonal(lines)) + get_xmases(calc_diagonal(lines[:, ::-1]))
    
def calc_diagonal(lines):
    array = []
    for index in range(len(lines)+ len(lines[0])-1):
        k_val = index - len(lines) +1
        diag = np.diag(lines, k = k_val)
        array.append("".join([str(char) for char in diag]))
    return array

def task2(lines):
    return num_cross_xmas([list(subarray) for subarray in lines])

def num_cross_xmas(lines):
    sum = 0
    for i in range(len(lines)-2):
        for j in range(len(lines[i])-2):

            mas_check = lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S"
            sam_check = lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M"
            if mas_check or sam_check:
                s_and_m = lines[i][j+2] == "M"  and lines[i+2][j] == "S"
                m_and_s = lines[i][j+2] == "S"  and lines[i+2][j] == "M"
                if s_and_m or m_and_s:
                    sum += 1
    return sum

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

        print(f"Task 1: {task1(lines)}")
        print(f"Task 2: {task2(lines)}")

    