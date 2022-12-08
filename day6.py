def solve():
    input_text = open("data\\day6.txt").read()

    find_marker(input_text, 4)
    find_marker(input_text, 14)


def find_marker(text, size):
    for x in range(len(text)):
        if len(set(text[x:x+size])) == size:
            print(x+size)
            break
