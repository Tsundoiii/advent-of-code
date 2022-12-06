input = open("input.txt").read()

for i in range(len(input) - 4):
    for char in input[i:i + 4]:
        if input[i:i + 4].count(char) > 1:
            break
    else:
        print(f"{i + 4}: {input[i:i + 4]}")
        break