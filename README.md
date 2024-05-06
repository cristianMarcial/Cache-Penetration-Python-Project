About
=====

This program was created as a project at college, and its functionality is to create a Bloom Filter based on multiple hashes.
The Bloom Filter is created dynamically based on dummy inputs (for example, emails) from a csv file that is evaluated at run time. It has a false positive probability of 0.0000001.
You can understand the equations involved at https://hur.st/bloomfilter/.

Functionality
=====

The program takes 2 files as inputs.

Example: python main.py input.csv check.csv

The input comma-separated files will contain one column: Email. Based on the email key, the program builds the Bloom Filter based on file 1 inputs.
Then it checks file 2 entries against the bloom filter and provide its assessment.

Finally, the program outputs to the command line the original e-mail and the Bloom Filter result in the following format:

myemail32414334@aol.com,Probably in the DB

dlaskjfdla@hotmail.com,Not in the DB

xdlmao,Not in the DB
