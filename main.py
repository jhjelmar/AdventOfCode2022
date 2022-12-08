import time


def day8_part1():
    input = open("data\\day8.txt").read().split("\n")

    tree_grid = []
    visible = []

    for x in input:
        tree_grid.append([*x])

    for row in range(len(tree_grid)):
        highest_left = -1
        highest_right = -1

        column_length = len(tree_grid[0])

        for column in range(column_length):
            reverse_column = column_length - 1 - column

            if int(tree_grid[row][column]) > highest_left:
                visible.append(str(row) + "," + str(column))
                highest_left = int(tree_grid[row][column])

            if int(tree_grid[row][reverse_column]) > highest_right:
                visible.append(str(row) + "," + str(reverse_column))
                highest_right = int(tree_grid[row][reverse_column])

    for column in range(len(tree_grid[0])):
        highest_up = -1
        highest_down = -1

        row_length = len(tree_grid)

        for row in range(row_length):
            reverse_row = row_length - 1 - row

            if int(tree_grid[row][column]) > highest_up:
                visible.append(str(row) + "," + str(column))
                highest_up = int(tree_grid[row][column])

            if int(tree_grid[reverse_row][column]) > highest_down:
                visible.append(str(reverse_row) + "," + str(column))
                highest_down = int(tree_grid[reverse_row][column])

    print(len(set(visible)))


def day8_part2():
    input = open("data\\day8.txt").read().split("\n")

    tree_grid = []

    for x in input:
        tree_grid.append([*x])

    row_length = len(tree_grid)
    column_length = len(tree_grid[0])
    radius_max = max(row_length, column_length)
    highest_scenic_score = 0

    for row in range(row_length):
        for column in range(column_length):

            visible_trees_right = 0
            visible_trees_left = 0
            visible_trees_up = 0
            visible_trees_down = 0
            stop_right = False
            stop_left = False
            stop_up = False
            stop_down = False

            for radius in range(1, radius_max):
                if column + radius < column_length and not stop_right:
                    if tree_grid[row][column] > tree_grid[row][column+radius]:
                        visible_trees_right += 1
                    elif tree_grid[row][column] <= tree_grid[row][column+radius]:
                        visible_trees_right += 1
                        stop_right = True

                if column - radius >= 0 and not stop_left:
                    if tree_grid[row][column] > tree_grid[row][column-radius]:
                        visible_trees_left += 1
                    elif tree_grid[row][column] <= tree_grid[row][column-radius]:
                        visible_trees_left += 1
                        stop_left = True

                if row + radius < row_length and not stop_down:
                    if tree_grid[row][column] > tree_grid[row+radius][column]:
                        visible_trees_down += 1
                    elif tree_grid[row][column] <= tree_grid[row+radius][column]:
                        visible_trees_down += 1
                        stop_down = True

                if row - radius >= 0 and not stop_up:
                    if tree_grid[row][column] > tree_grid[row-radius][column]:
                        visible_trees_up += 1
                    elif tree_grid[row][column] <= tree_grid[row-radius][column]:
                        visible_trees_up += 1
                        stop_up = True

            score = visible_trees_right * visible_trees_left * visible_trees_up * visible_trees_down
            highest_scenic_score = max(highest_scenic_score, score)
            print("{"+str(row)+","+str(column)+"}", score)
    print(highest_scenic_score)


if __name__ == '__main__':
    start = time.perf_counter()
    day8_part2()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
