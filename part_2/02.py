rps_dict = {'A': {'X': 'C', 'Y': 'A', 'Z': 'B'}, 'B': {'X': 'A', 'Y': 'B', 'Z': 'C'}, 'C': {'X': 'B', 'Y': 'C', 'Z': 'A'}}
selection_dict = {'A': 1, 'B': 2, 'C': 3}
outcome_dict = {'X': 0, 'Y': 3, 'Z': 6}

total = 0
with open('../inputs/02.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        game = outcome_dict[line[-1]]
        selection = selection_dict[rps_dict[line[0]][line[-1]]]
        total += (game + selection)

print(total)
