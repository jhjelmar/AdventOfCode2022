def solve():
    stream = open("data\\day6.txt").read()
    packet_marker = 4
    message_marker = 14

    for x in range(len(stream)):
        if len(set(stream[x:x+packet_marker])) == packet_marker:
            print(x+packet_marker)
            break

    for x in range(len(stream)):
        if len(set(stream[x:x + message_marker])) == message_marker:
            print(x + message_marker)
            break
