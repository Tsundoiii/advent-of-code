input = [ #open("input.txt").readlines()
"$ cd /",
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

class File(Node):
    def __init__(self, parent: Directory, size: int):
        self.parent: Directory = parent
        self.size: int = size

root = Directory("/", None)
current_directory = root
directories: list[Directory] = []

for i in range(1, len(input)):
    line = input[i]
    if line[0] == "$":
        match line[1]:
            case "cd":
                if line[2] == "..":
                    current_directory = current_directory.parent
                else:
                    for child in current_directory.children:
                        if isinstance(child, Directory) and child.name == list[2]:
                            current_directory = child
            case "ls":
                pass
    else:
        continue

sum = 0

for directory in directories:
    if s := directory.size() <= 100000:
        sum += s

print(sum)