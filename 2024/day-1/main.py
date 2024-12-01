from pandas import *


def task1(list1, list2):
    total_distance = 0
    for index in range(len(list1)):
        if list1[index] <= list2[index]:
            total_distance += list2[index] - list1[index]
        else:
            total_distance += list1[index] - list2[index]
    return total_distance
    
def task2(list1, list2):
    score = 0
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                score += num1
            elif num1 > num2:
                continue
    return score
            
if __name__ == '__main__':
    data = read_csv("./input.csv", header=None, delim_whitespace=True)
    list1 = data[0].to_list()
    list2 = data[1].to_list()
    list1.sort()
    list2.sort()
    print(f"Task 1: {task1(list1, list2)}")
    print(f"Task 2: {task2(list1, list2)}")