items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0
with open('../inputs/03.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        compartment_1, compartment_2 = line[:len(line) // 2], line[len(line) // 2:]
        for item in compartment_1:
            if item in compartment_2:
                total += (items.index(item) + 1)
                break  # don't want to double count!

    print(total)
