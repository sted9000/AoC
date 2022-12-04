with open('../inputs/04.txt') as f:
    lines = f.read().splitlines()
    counter = 0
    pairs = []
    for line in lines:
        pair = []
        for assignment in line.split(','):
            r = assignment.split('-')
            pair.append(list(range(int(r[0]), int(r[1]) + 1)))
        pairs.append(pair)

    for pair in pairs:
        x = all(el in pair[0] for el in pair[1])
        y = all(el in pair[1] for el in pair[0])
        if x or y:
            counter += 1

    print(counter)
