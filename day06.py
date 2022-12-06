import sys;
import utils.inputReaders as ir

print("Day 6: Tuning Trouble");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
data_stream = ir.read_oneline_records_as_list_entries(puzzle_file)

char_offset = 0
uniq_chars = 0
print (data_stream[0])

def is_char_uniq_in_chunk (char, chunk):
    if chunk.count(char)>1:
        print ("\'{}\' repeats in {}".format(char,chunk))
        return False
    else:
        print ("\'{}\' is unique in {}".format(char,chunk))
        return True

# convert to single string
data_stream = ''.join(data_stream)

for char_offset in range(len(data_stream)):

    while uniq_chars < 4:
        char = data_stream[char_offset+uniq_chars]
        print ("Processing \'{}\' offset {}".format (char,char_offset+uniq_chars))
        if is_char_uniq_in_chunk(char,data_stream[char_offset:char_offset+4]):
            print ("Found uniq char, examine next entry")
            uniq_chars += 1
        else:
            print ("Found duplicate, restarting")
            uniq_chars = 0
            break
    if uniq_chars == 4:
        break

print ("Part 1: the first start-of-packet marker is after {} character".format(char_offset+4))
