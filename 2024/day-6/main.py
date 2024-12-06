
def simulate(grid, next_row, next_col, start_pos):
    max_rows = len(grid)
    max_col = len(grid[0])
    visited = set()
    (current_row, current_col) = start_pos

    while True:
        visited.add((current_row, current_col))

        north_bound = current_row + next_row < 0
        south_bound = current_row + next_row >= max_rows
        west_bound = current_col + next_col < 0
        east_bound = current_col + next_col >= max_col

        if north_bound or south_bound  or west_bound or east_bound :
            break 
        
        if grid[current_row + next_row][current_col + next_col] == '#':
            (next_col, next_row) = (-next_row, next_col)
        else:
            current_row += next_row
            current_col += next_col
    return visited


def task1(grid):
    
    start_pos = (0, 0)

    for x_index, line in enumerate(grid):
        if '^' in line:
            y_index = line.index('^')
            start_pos = (x_index, y_index)
    
    (next_row, next_col) = (-1, 0)

    num_x = simulate(grid, next_row, next_col, start_pos)

    return len(num_x)

def simulate_looped(grid, next_row, next_col, start_pos):
    max_rows = len(grid)
    max_col = len(grid[0])
    visited = set()
    (current_row, current_col) = start_pos

    while True:
        visited.add((current_row, current_col, next_row, next_col))

        north_bound = current_row + next_row < 0
        south_bound = current_row + next_row >= max_rows
        west_bound = current_col + next_col < 0
        east_bound = current_col + next_col >= max_col

        if north_bound or south_bound  or west_bound or east_bound :
            break 
        
        if grid[current_row + next_row][current_col + next_col] == '#':
            (next_col, next_row) = (-next_row, next_col)
        else:
            current_row += next_row
            current_col += next_col
        if (current_row, current_col, next_row, next_col) in visited:
            return True
    return False    
  

def task2(grid):
    start_pos = (0, 0)

    for x_index, line in enumerate(grid):
        if '^' in line:
            y_index = line.index('^')
            start_pos = (x_index, y_index)
    
    (next_row, next_col) = (-1, 0)
    
    loops = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                continue
            grid[row][col] = '#'
            if simulate_looped(grid, next_row, next_col, start_pos):
                loops += 1
            grid[row][col] = '.'
    
    return loops


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]

    print("f")
    
    print(f"Task 1: {task1(grid)}")
    print(f"Task 2: {task2(grid)}")