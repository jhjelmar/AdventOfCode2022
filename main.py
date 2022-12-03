import string
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

    for game_round in input_list:
        match game_round:
            case "A X":
                part1_score += draw + rock
                part2_score += loss + scissors
            case "A Y":
                part1_score += win + paper
                part2_score += draw + rock
            case "A Z":
                part1_score += loss + scissors
                part2_score += win + paper
            case "B X":
                part1_score += loss + rock
                part2_score += loss + rock
            case "B Y":
                part1_score += draw + paper
                part2_score += draw + paper
            case "B Z":
                part1_score += win + scissors
                part2_score += win + scissors
            case "C X":
                part1_score += win + rock
                part2_score += loss + paper
            case "C Y":
                part1_score += loss + paper
                part2_score += draw + scissors
            case "C Z":
                part1_score += draw + scissors
                part2_score += win + rock

    print(part1_score)
    print(part2_score)

    #14375
    #10274
    #Execution time (ms): 0.5049000028520823


def intersect(string1, string2):
    common = []
    for char in set(string1):
        common.extend(char * min(string1.count(char), string2.count(char)))

    return common


def day3_part1():
    rucksacks = open("data\\day3.txt").read().split("\n")
    priority_sum = 0

    for rucksack in rucksacks:
        l = len(rucksack)
        item = intersect(rucksack[0:l//2], rucksack[l//2:])

        priority = string.ascii_lowercase.index(item[0].lower()) + 1
        if item[0].isupper():
            priority += 26

        priority_sum += priority

    print(priority_sum)


def day3_part2():
    rucksacks = open("data\\day3.txt").read().split("\n")
    start_index = 0
    stop_index = 3
    take = 3
    priority_sum = 0

    while start_index < len(rucksacks):
        group = rucksacks[start_index: stop_index]
        start_index += take
        stop_index += take

        first_intersect = list(set((intersect(group[0], group[1]))))
        item = intersect(first_intersect, group[2])[0]

        priority = string.ascii_lowercase.index(item.lower()) + 1
        if item[0].isupper():
            priority += 26

        priority_sum += priority

    print(priority_sum)


if __name__ == '__main__':
    start = time.perf_counter()

    day3_part2()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
