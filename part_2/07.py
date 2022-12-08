paths = {}
current_path = ''

with open('../inputs/07.txt') as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        split_line = line.split(' ')

        # commands
        if split_line[0] == '$':

            # change directory
            if split_line[1] == 'cd':

                # go back
                if split_line[2] == '..':
                    # remove end of current path
                    current_path = '/'.join(current_path.split('/')[:-2]) + '/'

                # go forward
                else:

                    # update path
                    if current_path == '':
                        current_path += split_line[2]
                    else:
                        current_path += (split_line[2] + '/')

                    # add key:value to paths
                    if current_path not in paths.keys():
                        paths[current_path] = 0

        # files size and names
        elif split_line[0] != 'dir':

            # add file size to paths[current_path]
            paths[current_path] += int(split_line[0])

    # add children directories sizes to parent
    final_dic = paths.copy()
    for key, value in paths.items():
        for key_0, value_0 in paths.items():
            if key_0.startswith(key) and key != key_0:
                final_dic[key] += value_0

    # find how much space we need to free up
    used_space = sum(paths.values())
    space_left = 70000000 - used_space
    space_needed = 30000000 - space_left

    # find the smallest directory that frees up enough space
    current_value = 9999999999999999
    for value in final_dic.values():
        if space_needed <= value < current_value:
            current_value = value

    print(current_value)
