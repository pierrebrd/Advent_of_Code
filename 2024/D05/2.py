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

bad_updates = []


for update in updates:
    good = True
    pages = update.split(",")
    pages = [int(page) for page in pages]
    for i in range(len(pages) - 1):
        for j in range(len(pages) - 1 - i):
            if pages[i] in pages_after[pages[i + j + 1]]:
                good = False
                bad_updates.append(pages)
                break
        if good == False:
            break

sum = 0

for update in bad_updates:
    # On va faire un truc moche
    for i in range(len(update)):
        for j in range(i, len(update)):
            # On parcours les pages pas encore triées
            good_page = True
            for k in range(i, len(update)):
                if k != j:
                    if update[j] in pages_after[update[k]]:
                        good_page = False
                        break
            if good_page == True:
                # la page est une bonne candidate pour ette la suivante dans le bon ordre
                other_updates = []
                for k in range(i, len(update)):
                    if j != k:
                        other_updates.append(update[k])
                update = update[:i] + [update[j]] + other_updates
                break

    sum += update[len(update) // 2]

sum
