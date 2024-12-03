import re

def task1(text):
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

    sum = 0
    for mul in muls:
        (a, b) = str(mul).replace("mul(", "").replace(")", "").split(",")
        sum += int(a) * int(b)
    
    return sum

def task2(text):
    expressions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", text)

    sum = 0
    do_next_mul = True
    for expression in expressions:
        if expression == "don't()":
            do_next_mul = False
            continue
        elif expression == "do()":
            do_next_mul = True
            continue
        if not do_next_mul:
            continue
        (a, b) = str(expression).replace("mul(", "").replace(")", "").split(",")
        sum += int(a) * int(b)
    return sum

if __name__ == '__main__':
    file = open("input.txt")
    text = file.read()
    print(f"Task 1: {task1(text)}")
    print(f"Task 2: {task2(text)}")