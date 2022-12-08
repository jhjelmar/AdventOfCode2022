import time


def day8():
    input = open("data\\day8_test.txt").read().split("\n")
    tree_grid = [[]]
    for i in input:
        tree_grid

    visible = []

    row_no = 0
    for row in tree_grid:
        highest_left = -1
        highest_right = -1

        for t in range(len(row)):
            if int(row[t]) > highest_left:
                visible.append(str(row_no) + "," + str(t))
                highest_left = int(row[t])

            if int(row[len(row)-t-1]) > highest_right:
                visible.append(str(row_no) + "," + str(len(row)-t))
                highest_right = int(row[len(row)-t-1])

        print(visible)
        row_no += 1


if __name__ == '__main__':
    start = time.perf_counter()
    day8()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
