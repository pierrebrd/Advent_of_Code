import copy

file = open('input02_1.txt', 'r')
data = file.readlines()

data = [line.split() for line in data]
for i in range(len(data)):
    data[i] = [int(data[i][j]) for j in range(len(data[i]))]


sum = 0 
for i in range(len(data)) :
    for j in range(len(data[i])):
        # On va enlever un repport au fur et a mesure
        line_full=copy.deepcopy(data[i])
        line = line_full[:j] + line_full[j+1:]
        line_sort = copy.deepcopy(line)
        line_rsort = copy.deepcopy(line)
        line_sort.sort()
        line_rsort.sort(reverse=True)
        if (line == line_sort or line == line_rsort) :
            okay = 1
            for k in range(len(line)-1) :
                if not ( 0 < abs(line[k] - line[k+1]) < 4) :
                    okay = 0
            if okay == 1 :
                sum += 1
                break

sum

# C'est très moche mais ça a le mérite de fonctionner
# On aurait pu utiliser np.diff() 