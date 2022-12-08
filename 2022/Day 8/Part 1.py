input = [[int(tree) for tree in treerow.rstrip()] for treerow in open("input.txt").readlines()]

visible = 0

def visible_in_row(forest):
    pass

def visibie_in_column(forest):
    pass

for treerow in input:
    for tree in treerow:
        if input.index(treerow) == 0 or input.index(treerow) == len(treerow) - 1:
            visible += 1
