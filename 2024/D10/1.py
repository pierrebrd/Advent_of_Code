import copy
import re

file = open("input.txt", "r")
data = file.readlines()

map = [[int(char) for char in row.strip()] for row in data]

n = len(map)
m = len(map[0])

zero_indexes = []

for row_index, row in enumerate(map):
    for col_index, number in enumerate(row):
        if number == 0:
            zero_indexes.append((row_index, col_index))

# I used DFS instead of BFS.
# BFS can be implemented with a queue and a loop where you dequeue while queue is not empty


def explore_around(map, current_height, current_x, current_y, nine_indexes):
    if current_height == 9:
        if (current_x, current_y) not in nine_indexes:
            nine_indexes.append((current_x, current_y))
    else:
        if current_x + 1 < n and map[current_x + 1][current_y] == current_height + 1:
            explore_around(
                map, current_height + 1, current_x + 1, current_y, nine_indexes
            )
        if current_x - 1 >= 0 and map[current_x - 1][current_y] == current_height + 1:
            explore_around(
                map, current_height + 1, current_x - 1, current_y, nine_indexes
            )
        if current_y + 1 < m and map[current_x][current_y + 1] == current_height + 1:
            explore_around(
                map, current_height + 1, current_x, current_y + 1, nine_indexes
            )
        if current_y - 1 >= 0 and map[current_x][current_y - 1] == current_height + 1:
            explore_around(
                map, current_height + 1, current_x, current_y - 1, nine_indexes
            )


sum = 0

for x, y in zero_indexes:
    nine_indexes = []
    explore_around(map, 0, x, y, nine_indexes)
    sum += len(nine_indexes)
sum
