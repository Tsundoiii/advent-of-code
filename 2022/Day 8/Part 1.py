input = [[int(tree) for tree in treerow.rstrip()] for treerow in open("input.txt").readlines()]
columns = []

for j in range(len(input)):
    row = []
    for treerow in input:
        row.append(treerow[j])
    columns.append(row)

visible = 0

def before(row, index):
    if index == 0:
        return []
    elif index == 1:
        return [row[0]]
    else:
        return row[:index]

def after(row, index):
    if index == len(row) - 1:
        return []
    else:
        return row[index + 1:]

for i, treerow in enumerate(input):
    for j, tree in enumerate(treerow):
        try:
            if max(before(treerow, j)) < tree or max(after(treerow, j)) < tree or max(before(columns[j], i)) < tree or max(after(columns[j], i)) < tree:
                visible += 1
        except ValueError:
            visible += 1

print(visible)
