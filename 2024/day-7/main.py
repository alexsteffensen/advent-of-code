import math
import operator

def task1(tests):
    sum = 0
    for result, values in tests.items():
        calc_sum = calculate(values, 1, result, values[0], operator.add)
        calc_mul = calculate(values, 1, result, values[0], operator.mul)
        if calc_sum or calc_mul:
            sum += result
    return sum

def calculate(values, index, result, immediate_res, op):
    if index == len(values):
        return immediate_res == result
    return calculate(values, index + 1, result, op(immediate_res, values[index]), operator.add) or calculate(values, index + 1, result, op(immediate_res, values[index]), operator.mul)

def task2(tests):
    sum = 0
    for result, values in tests.items():
        calc_sum = new_calculate(values, 1, result, values[0], operator.add)
        calc_mul = new_calculate(values, 1, result, values[0], operator.mul)
        calc_conc = new_calculate(values, 1, result, values[0], concatenate_integers)
        if calc_sum or calc_mul or calc_conc:
            sum += result
    return sum

def new_calculate(values, index, result, immediate_res, op):
    if index == len(values):
        return immediate_res == result
    calc_sum = new_calculate(values, index + 1, result, op(immediate_res, values[index]), operator.add)
    calc_mul = new_calculate(values, index + 1, result, op(immediate_res, values[index]), operator.mul)
    calc_conc = new_calculate(values, index + 1, result, op(immediate_res, values[index]), concatenate_integers)
    return calc_sum or calc_mul or calc_conc

def concatenate_integers(a, b):
    return int(str(a) + str(b))

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    result = {}

    for line in lines:
        key, values = line.split(":")
        result[int(key.strip())] = list(map(int, values.split()))
    
    print(f"Task 1: {task1(result)}")
    print(f"Task 2: {task2(result)}")