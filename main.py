from sys import argv
import csv, bloomFilterAlgorithm as bfa

if len(argv) > 1:
    with open(argv[1]) as file:
        # This makes sure that the lines are read as an csv file.
        csvFile = csv.reader(file)

        # This omits the first row on the csv document.
        file.readline()

        for line in csvFile: 
            bfa.input(str(line))
    file.close()

    with open(argv[2]) as file:
        # This makes sure that the lines are read as an csv file.
        csvFile = csv.reader(file)

        # This omits the first row on the csv document.
        file.readline()

        for line in csvFile: 
            print(line[0] + ',' + bfa.output(str(line)))
    file.close()
else:
    print("Invalid input; this only works with two files as inputs on the command line.")