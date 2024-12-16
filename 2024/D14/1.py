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


for i in range(len(data)):
    x, y, vx, vy = data[i]
    for j in range(100):
        x, y = iteration(x, y, vx, vy)
    data[i] = [x, y, vx, vy]


# Now we count the robots in each quadrant
quadrants = [0, 0, 0, 0]

for robot in data:
    x, y = robot[0], robot[1]
    if x < width // 2:
        if y < height // 2:
            quadrants[0] += 1
        elif y > height // 2:
            quadrants[2] += 1
    elif x > width // 2:
        if y < height // 2:
            quadrants[1] += 1
        elif y > height // 2:
            quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
