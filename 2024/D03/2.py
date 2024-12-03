import copy
import re

file = open('input', 'r')
data = file.readlines()

sum = 0
counting = True

#pattern = r"mul\(([0-9]+),([0-9]+)\)"
pattern = r"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))"
pattern_numbers = r"[0-9]+"

## Cette fois il faut prendre en compte les do() et don't()

for line in data :
    i_start = 0
    found = re.search(pattern,line[i_start:])
    while (found != None) :
            #print(found)
            i_start+= (found.span()[1])
            print(i_start)
            print(line[i_start:])
            content = found.group()
            print(content)
            if content =="do()" :
                  counting = True
            elif content == "don't()" :
                  counting = False
            else :
                numbers = re.findall(pattern_numbers,content)
                #print(numbers)
                if counting==True :
                    sum += int(numbers[0]) * int(numbers[1])
            found = re.search(pattern,line[i_start:])
    
sum

# I could have used re.findall(pattern,line) to find all the multiplications, instead of finding them one by one

