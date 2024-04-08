from sys import argv; from math import ceil, log; import csv
with open(argv[1]) as file: 
    file.readline()
    n = sum(1 for row in csv.reader(file)) 
    m = ceil((n * log(0.0000001)) / log(1 / 2**log(2))) 
    bF = [False for i in range(m)]
    file.seek(1)
    for line in csv.reader(file): bF[hash(str(line)) % m] = True
file.close()
with open(argv[2]) as file:
    file.readline()
    for l in csv.reader(file): print(l[0] + ',' + ("Probably in the DB" if (bF[hash(str(l)) % m] == True) else "Not in the DB"))
file.close()