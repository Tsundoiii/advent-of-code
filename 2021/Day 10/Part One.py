vals = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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

def fsum(l):
    global vals, genl, compl

    sum = 0

    for line in l:
        if compl(line, genl(line)) is not None:
            sum += vals[compl(line, genl(line))]

    return sum

print(f"Sum is: {fsum(lines)}")