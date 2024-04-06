from sys import argv; from math import ceil, log; import csv

# This function returns an integer resulting from the value of the "entry" parameter passed by the function "hash" k times.
def hashing(entry):
    for i in range(k): entry = hash(entry) % m
    return entry

if len(argv) > 1:
    # The first file opening consist in counting the lines in the first input and storing the value in 'n' variable
    with open(argv[1]) as file: 
        file.readline() # This omits the first row on the file

        # Number of items in the bloom filter.
        n = sum(1 for row in csv.reader(file)) 

        # Number of bits in the filter.
        m = ceil((n * log(0.0000001)) / log(1 / 2**log(2))) 

        # Number of hash functions.
        k = round((m / n) * log(2)) 

        bloomFilter = [False for i in range(m)]

        # The first input file is read from the beginning again in order to give the bloom filter values.
        file.seek(1)
        for line in csv.reader(file): 
            bloomFilter[hashing(str(line))] = True
    file.close()

    # Finally, the second file is opened to test its entries against the bloom filter.
    with open(argv[2]) as file: 
        file.readline()
        for line in csv.reader(file): 
            print(line[0] + ',' + ("Probably in the DB" if (bloomFilter[hashing(str(line))] == True) else "Not in the DB"))
    file.close()