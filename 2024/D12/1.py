import copy
import re

file = open("input.txt", "r")
map = [[char for char in line.strip()] for line in file.readlines()]

# We will find the regions, and then the perimeter
# The perimeter can be calculated for each plot, without knowing the region

regions = []
visited_plots = set()

# Let's create the regions list

n = len(map)
m = len(map[0])


def add_to_region(i, j, k, l):
    for region in regions:
        if (i, j) in region:
            region.append((k, l))
            return


def explore_around(i, j):
    char = map[i][j]
    if i > 0 and char == map[i - 1][j] and (i - 1, j) not in visited_plots:
        add_to_region(i, j, i - 1, j)
        visited_plots.add((i - 1, j))
        explore_around(i - 1, j)
    if i < n - 1 and char == map[i + 1][j] and (i + 1, j) not in visited_plots:
        add_to_region(i, j, i + 1, j)
        visited_plots.add((i + 1, j))
        explore_around(i + 1, j)
    if j > 0 and char == map[i][j - 1] and (i, j - 1) not in visited_plots:
        add_to_region(i, j, i, j - 1)
        visited_plots.add((i, j - 1))
        explore_around(i, j - 1)
    if j < m - 1 and char == map[i][j + 1] and (i, j + 1) not in visited_plots:
        add_to_region(i, j, i, j + 1)
        visited_plots.add((i, j + 1))
        explore_around(i, j + 1)


for i in range(n):
    for j in range(m):
        if (i, j) not in visited_plots:
            visited_plots.add((i, j))
            regions.append([(i, j)])
            explore_around(i, j)

sum = 0
for region in regions:
    perimeter = 0
    for i, j in region:
        char = map[i][j]
        if not i > 0 or char != map[i - 1][j]:
            perimeter += 1
        if not i < n - 1 or char != map[i + 1][j]:
            perimeter += 1
        if not j > 0 or char != map[i][j - 1]:
            perimeter += 1
        if not j < m - 1 or char != map[i][j + 1]:
            perimeter += 1
    sum += perimeter * len(region)

sum
