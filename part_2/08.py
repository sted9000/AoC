high_score = 0


def get_view_score(vista, tree_height):
    counter = 0
    for tree in vista:
        if tree < tree_height:
            counter += 1
        elif tree == tree_height:
            counter += 1
            return counter
    return counter


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
                continue

            else:
                north = get_view_score(reversed(columns[j][:i]), int(col))
                south = get_view_score(columns[j][i + 1:], int(col))
                west = get_view_score(reversed(rows[i][:j]), int(col))
                east = get_view_score(rows[i][j + 1:], int(col))

                score = north * south * west * east
                if score > high_score:
                    high_score = score

    print(high_score)