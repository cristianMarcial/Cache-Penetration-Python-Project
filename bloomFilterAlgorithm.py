from math import log, ceil

PROBABILITY_OF_FALSE_POSITIVES = 0.0000001

nl = 0
def countLines(entry):
    global nl
    for line in entry:
        nl+=1

n = 4000
p = 0.0000001
m = ceil((n * log(p)) / log(1 / 2**log(2) ))
NUMBER_OF_HASH_FUNCTION = 40 #round((m / n) * log(2))
k = round((m / n) * log(2))

bloomFilter = [0 for i in range(NUMBER_OF_HASH_FUNCTION)]

def input(entry):
    bloomFilter[hash(entry) % NUMBER_OF_HASH_FUNCTION] = 1

def output(entry):
    return "Probably in the DB" if (bloomFilter[hash(entry) % NUMBER_OF_HASH_FUNCTION] == 1)  else "Not in the DB"