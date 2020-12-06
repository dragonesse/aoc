import sys
import utils.inputReaders as ir

print("Day 6 puzzle: Custom Customs");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

customs_forms = ir.read_multiline_records_as_list_entries(puzzle_file)

def anonimize_group_data (group_data):
    return list(''.join(forms))

def get_uniq_answers (anonymous_data):
    return list(dict.fromkeys(anonymous_data))

num_yes = 0
num_yes2 = 0
for forms in customs_forms:
    anonymous_data = anonimize_group_data(forms)
    uniq_answers = get_uniq_answers (anonymous_data)
    num_yes += len (uniq_answers)
    for answer in uniq_answers:
        if anonymous_data.count(answer) == len (forms):
            num_yes2 += 1

print ("answers in groups #1 %d" %(num_yes))
print ("answers in groups #2 %d" %(num_yes2))
