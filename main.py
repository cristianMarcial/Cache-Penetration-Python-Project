import csv, sys, math

# This function returns an integer resulting from the value of the "entry" parameter passed by the function "hash" k times.
def hashing(entry):
    for i in range(k): entry = hash(entry) % m
    return entry

if len(sys.argv) > 1:
    with open(sys.argv[1]) as file: # The first file opening consist in counting the first input lines and storing the value in 'n' variable
        file.readline() # This omits the first row on the file.

        global n, m, k, bloomFilter #This four variables are initialized below:
        n = 0 # Number of items in the bloom filter.
        for line in csv.reader(file): n+=1 # This count the number of lines in the first argument given in order to give a number to the variable 'n'.
        m = math.ceil((n * math.log(0.0000001)) / math.log(1 / 2**math.log(2))) # Number of bits in the filter.
        k = round((m / n) * math.log(2)) # Number of hash functions.
        bloomFilter = [False for i in range(m)]

        file.seek(1) # The first input file is opened again in order to initialize the bloom filter.
        for line in csv.reader(file): bloomFilter[hashing(str(line))] = True # This gives the bloom filter a value.
    file.close()

    with open(sys.argv[2]) as file: # Finally, the second file is opened to test its entries against the bloom filter.
        file.readline()
        for line in csv.reader(file): print(line[0] + ',' + ("Probably in the DB" if (bloomFilter[hashing(str(line))] == True) else "Not in the DB"))
    file.close()