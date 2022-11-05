numsList = [int(x) for x in open('input.txt').readlines()]

for i in numsList:
    for j in numsList:
        for k in numsList:
            if i + j + k == 2020:
                nums = [i, j, k]

print(f"The product is {nums[0] * nums[1] * nums[2]}")