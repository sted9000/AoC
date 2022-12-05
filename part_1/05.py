import re

with open('../inputs/05.txt') as f:

    # format input
    lines = f.read().splitlines()
    stack_lines = []
    move_lines = []
    for line in lines:
        if line.startswith('['):
            stack_lines.append(line)
        elif line.startswith('m'):
            move_lines.append(line)

    # get stacks
    stacks = [[] for x in range(9)]
    for line in stack_lines:
        for i, stack in enumerate(stacks):
            crate_index = i * 4 + 1  # just eyeballed this
            if len(line) >= crate_index and line[crate_index].isalpha():  # is a letter
                stacks[i].append(line[crate_index])

    # move crates
    for line in move_lines:
        split_line = line.split(' ')
        num, start, end = [int(split_line[1]), int(split_line[3]), int(split_line[5])]
        for n in range(num):
            crate = stacks[start - 1].pop(0)
            stacks[end - 1].insert(0, crate)

    # format answer
    final_string = ''
    for stack in stacks:
        final_string += stack[0]
    print(final_string)