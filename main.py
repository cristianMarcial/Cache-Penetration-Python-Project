from sys import argv
from math import log, ceil
import csv

# Number of items in the bloom filter. Its initial value is 0 because the number of lines has not been calculated yet
n = 0 

# Probability of false positives
p = 0.0000001

global m, k
# Number of bits in the filter. Its initial value is 0 because the number of bits in the filter depends of 'n' variable.
m = 0 

# Number of hash functions. The number of hash functions depends of both 'm' and 'n' variables, so its initial value is 0.
k = 0

# This count the number of lines in the first argument given in order to give a number to the variable 'n'.
def countLines(entry):
    global n
    i = 0
    for line in entry:
        i+=1
    n = i

# This function returns an integer resulting from the value of the "entry" parameter passed by the build-in function "hash" k times.
def hashing(entry):
    for i in range(k):
        entry = hash(entry) % m
    return entry

# This function initializes the bloom filter.
def input(entry):
    bloomFilter[hashing(entry)] = 1

# This functions outputs to the command line the original e-mail and the Bloom Filter result.
def output(entry):
    return "Probably in the DB" if (bloomFilter[hashing(entry)] == 1)  else "Not in the DB"

if len(argv) > 1:
    # The first opening consist in opening the first input file, reading it, storing the number of lines in the 'n' 
    # variable and finally giving the variables m, k and bloomFilter a value.
    with open(argv[1]) as file:
        # This makes sure that the lines are read as an csv file.
        csvFile = csv.reader(file)

        # This omits the first row on the csv document.
        file.readline()

        #Then the following four variables are given a value:
        countLines(csvFile) # this assign the 'n' variable value.
        m = ceil((n * log(p)) / log(1 / 2**log(2) ))
        k = round((m / n) * log(2))
        global bloomFilter
        bloomFilter = [0 for i in range(m)]
    file.close()  

    # The first input file is opened again in order to initialize the bloom filter.
    with open(argv[1]) as file:
        csvFile = csv.reader(file)

        file.readline()

        for line in csvFile: 
            input(str(line))
    file.close()

    # Finally, the file 2 is opened to test its entries against the bloom filter.
    with open(argv[2]) as file:
        csvFile = csv.reader(file)
        file.readline()

        for line in csvFile: 
            print(line[0] + ',' + output(str(line)))
    file.close()
else:
    print("Invalid input; this only works with two csv files as inputs on the command line.")