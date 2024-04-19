from sys import argv; 
from csv import reader;
from math import ceil, log;
import array

# This function returns an integer resulting from the value of the "entry" parameter passed by the function "hash" k times.
def hashing(entry, k):
    if k > 0:
        entry = hash(entry) % m
        hashing(entry, k-1)
    return entry

# This returns an Array of a certain size of bits (passed in the bitsize parameter)
def makeBitArray(bitSize):
    # This creates the Array of bits. 'I' is an unsigned 32-bit integer.
    bitArray = array.array('I') 

    # A 0 is added to the Array for every 32 bit integers. If bitSize != (32 * n), a record for stragglers is added.
    bitArray.extend((0,) * ((bitSize >> 5) + 1 if bitSize & 31 else bitSize >> 5))
    return bitArray

# This returns an integer with the bit at 'bitNum' set to 1.
def setBit(arrayName, bitNum):
    arrayName[bitNum >> 5] |= 1 << (bitNum & 31)
    return arrayName[bitNum >> 5]

# This returns a nonzero result, 2**(bit_num & 31), if the bit at 'bitNum' is set to 1.
def testBit(arrayName, bitNum):
    return arrayName[bitNum >> 5] & (1 << (bitNum & 31))

if len(argv) > 1:
    # The first file opening consist in counting the lines in the first input file and storing the value in 'n' variable
    with open(argv[1]) as file: 
        file.readline() # This omits the first row on the file.

        # Number of items in the bloom filter.
        n = sum(1 for row in reader(file))

        # Number of bits in the filter.
        m = ceil((n * log(0.0000001)) / log(1 / 2**log(2)))

        # Number of hash functions.
        k = round((m / n) * log(2))

        # BloomFilter is assigned an Array of bits.
        bloomFilter = makeBitArray(m)

        # The first input file is read from the beginning again in order to give values to the bloom filter.
        file.seek(1)
        for line in reader(file): 
            setBit(bloomFilter, hashing(str(line), k))
    file.close()

    # Finally, the second input file is opened to test its entries against the bloom filter.
    with open(argv[2]) as file: 
        file.readline()
        for line in reader(file): 
            print(line[0] + ',' + ("Probably in the DB" if testBit(bloomFilter, hashing(str(line), k)) else "Not in the DB"))
    file.close()