from functools import reduce

input = [[int(tree) for tree in treerow.rstrip()] for treerow in open("input.txt").readlines()]
columns = []

for j in range(len(input)):
    row = []
    for treerow in input:
        row.append(treerow[j])
    columns.append(row)

def before(row, index) -> list:
    if index == 0:
        return [0]
    elif index == 1:
        return [row[0]]
    else:
        return row[:index]

def after(row, index) -> list:
    if index == len(row) - 1:
        return [0]
    else:
        return row[index + 1:]

def scenic_score(i, j):
    tree = input[i][j]
    shorter_trees = []
    lengths = []

    #horizontal before
    for hb in before(input[i], j)[::-1]:
        if hb < tree:
            shorter_trees.append(hb)
        else:
            shorter_trees.append(1)
            break

    
    lengths.append(len(shorter_trees))
    shorter_trees.clear()

    #horizontal after
    for ha in after(input[i], j):
        if ha < tree:
            shorter_trees.append(ha)
        else:
            shorter_trees.append(1)
            break

    lengths.append(len(shorter_trees))
    shorter_trees.clear()

    #vertical before
    for vb in before(columns[j], i)[::-1]:
        if vb < tree:
            shorter_trees.append(vb)
        else:
            shorter_trees.append(1)
            break

    lengths.append(len(shorter_trees))
    shorter_trees.clear()

    #vertical after
    for va in after(columns[j], i):
        if va < tree:
            shorter_trees.append(va)
        else:
            shorter_trees.append(1)
            break

    lengths.append(len(shorter_trees))
    shorter_trees.clear()

    return reduce(lambda x, y: x * y, lengths)

highest = 0


for i, treerow in enumerate(input):
    for j, tree in enumerate(treerow):
        if (score := scenic_score(i, j)) > highest:
            highest = score

print(highest)