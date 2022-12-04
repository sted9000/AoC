rps_dict = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
selection_dict = {'X': 1, 'Y': 2, 'Z': 3}

total = 0
with open('../inputs/02.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        game = (rps_dict[line[0]][line[-1]])
        selection = selection_dict[line[-1]]
        total += (game + selection)

print(total)
