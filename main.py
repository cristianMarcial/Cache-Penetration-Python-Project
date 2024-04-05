from sys import argv
from math import ceil, log
import csv

# Probability of false positives
p = 0.0000001

# This function returns an integer resulting from the value of the "entry" parameter passed by the build-in function "hash" k times.
def hashing(entry):
    for i in range(k):
        entry = hash(entry) % m
    return entry

if len(argv) > 1:

    """The first file opening consist in opening the first input file, reading it, storing the number of lines in the 'n' 
    variable and finally giving the variables m, k and bloomFilter a value."""
    with open(argv[1]) as file:
        # This makes sure that the input is read as an csv file.
        csvFile = csv.reader(file)

        # This omits the first row on the file.
        file.readline()

        #Then the following four variables are initialized:
        global n, m, k, bloomFilter

        # This count the number of lines in the first argument given in order to give a number to the variable 'n'.
        n = 0 # Number of items in the bloom filter.
        for line in csvFile:
            n+=1

        # Number of bits in the filter.
        m = ceil((n * log(p)) / log(1 / 2**log(2) ))

        # Number of hash functions.
        k = round((m / n) * log(2))

        bloomFilter = [False for i in range(m)]
    file.close()

    """ The first input file is opened again in order to initialize the bloom filter. """
    with open(argv[1]) as file:
        csvFile = csv.reader(file)
        file.readline()

        # This gives the bloom filter a value.
        for line in csvFile:
            bloomFilter[hashing(str(line))] = True
    file.close()

    """ Finally, the second file is opened to test its entries against the bloom filter. """
    with open(argv[2]) as file:
        csvFile = csv.reader(file)
        file.readline()

        # This outputs to the command line the original e-mail and the bloom filter result.
        for line in csvFile: 
            print(line[0] + ',' + ("Probably in the DB" if (bloomFilter[hashing(str(line))] == True) else "Not in the DB"))
    file.close()
else:
    print("Invalid input; this only works with two csv files as inputs on the command line.")