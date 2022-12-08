from hashlib import new


input = [
"$ cd /", #open("input.txt").readlines()
"$ ls",
"dir a",
"14848514 b.txt",
"8504156 c.dat",
"dir d",
"$ cd a",
"$ ls",
"dir e",
"29116 f",
"2557 g",
"62596 h.lst",
"$ cd e",
"$ ls",
"584 i",
"$ cd ..",
"$ cd ..",
"$ cd d",
"$ ls",
"4060174 j",
"8033020 d.log",
"5626152 d.ext",
"7214296 k"
]
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
    if line[1] == "cd":
        print(line)
        if line[2] == "..":
            current_directory = current_directory.parent
        else:
            print([c.name for c in current_directory.children])
            for child in current_directory.children:
                if isinstance(child, Directory) and child.name == list[2]:
                    current_directory = child
    else:
        if line[0] == "dir":
            new_directory = Directory(line[1], current_directory)
            current_directory.add(new_directory)
            directories.append(new_directory)
            print(new_directory.name + " " + new_directory.parent.name + " " + str([c.name for c in current_directory.children]))
        elif line[0] != "$":
            current_directory.add(File(line[1], int(line[0]), current_directory))

sum = 0

for directory in directories:
    if s := directory.size() <= 100000:
        sum += s

print(sum)