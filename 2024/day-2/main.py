def task1(reports):
    safe_reports = 0
    for report in reports:
        safe_reports += check_report(report)
    return safe_reports

def check_report(report):
    increasing = False
    decreasing = False
    for index in range(len(report)-1):
        valid = False
        if report[index] < report[index+1] and report[index] >= (report[index+1]- 3):
            increasing = True
            valid = True
        elif report[index] > report[index+1] and (report[index] - 3)  <= report[index+1]:
            decreasing = True
            valid = True
        if not valid or increasing and decreasing:
            return 0
        if valid and index+1 == len(report)-1:
            return 1
    return 0


def task2(reports):
    safe_reports = 0
    for report in reports:
        if check_report(report) == 0:
            for index in range(len(report)):
                new_report = remove_at_index(report, index)
                if check_report(new_report) == 1:
                    safe_reports += 1
                    break
        elif check_report(report) == 1:
            safe_reports += 1
    return safe_reports



def remove_at_index(report, i):
    if 0 <= i < len(report):
        return report[:i] + report[i+1:]
    else:
        raise IndexError("Index out of range.")




if __name__ == '__main__':
    reports = []
    with open("input.txt") as file:
        reports = [list(map(int, line.strip().split(' '))) for line in file]

    print(f"Task 1: {task1(reports)}")
    print(f"Task 2: {task2(reports)}")
    

