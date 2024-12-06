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

x_init = x
y_init = y

sum = 0

for i in range(len(map)):
    print(i)
    for j in range(len(map[0])):
        if map[i][j] == ".":
            # la case est vide, on regarde si on peut ajouter une obstruction valable
            map[i][j] = "#"
            iter = 0
            dir = 1
            x = x_init
            y = y_init
            trapped = True
            while iter < 100000:
                # oui c'est moche
                iter += 1
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
                    trapped = False
                    break  # On est sorti de la carte
                else:
                    if map[x1][y1] == "#":
                        # obstacle
                        dir = turn(dir)
                    else:
                        x = x1
                        y = y1
                        # map[x][y] = "X"
            map[i][j] = "."
            if trapped == True:
                sum += 1

sum
