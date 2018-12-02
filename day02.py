import sys;
from collections import Counter

print("Day 2 puzzle: Inventory Management System");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
box_ids = []

with open(puzzle_file, 'r') as puzzle_in:
    box_ids = [cur_line.strip("\n") for cur_line in puzzle_in]
puzzle_in.close()

# search the repetitions
total_dupes = 0
total_triples = 0
# examine each box
for box_num in box_ids:
    tag_summary = Counter(box_num)
    if 2 in tag_summary.values():
        total_dupes += 1
    if 3 in tag_summary.values():
        total_triples += 1

# examine tags' similarity
chars_evidence = {}
for box_tag in box_ids:

    #now we have a list without element taken to comparison
    for box_to_check in box_ids:
        common_chars = ""
        diff_cntr = 0
        for pos in range (len(box_tag)):
            if box_tag[pos] == box_to_check[pos]:
                common_chars = common_chars + box_tag[pos]
            else:
                diff_cntr += 1
                if diff_cntr > 1:
                    # no point to do more checks
                    break

        if diff_cntr == 1:
            if common_chars not in chars_evidence:
                chars_evidence[common_chars] = 1
            else:
                chars_evidence[common_chars] = chars_evidence[common_chars] + 1

print ("The checksum is: %d" %(total_triples*total_dupes))
print ("The most popular sequence is: ", Counter(chars_evidence).most_common(5))