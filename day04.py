import re;
import sys;

print("Day 4 puzzle: High-Entropy Passphrases");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
passphr_cntr = 0;
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        passphrase = [];
        passphrase = cur_line.strip("\n").split();

        found_equal = 0;

        for i in range(len(passphrase)):
            for j in range (i+1, len(passphrase) ):
                if (sorted(list(passphrase[i])) == sorted(list(passphrase[j]))):
                    # we found anagrams, no point to search futher...
                    found_equal = 1;
                    break;

        if (found_equal == 0):
            passphr_cntr += 1;

puzzle_in.close();

print ("Number of valid passphrases: %d" %(passphr_cntr));