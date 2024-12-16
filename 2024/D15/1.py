import copy
import re
import math as m

with open("input.txt", "r") as file:
    data = file.read().split("\n\n")

map = [[char for char in line] for line in data[0].split("\n")]
moves = data[1].replace("\n", "")


def try_move(move, x, y):
    if move == "^":
        i = -1
        j = 0
    elif move == "v":
        i = 1
        j = 0
    elif move == "<":
        i = 0
        j = -1
    elif move == ">":
        i = 0
        j = 1
    else:
        return x, y  # In case of invalid move
    moved_items = 0
    # We need the next cell to not be a wall, but we stop if the cell after that is empty
    # Also, we stop if we find a wall with no empty space before it, we can't move at all
    # My code is kinda ugly, I guess there is a easier way to do this

    while (
        map[x + (moved_items + 1) * i][y + (moved_items + 1) * j] != "#"
        and map[x + (moved_items) * i][y + (moved_items) * j] != "."
    ):
        if (
            map[x + (moved_items + 1) * i][y + (moved_items + 1) * j] != "."
            and map[x + (moved_items + 2) * i][y + (moved_items + 2) * j] == "#"
        ):
            moved_items = 0
            break
        else:
            moved_items += 1
    if moved_items == 0:
        return x, y
    else:
        for k in range(moved_items, 0, -1):
            map[x + k * i][y + k * j] = map[x + (k - 1) * i][y + (k - 1) * j]
        map[x][y] = "."
        return x + i, y + j


for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "@":
            x = i
            y = j


for move in moves:
    x, y = try_move(move, x, y)


def score_p1(map):
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                sum += 100 * i + j
    return sum


print(score_p1(map))
