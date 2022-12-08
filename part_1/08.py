visible = 0


with open('../inputs/08.txt') as f:
    lines = f.read().splitlines()

    # make list of rows and list of columns
    rows = []
    columns = [[] for _ in range(len(lines[0]))]
    for i, row in enumerate(lines):
        current_row = []
        for j, col in enumerate(row):
            current_row.append(int(col))
            columns[j].append(int(col))
        rows.append(current_row)

    for i, row in enumerate(lines):
        for j, col in enumerate(row):

            # "edge cases"
            if i == 0 or i == len(lines) - 1 or j == 0 or j == len(row) - 1:
                visible += 1

            else:

                # see if no trees to the north provide cover (col)
                # note: remember [inclusive:exclusive] list slicing
                if max(columns[j][:i]) < int(col):
                    visible += 1

                # south
                elif max(columns[j][i+1:]) < int(col):
                    visible += 1

                # west
                elif max(rows[i][:j]) < int(col):
                    visible += 1

                # east
                elif max(rows[i][j+1:]) < int(col):
                    visible += 1

    print(visible)
