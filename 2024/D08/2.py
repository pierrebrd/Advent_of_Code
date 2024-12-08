import copy
import re


file = open("test_input.txt", "r")
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

from math import gcd

for freq in dict:
    antennas = dict[freq]  # Not really pretty
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            # We have two antinodes to check
            a1 = antennas[i]
            a2 = antennas[j]
            dist_x = a1[0] - a2[0]
            dist_y = a1[1] - a2[1]
            # We don't need the distance but rather the minimal "offsets" to stay on the same line
            pgcd = gcd(dist_x, dist_y)
            dist_x = dist_x // pgcd
            dist_y = dist_y // pgcd

            # We will start from the first antenna, and add the distance until we go off the map.
            # Then, we star again in the other direction
            x = a1[0]
            y = a1[1]
            while 0 <= x < n and 0 <= y < m:
                if (x, y) not in antinodes:
                    antinodes.append((x, y))
                x += dist_x
                y += dist_y
            x = a1[0] - dist_x
            y = a1[1] - dist_y
            while 0 <= x < n and 0 <= y < m:
                if (x, y) not in antinodes:
                    antinodes.append((x, y))
                x -= dist_x
                y -= dist_y

sum = len(antinodes)
sum


# We'll create a dict containing all the positions of antennas for each frequency.
# Then, we'll go through this dict to create the list of all unique antinode positions