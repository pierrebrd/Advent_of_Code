import copy
import re

file = open('input', 'r')
data = file.readlines()

sum = 0

pattern = r"mul\(([0-9]+),([0-9]+)\)"
pattern_numbers = r"[0-9]+"

for line in data :
    i_start = 0
    found = re.search(pattern,line[i_start:])
    while (found != None) :
            print(found)
            i_start+= (found.span()[1])
            print(i_start)
            print(line[i_start:])
            multiplication = found.group()
            numbers = re.findall(pattern_numbers,multiplication)
            print(numbers)
            sum += int(numbers[0]) * int(numbers[1])
            found = re.search(pattern,line[i_start:])
    
sum

# I could have used re.findall(pattern,line) to find all the multiplications, instead of finding them one by one

