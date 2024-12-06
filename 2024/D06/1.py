import copy
import re

file = open("input", "r")
data = file.readlines()
data = [line.strip() for line in data]
map = [[char for char in line] for line in data]

up = 1
right = 2
down = 3
left = 4


def turn(direction):
    if direction < 4:
        return direction + 1
    return 1


for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "^":
            x = i
            y = j
            map[x][y] = "X"

map

dir = 1


while True:
    # Oui je sais le while true c'est moche
    if dir == up:
        x1 = x - 1
        y1 = y
    elif dir == down:
        x1 = x + 1
        y1 = y
    elif dir == right:
        x1 = x
        y1 = y + 1
    else:
        x1 = x
        y1 = y - 1

    if x1 >= len(map) or x1 < 0 or y1 >= len(map[0]) or y1 < 0:
        break  # On est sorti de la carte

    else:
        if map[x1][y1] == "#":
            # obstacle
            dir = turn(dir)
        else:
            x = x1
            y = y1
            map[x][y] = "X"

sum = 0

for line in map:
    for char in line:
        if char == "X":
            sum += 1

sum
