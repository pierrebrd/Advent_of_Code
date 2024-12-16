import copy
import re
import math as m

with open("input.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    matches = re.findall(r"-?\d+", data[i])
    data[i] = [int(number) for number in matches]

# width = 11
# height = 7
width = 101
height = 103


def iteration(x, y, vx, vy):
    x1 = (x + vx) % width
    y1 = (y + vy) % height
    return x1, y1


def get_map(data):
    map = [[0 for i in range(width)] for j in range(height)]
    for robot in data:
        x, y = robot[0], robot[1]
        map[y][x] += 1
    return map


def get_linicity(map):
    linicity = 0
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            if map[i][j] > 0:
                if map[i - 1][j] > 0:
                    linicity += 1
                if map[i + 1][j] > 0:
                    linicity += 1
                if map[i][j - 1] > 0:
                    linicity += 1
                if map[i][j + 1] > 0:
                    linicity += 1
    return linicity


def print_map(data):
    map = [[0 for i in range(width)] for j in range(height)]
    for robot in data:
        x, y = robot[0], robot[1]
        map[y][x] += 1
    for line in map:
        string = ""
        for char in line:
            if char == 0:
                string += " "
            else:
                string += "#"
        print(string)


max_linicity = 0

for j in range(100000000):
    for i in range(len(data)):
        x, y, vx, vy = data[i]
        x, y = iteration(x, y, vx, vy)
        data[i] = [x, y, vx, vy]
    map = get_map(data)
    linicity = get_linicity(map)
    if linicity > max_linicity:
        max_linicity = linicity
        print_map(data)
        print(linicity)
        print(j + 1)
