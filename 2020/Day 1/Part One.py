nums = [int(x) for x in open('input.txt').readlines()]

table = {}

def sum_finder(nums: list[int]) -> int:
    for x in nums:
        table.update({x: 2020 - x})
        if table[x] in table:
            return x

print(f"The product is {(2020 - sum_finder(nums)) * 111}")