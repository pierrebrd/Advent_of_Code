import copy
import re
from math import log10

file = open("input.txt", "r")
data = file.readline().strip().split(" ")
data = [int(char) for char in data]

# We can't just replace 25 by 75, it really is too slow
# We will need some memory


def blink(blinks_to_do, stone):
    if not blinks_to_do:
        return 1

    if stone in memo[blinks_to_do]:
        return memo[blinks_to_do][stone]

    if not stone:
        result = blink(blinks_to_do - 1, 1)
    else:
        stone_string = str(stone)
        digits = len(stone_string)
        if not digits % 2:  # Even number
            result = blink(blinks_to_do - 1, int(stone_string[: digits // 2])) + blink(
                blinks_to_do - 1, int(stone_string[digits // 2 :])
            )
        else:
            result = blink(blinks_to_do - 1, 2024 * stone)
    memo[blinks_to_do][stone] = result
    return result


sum = 0
blinks = 75
memo = [{} for i in range(blinks + 1)]
for stone in data:
    print(stone)
    sum += blink(blinks, stone)

sum
