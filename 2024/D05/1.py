import copy
import re

file = open("input", "r")
data = file.readlines()
data = [line.strip() for line in data]

pages_after = [[] for i in range(100)]

i_sep = data.index("")

order = data[:i_sep]
updates = data[i_sep + 1 :]

for line in order:
    pages_after[int(line[:2])].append(int(line[3:]))

good_updates = []

for update in updates:
    good = True
    pages = update.split(",")
    pages = [int(page) for page in pages]
    for i in range(len(pages) - 1):
        for j in range(len(pages) - 1 - i):
            if pages[i] in pages_after[pages[i + j + 1]]:
                good = False
                break
        if good == False:
            break
    if good == True:
        good_updates.append(pages)

sum = 0

for update in good_updates:
    sum += update[len(update) // 2]

sum
