def solve():
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