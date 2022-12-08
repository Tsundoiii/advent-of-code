input = open("input.txt").read()

for i in range(len(input) - 14):
    for char in input[i:i + 14]:
        if input[i:i + 14].count(char) > 1:
            break
    else:
        print(f"{i + 14}: {input[i:i + 14]}")
        break