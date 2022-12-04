items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0
group_size = 3
with open('../inputs/03.txt') as f:
    elves = f.read().splitlines()
    for i, elf in enumerate(elves):
        if i == 0 or i % 3 == 0:
            for item in elf:
                if item in elves[i+1] and item in elves[i+2]:
                    total += (items.index(item) + 1)
                    break

    print(total)