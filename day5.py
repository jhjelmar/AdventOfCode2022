def solve():
    part1()
    part2()


def cargo_setup():
    stack1 = ['S', 'T', 'H', 'F', 'W', 'R']
    stack2 = ['S', 'G', 'D', 'Q', 'W']
    stack3 = ['B', 'T', 'W']
    stack4 = ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J']
    stack5 = ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z']
    stack6 = ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G']
    stack7 = ['Z', 'B', 'R', 'T', 'W', 'G', 'P']
    stack8 = ['N', 'G', 'M', 'T', 'C', 'J', 'R']
    stack9 = ['L', 'G', 'B', 'W']

    return [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]


def part1():
    cargo = cargo_setup()
    procedure = open("data\\day5.txt").read().split("\n")

    for step in procedure:
        instructions = step.split(" ")
        from_cargo = int(instructions[3]) - 1
        to_cargo = int(instructions[5]) - 1

        for x in range(int(instructions[1])):
            item = cargo[from_cargo].pop()
            cargo[to_cargo].append(item)

    message = ""
    for x in cargo:
        message += x.pop()

    print(message)
    # ZRLJGSCTR


def part2():
    cargo = cargo_setup()
    procedure = open("data\\day5.txt").read().split("\n")

    for step in procedure:
        instructions = step.split(" ")
        from_cargo = int(instructions[3]) - 1
        to_cargo = int(instructions[5]) - 1

        temp_list = []
        for x in range(int(instructions[1])):
            item = cargo[from_cargo].pop()
            temp_list.append(item)

        for x in range(int(instructions[1])):
            item = temp_list.pop()
            cargo[to_cargo].append(item)

    message = ""
    for x in cargo:
        message += x.pop()

    print(message)
    # PRTTGRFPB