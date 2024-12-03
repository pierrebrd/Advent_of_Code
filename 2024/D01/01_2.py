file = open('input1_1.txt', 'r')
data = file.readlines()

data = [line.split() for line in data]

list1 = [int(data[i][0]) for i in range(len(data))]
list2 = [int(data[i][1]) for i in range(len(data))]

sum = 0

for i in range(len(list1)):
    sum += list1[i] * list2.count(list1[i]) 

sum