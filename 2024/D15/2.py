# After a long time of debugging, my code works, but it is horrible. I should have better handled the dependecies between the boxes.
# Some workaround seen on reddit :
# - Make a backup of the map : if some push become invalid, restore the map
# - Use two separates fonctions, one to check if a push is valid and appending the move to a list, and another one to make the pushes when the are valid


import copy
import re
import math as m
import time

with open("/home/pierre/Documents/Advent_Of_Code/2024/D15/input.txt", "r") as file:
    data = file.read().split("\n\n")

map = [[char for char in line] for line in data[0].split("\n")]

for i in range(len(map)):
    newline = []
    for char in map[i]:
        if char == "@":
            newline += ["@", "."]
        elif char == "#":
            newline += ["#", "#"]
        elif char == ".":
            newline += [".", "."]
        elif char == "O":
            newline += ["[", "]"]
    map[i] = newline

# Debugging

# count1 = 0
# count2 = 0
# count3 = 0
# for line in map:
#     for char in line:
#         if char == "[":
#             count1 += 1
#         if char == "]":
#             count2 += 1
#         if char == "#":
#             count3 += 1

# print(count1, count2, count3)


def print_map():
    for line in map:
        print("".join(line))


moves = data[1].replace("\n", "")


def cancel_moves(moved_list, move):
    if moved_list != []:
        print(moved_list)
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
    for k in range(len(moved_list) - 1, -1, -1):
        x, y = moved_list[k]
        map[x + i][y + j] = "."
        map[x + i][y + j + 1] = "."
        map[x][y] = "["
        map[x][y + 1] = "]"


def move_box(moved_list, move, x, y):
    # move the box if it can be moved, and return a boolean indicating if the box was moved
    # It recursively move all the boxes that can be moved
    # y is the position of the left corner of the box
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
        return False  # In case of invalid move

    if move in ["^", "v"]:
        # Vertical move
        if map[x + i][y] == "#" or map[x + i][y + 1] == "#":
            return False
        if map[x + i][y] == "." and map[x + i][y + 1] == ".":
            map[x + i][y] = "["
            map[x + i][y + 1] = "]"
            map[x][y] = "."
            map[x][y + 1] = "."
            moved_list.append((x, y))
            return True

        if map[x + i][y] == "[":
            movable = move_box(moved_list, move, x + i, y)
            if movable == True:
                map[x + i][y] = "["
                map[x + i][y + 1] = "]"
                map[x][y] = "."
                map[x][y + 1] = "."
                moved_list.append((x, y))
                return True
            else:
                return False
        if map[x + i][y] == "]" and map[x + i][y + 1] == ".":
            movable = move_box(moved_list, move, x + i, y - 1)
            if movable == True:
                map[x + i][y] = "["
                map[x + i][y + 1] = "]"
                map[x][y] = "."
                map[x][y + 1] = "."
                moved_list.append((x, y))
                return True
            else:
                return False
        if map[x + i][y + 1] == "[" and map[x + i][y] == ".":
            movable = move_box(moved_list, move, x + i, y + 1)
            if movable == True:
                map[x + i][y] = "["
                map[x + i][y + 1] = "]"
                map[x][y] = "."
                map[x][y + 1] = "."
                moved_list.append((x, y))
                return True
            else:
                return False
        if map[x + i][y] == "]" and map[x + i][y + 1] == "[":
            movable1 = move_box(moved_list, move, x + i, y - 1)
            if movable1 == True:
                movable2 = move_box(moved_list, move, x + i, y + 1)
                if movable2 == True:
                    map[x + i][y] = "["
                    map[x + i][y + 1] = "]"
                    map[x][y] = "."
                    map[x][y + 1] = "."
                    moved_list.append((x, y))
                    return True
                else:
                    # Buggy and not needed
                    # moved_list.remove((x + i, y - 1))
                    # if move == "^":
                    #     move_box(moved_list, "v", x + 2 * i, y - 1)
                    # else:
                    #     move_box(moved_list, "^", x + 2 * i, y - 1)
                    return False
    else:
        # Horizontal move
        # It depends on the direction
        if move == "<":
            if map[x][y + j] == ".":
                map[x][y + j] = "["
                map[x][y + j + 1] = "]"
                map[x][y + j + 2] = "."
                moved_list.append((x, y))
                return True
            if map[x][y + j] == "]":
                movable = move_box(moved_list, move, x, y + j - 1)
                if movable == True:
                    map[x][y + j] = "["
                    map[x][y + j + 1] = "]"
                    map[x][y + j + 2] = "."
                    moved_list.append((x, y))
                    return True
                else:
                    return False
            else:
                return False

        if move == ">":
            if map[x][y + j + 1] == ".":
                map[x][y + j] = "["
                map[x][y + j + 1] = "]"
                map[x][y + j - 1] = "."
                moved_list.append((x, y))
                return True
            if map[x][y + j + 1] == "[":
                movable = move_box(moved_list, move, x, y + j + 1)
                if movable == True:
                    map[x][y + j] = "["
                    map[x][y + j + 1] = "]"
                    map[x][y + j - 1] = "."
                    moved_list.append((x, y))
                    return True
                else:
                    return False
            else:
                return False


def try_move(move, x, y):
    moved_list = []
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

    if map[x + i][y + j] == "#":
        return x, y
    if map[x + i][y + j] == ".":
        map[x + i][y + j] = "@"
        map[x][y] = "."
        return x + i, y + j
    if map[x + i][y + j] == "[":
        if move_box(moved_list, move, x + i, y + j) == True:
            map[x + i][y + j] = "@"
            map[x][y] = "."
            return x + i, y + j
        else:
            cancel_moves(moved_list, move)
            return x, y
    if map[x + i][y + j] == "]":
        if move_box(moved_list, move, x + i, y + j - 1) == True:
            map[x + i][y + j] = "@"
            map[x][y] = "."
            return x + i, y + j
        else:
            cancel_moves(moved_list, move)
            return x, y
    else:
        return x, y


for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "@":
            x = i
            y = j


okay = True

for i in range(len(moves)):
    move = moves[i]
    x, y = try_move(move, x, y)

    # Debugging

    # if okay == False:
    #     print_map()
    #     print(move)
    #     print(i)
    #     break

    # count1 = 0
    # count2 = 0
    # count3 = 0
    # for line in map:
    #     for char in line:
    #         if char == "[":
    #             count1 += 1
    #         if char == "]":
    #             count2 += 1
    #         if char == "#":
    #             count3 += 1

    # if count1 != 603 or count2 != 603 or count3 != 858:
    #     print(count1, count2, count3)
    #     print("ERROR")
    #     print_map()
    #     print(move)
    #     print(i)
    #     okay = False

    # if i > 4364:
    #     print(i, move)
    #     print_map()
    # time.sleep(0.01)


def score_p1(map):
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "[":
                sum += 100 * i + j
    return sum


print(score_p1(map))


# Debugging
count1 = 0
count2 = 0
count3 = 0
for line in map:
    for char in line:
        if char == "[":
            count1 += 1
        if char == "]":
            count2 += 1
        if char == "#":
            count3 += 1

print(count1, count2, count3)
