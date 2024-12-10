import copy
import re

file = open("input.txt", "r")
data = file.readline().strip()
data = [int(char) for char in data]

# The ID number is index//2 for a file block

# I don't think it is an efficient idea but i will
# create list of all the code blocks, as in the examples

fs = []
for index, number in enumerate(data):
    if index % 2 == 0:  # file block
        fs += [index // 2] * number
    else:
        fs += [-1] * number


i_free = fs.index(-1)
i_block = len(fs) - 1

while i_free < i_block:
    if fs[i_block] == -1:
        i_block -= 1
    else:  ## we have a block file
        fs[i_free] = fs[i_block]
        fs[i_block] = -1
        i_block -= 1
        i_free = fs.index(-1, i_free)

sum = 0
for i in range(fs.index(-1)):
    sum += i * fs[i]

sum
