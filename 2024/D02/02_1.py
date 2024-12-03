import copy

file = open('input02_1.txt', 'r')
data = file.readlines()

data = [line.split() for line in data]
for i in range(len(data)):
    data[i] = [int(data[i][j]) for j in range(len(data[i]))]

data_sort= copy.deepcopy(data)
data_rsort = copy.deepcopy(data)
for i in range(len(data)) :
    data_sort[i].sort()
    data_rsort[i].sort(reverse=True)

sum = 0 
for i in range(len(data)) :
    if (data[i] == data_sort[i] or data[i] == data_rsort[i]) :
        okay = 1
        for j in range(len(data[i])-1) :
            if not ( 0 < abs(data[i][j] - data[i][j+1]) < 4) :
                okay = 0
                break
        if okay == 1 :
            sum += 1

sum