import re


def solve():
    part1()
    part2()


def part1():
    assignment_pairs = open("data\\day4.txt").read().split("\n")

    fully_contained_pair = 0

    for assignment_pair in assignment_pairs:
        area_boundaries = re.split('\W+', assignment_pair)

        if (
                (int(area_boundaries[0]) <= int(area_boundaries[2]) and
                 int(area_boundaries[1]) >= int(area_boundaries[3]))
                or
                (int(area_boundaries[2]) <= int(area_boundaries[0]) and
                 int(area_boundaries[3]) >= int(area_boundaries[1]))):
            fully_contained_pair += 1

    print(fully_contained_pair)
    # 494


def part2():
    assignment_pairs = open("data\\day4.txt").read().split("\n")
    overlapping = 0

    for assignment_pair in assignment_pairs:
        area_boundaries = re.split('\W+', assignment_pair)

        range1 = range(int(area_boundaries[0]), int(area_boundaries[1]) + 1)
        range2 = range(int(area_boundaries[2]), int(area_boundaries[3]) + 1)

        overlapping_range = range(max(range1[0], range2[0]), min(range1[-1], range2[-1]) + 1)

        temp = list(overlapping_range)
        if len(temp) > 0:
            overlapping += 1

    print(overlapping)
    # 833