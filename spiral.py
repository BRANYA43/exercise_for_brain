from tabulate import tabulate

move_left = False
move_right = True
move_up = False
move_down = False

rows = 13
columns = 8
steps = rows * columns
matrix = [[0 for j in range(columns)] for i in range(rows)]

min_x = 0
min_y = 0
max_x = rows - 1
max_y = columns - 1
x = 0
y = 0

for num in range(1, steps + 1):
    matrix[x][y] = num

    if move_right and y != max_y:
        y += 1
    elif move_right and y == max_y:
        move_right = False
        move_down = True
        min_x += 1

    if move_down and x != max_x:
        x += 1
    elif move_down and x == max_x:
        move_down = False
        move_left = True
        max_y -= 1

    if move_left and y != min_y:
        y -= 1
    elif move_left and y == min_y:
        move_left = False
        move_up = True
        max_x -= 1

    if move_up and x != min_x:
        x -= 1
    elif move_up and x == min_x:
        move_up = False
        move_right = True
        min_y += 1
        if move_right and y != max_y:
            y += 1

print(tabulate(matrix))
