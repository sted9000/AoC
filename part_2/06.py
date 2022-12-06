def no_duplicates(my_list):
    my_set = set(my_list)
    return len(my_list) == len(my_set)


packet_length = 14
with open('../inputs/06.txt') as f:
    line = f.read().splitlines()[0]
    for i in range(len(line)):
        packet = line[i:i + packet_length]
        if no_duplicates(packet):
            print(i + packet_length)
            break
