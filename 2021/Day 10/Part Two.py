vals = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

syms = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

with open("input.txt") as bonanza:
    lines = bonanza.readlines()

for line in lines:
    lines[lines.index(line)] = line.replace("\n", "")

def genl(line):
    global syms

    nline = []
    
    for count, char in enumerate(line):
        if char in syms.keys():
            nline.insert(count, char)
            nline.insert(count + 1, syms[char])

    return "".join(nline)

def compl(l1, l2):
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            print(l1)
            print(l2)
            return c1

def fsum(lines):
    global vals, genl, compl

    for line in lines:
        if compl(line, genl(line)) is not None:
            lines.remove(line)

    return lines

lines = fsum(lines)

for line in lines:
    print(line)