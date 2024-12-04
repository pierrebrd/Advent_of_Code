import copy
import re

file = open('input', 'r')
data = file.readlines()
data = [line.strip() for line in data]

pattern=r"(?=(XMAS)|(SAMX))"

sum = 0

data_reverse = ["" for i in range(len(data[0]))]
for i in range(len(data)) :
    for j in range(len(data[0])) :
        data_reverse[j] += data[i][j]
    

def diag(data) :
    ni = len(data)
    nj = len(data[0])
    #Nombre de diagonales : nj + ni -1
    result = ['' for l in range(ni+nj-1)]
    # On remplit les nj-1 premières lignes
    for i in range(ni-1):
        #Pour chaque ligne, on parcout la diagonale jusqu'à ce qu'on arrive en bas ou à droite de data
        for j in range(nj) : #Maximum nj charactères avant d'arriver à la droite de data
            if i+1+j<ni : result[i] += data[i+1+j][j]
    # On remplit les nj autres lignes (diagonales dont les premiers charactères sont ceux de la première ligne de data)
    for i in range(nj):
        #Pour chaque ligne, on parcout la diagonale jusqu'à ce qu'on arrive en bas ou à droite de data
        for j in range(nj) :# idem, maximum nj caractères
            if i+j<nj : result[ni-1+i] += data[j][i+j]
    return result

def diag_reverse(data) :
    ni = len(data)
    nj = len(data[0])
    #Nombre de diagonales : nj + ni -1
    result = ['' for l in range(ni+nj-1)]
    # On remplit les nj-1 premières lignes
    for i in range(ni-1):
        #Pour chaque ligne, on parcout la diagonale jusqu'à ce qu'on arrive en bas ou à gauche de data
        for j in range(nj) : #Maximum nj charactères avant d'arriver à gauche de data
            if i+1+j<ni and j<ni : result[i] += data[i+1+j][nj-1-j]
    # On remplit les nj autres lignes (diagonales dont les premiers charactères sont ceux de la première ligne de data)
    for i in range(nj):
        #Pour chaque ligne, on parcout la diagonale jusqu'à ce qu'on arrive en bas ou à droite de data
        for j in range(nj) :# idem, maximum nj caractères
            if -i+nj-1-j>=0 and j<ni :result[ni-1+i] += data[j][-i+nj-1-j]
    return result

# J'aurais pu utiliser des try except pour ne pas avoir à me soucier des IndexErrors.
# Une autre solution est de rajouter du padding


data_diag = diag(data)
data_diag_reverse =  diag_reverse(data)



for line in data :
    sum+= len(re.findall(pattern,line))

for line in data_reverse :
    sum+= len(re.findall(pattern,line))

for line in data_diag :
    sum+= len(re.findall(pattern,line))

for line in data_diag_reverse :
    sum+= len(re.findall(pattern,line))

sum

# J'ai perdu pas mal de temps à faire les fonctions qui calculent la liste des diagonales, 
# il aurait probablement été plus simple de "hardcoder", en recherchant les X puis les MAS autour,
# avec pleins de for et de if.

# Qui sait, peut-être qu'un jour j'aurai besoin d'une fonction qui liste les diagonales ! 

