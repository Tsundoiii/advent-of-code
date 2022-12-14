from itertools import zip_longest

input = [[eval(packet) for packet in pair.splitlines()] for pair in open("input.txt").read().split("\n\n")]
sum = 0

def compare(left: list, right: list) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return False
        elif left == right:
            return None
        else:
            return True
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

    for left_value, right_value in zip_longest(left, right):
        if left_value is None:
            return True
        elif right_value is None:
            return False
        elif left_value == right_value:
            continue
        else:
            if isinstance(left_value, list) or isinstance(right_value, list):
                return compare(left_value, right_value)
            else:
                return left_value < right_value

    return True

for i in range(len(input)):
    left = input[i][0]
    right = input[i][1]

    if compare(left, right):
        sum += i + 1

print(sum)