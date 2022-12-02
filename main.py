import time


def sum_inventory_calories(sum_inventory_input):
    individual_inventory = []

    elf_no = 0
    individual_inventory.append(0)
    for x in sum_inventory_input:
        if x != '':
            individual_inventory[elf_no] = individual_inventory[elf_no] + int(x)
        else:
            elf_no += 1
            individual_inventory.append(0)

    return individual_inventory


def day1():
    input_list = open("data\\day1.txt").read().split("\n")
    inventories_list = sum_inventory_calories(input_list)
    inventories_list.sort(reverse=True)
    print(inventories_list[0])
    print(sum(inventories_list[:3]))

    # 72240
    # 210957
    # Execution time (ms): 0.42569986544549465


def day2():
    input_list = open("data\\day2.txt").read().split("\n")
    part1_score = 0
    part2_score = 0
    win = 6
    draw = 3
    loss = 0
    rock = 1
    paper = 2
    scissors = 3

    for x in input_list:
        game_round = x.split(" ")

        match game_round[0]:
            case 'A':
                match game_round[1]:
                    case 'X':
                        part1_score += draw + rock
                        part2_score += loss + scissors
                    case 'Y':
                        part1_score += win + paper
                        part2_score += draw + rock
                    case 'Z':
                        part1_score += loss + scissors
                        part2_score += win + paper
            case 'B':
                match game_round[1]:
                    case 'X':
                        part1_score += loss + rock
                        part2_score += loss + rock
                    case 'Y':
                        part1_score += draw + paper
                        part2_score += draw + paper
                    case 'Z':
                        part1_score += win + scissors
                        part2_score += win + scissors
            case 'C':
                match game_round[1]:
                    case 'X':
                        part1_score += win + rock
                        part2_score += loss + paper
                    case 'Y':
                        part1_score += loss + paper
                        part2_score += draw + scissors
                    case 'Z':
                        part1_score += draw + scissors
                        part2_score += win + rock

    print(part1_score)
    print(part2_score)

    #14375
    #10274
    #Execution time (ms): 0.5366001278162003


if __name__ == '__main__':
    start = time.perf_counter()

    day2()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
