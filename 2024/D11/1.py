import copy
import re

file = open("input.txt", "r")
data = file.readline().strip().split(" ")
data = [int(char) for char in data]


for i in range(25):
    print(i)
    new_data = []
    for stone in data:
        if stone == 0:
            new_data.append(1)
        else:
            stone_string = str(stone)
            stone_len = len(stone_string)
            if not stone_len % 2:
                new_data.append(int(stone_string[: stone_len // 2]))
                new_data.append(int(stone_string[stone_len // 2 :]))
            else:
                new_data.append(stone * 2024)
    data = new_data

print(len(data))
