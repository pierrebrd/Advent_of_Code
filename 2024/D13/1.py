import copy
import re

file = open("input.txt", "r")

data = file.read().split("\n\n")

machines = []

for i in range(len(data)):
    machines.append([int(number) for number in re.findall(r"([0-9]+)", data[i])])

# We now have a list of all the machines and their parameters

sum = 0

for machine in machines:
    # We will check if we can have the prize
    x_a, y_a, x_b, y_b, x_p, y_p = machine
    min_cost = 1000
    max_a = min(x_p // x_a + 1, y_p // y_a + 1, 100)
    max_b = min(x_p // x_b + 1, y_p // y_b + 1, 100)
    for n_a in range(max_a + 1):
        for n_b in range(max_b + 1):
            x = n_a * x_a + n_b * x_b
            y = n_a * y_a + n_b * y_b
            if x > x_p or y > y_p:
                break
            if x == x_p and y == y_p:
                cost = 3 * n_a + n_b
                if cost < min_cost:
                    min_cost = cost
    if min_cost < 1000:
        sum += min_cost

sum
