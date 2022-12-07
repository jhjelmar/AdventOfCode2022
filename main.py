import time


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.subdirectories = []

    def calculate_size(self, total_size):
        calculated_size = self.size

        for sub in self.subdirectories:
            result = sub.calculate_size(total_size)
            calculated_size += result[0]
            total_size = result[1]

        if calculated_size <= 100000:
            total_size += calculated_size

        return calculated_size, total_size

    def find_smallest_to_delete(self, space_req, smallest):
        calculated_size = self.size

        for sub in self.subdirectories:
            result = sub.find_smallest_to_delete(space_req, smallest)
            calculated_size += result[0]
            smallest = result[1]

        if space_req <= calculated_size < smallest:
            smallest = calculated_size

        return calculated_size, smallest


def day7():
    input_list = open("data\\day7.txt").read().split("\n")
    root = Directory("root")
    active = root

    for line in input_list:
        if line == "$ cd /":
            active = root
        elif line == "$ cd ..":
            active = active.parent
        elif line.startswith("$ cd "):
            for sub in active.subdirectories:
                if sub.name == line[5:]:
                    active = sub
                    break
        elif line[0].isdigit():
            active.size += int(line[:line.index(" ")])
        elif line.startswith("dir"):
            active.subdirectories.append(Directory(line[4:], active))

    result = root.calculate_size(0)
    space_req = 30000000 - (70000000 - result[0])
    result2 = root.find_smallest_to_delete(space_req, result[0])

    print(result[1])
    print(result2[1])


if __name__ == '__main__':
    start = time.perf_counter()
    day7()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
