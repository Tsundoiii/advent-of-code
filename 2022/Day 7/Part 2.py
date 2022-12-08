input = [node.rstrip() for node in open("input.txt").readlines()]

input = [line.split(" ") for line in input]

class Node:
    pass

class Directory(Node):
    def __init__(self, name: str, parent: Node):
        self.name: str = name
        self.parent: Node = parent
        self.children: list[File | Directory] = []

    def add(self, node: Node):
        self.children.append(node)

    def size(self) -> int:
        size: int = 0

        for child in self.children:
            if isinstance(child, File):
                size += child.size
            elif isinstance(child, Directory):
                size += child.size()

        return size

class File(Node):
    def __init__(self, name: str, size: int, parent: Directory):
        self.name: str = name
        self.parent: Directory = parent
        self.size: int = size

root = Directory("/", None)
current_directory = root
directories: list[Directory] = []

for i in range(1, len(input)):
    line = input[i]
    if line[1] == "ls":
        continue
    elif line[1] == "cd":
        if line[2] == "..":
            current_directory = current_directory.parent
        else:
            for child in current_directory.children:
                if isinstance(child, Directory) and child.name == line[2]:
                    current_directory = child
    else:
        if line[0] == "dir":
            new_directory = Directory(line[1], current_directory)
            current_directory.add(new_directory)
            directories.append(new_directory)
        elif line[0] != "$":
            current_directory.add(File(line[1], int(line[0]), current_directory))
            
#print([{c.name: c.size()} for c in directories])

unused = 70000000 - root.size()
current_smallest = directories[0]
valid = []

for directory in directories:
    print({directory.name: directory.size()})
    if directory.size() + unused >= 30000000:
        valid.append(directory.size())

print(min(valid))
