import copy
import re

file = open("input.txt", "r")
data = file.readlines()
data = [line.strip() for line in data]

dict = {}
n = len(data)
m = len(data[0])

for i in range(n):
    for j in range(m):
        char = data[i][j]
        if char != ".":
            if char in dict:
                dict[char].append((i, j))
            else:
                dict[char] = [(i, j)]

antinodes = []

for freq in dict:
    antennas = dict[freq]  # Not really pretty
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            # We have two antinodes to check
            a1 = antennas[i]
            a2 = antennas[j]
            x = a1[0] + (a1[0] - a2[0])
            y = a1[1] + (a1[1] - a2[1])
            if 0 <= x < n and 0 <= y < m:
                if (x, y) not in antinodes:
                    antinodes.append((x, y))
            x = a2[0] - (a1[0] - a2[0])
            y = a2[1] - (a1[1] - a2[1])
            if 0 <= x < n and 0 <= y < m:
                if (x, y) not in antinodes:
                    antinodes.append((x, y))

sum = len(antinodes)
sum


# We'll create a dict containing all the positions of antennas for each frequency.
# Then, we'll go through this dict to create the list of all unique antinode positions
