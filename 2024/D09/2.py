import copy
import re

file = open("test_input.txt", "r")
data = file.readline().strip()
data = [int(char) for char in data]
file.close()

# The ID number is index//2 for a file block

# I don't think it is an efficient idea but i will
# create list of all the code blocks, as in the examples

fs = []
for index, number in enumerate(data):
    if index % 2 == 0:  # file block
        fs += [index // 2] * number
    else:
        fs += [-1] * number


def get_file_size(fs, file):
    file_size = 0
    for i in range(fs.index(file), len(fs)):
        if fs[i] == file:
            file_size += 1
        else:
            break
    return file_size


def get_free_size(fs, i_start):
    free_size = 0
    i_temp = i_start
    while i_temp < len(fs) and fs[i_temp] == -1:
        free_size += 1
        i_temp += 1
    return free_size


file = max(fs)
while file >= 0:
    # print(file)
    i_block = fs.index(file)
    file_size = get_file_size(fs, file)
    i_free = fs.index(-1)
    free_size = get_free_size(fs, i_free)
    while free_size < file_size and i_free + free_size < len(fs) and i_free < i_block:
        try:
            i_free = fs.index(-1, i_free + free_size)
        except:
            break
        free_size = get_free_size(fs, i_free)
    if (
        free_size >= file_size and i_free < i_block
    ):  # The i_free < i_block is important !
        # We've found enough free space
        for i in range(file_size):
            fs[i_free + i] = file
            fs[i_block + i] = -1
    file -= 1


sum = 0
for i in range(len(fs)):
    if fs[i] != -1:
        sum += i * fs[i]
sum
