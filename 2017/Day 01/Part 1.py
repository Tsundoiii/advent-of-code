input = open("input.txt").read().rstrip()

sum = 0

for i in range(len(input) - 1):
    if int(input[i]) == int(input[i + 1]):
        sum += int(input[i])

if int(input[-1]) == int(input[0]):
    sum += int(input[-1])
    
print(sum)