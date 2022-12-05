import string


def intersect(string1, string2):
    common = []
    for char in set(string1):
        common.extend(char * min(string1.count(char), string2.count(char)))

    return common


def part1():
    rucksacks = open("data\\day3.txt").read().split("\n")
    priority_sum = 0

    for rucksack in rucksacks:
        l = len(rucksack)
        item = list(set(rucksack[0:l // 2]) & set(rucksack[l // 2:]))

        priority = string.ascii_lowercase.index(item[0].lower()) + 1
        if item[0].isupper():
            priority += 26

        priority_sum += priority

    print(priority_sum)
    #7568


def part2():
    rucksacks = open("data\\day3.txt").read().split("\n")
    start_index = 0
    stop_index = 3
    take = 3
    priority_sum = 0

    while start_index < len(rucksacks):
        group = rucksacks[start_index: stop_index]
        start_index += take
        stop_index += take

        item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]

        priority = string.ascii_lowercase.index(item.lower()) + 1
        if item[0].isupper():
            priority += 26

        priority_sum += priority

    print(priority_sum)
    #2780