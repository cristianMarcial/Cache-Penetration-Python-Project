from sys import argv
import csv

if len(argv) > 1:
    with open(argv[1]) as file:
        # This makes sure that the lines are read as an csv file.
        csvFile = csv.reader(file)

        # This omits the first row on the csv document.
        file.readline()

        for lines in csvFile: 
            print(lines)
        file.close()
else:
    print("Invalid input; this only works with more than 3 inputs on the command line.")