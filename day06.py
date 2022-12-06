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

# convert to single string
data_stream = ''.join(data_stream)


def is_char_uniq_in_chunk (char, chunk):
    return not chunk.count(char)>1

def find_first_uniq_set (stream, chunk_len):
    char_offset = 0
    uniq_chars = 0

    for char_offset in range(len(stream)):

        while uniq_chars < chunk_len:
            char = data_stream[char_offset+uniq_chars]
            if is_char_uniq_in_chunk(char,data_stream[char_offset:char_offset+chunk_len]):
            # Found uniq char, examine next entry
                uniq_chars += 1
            else:
                # Found duplicate, restarting
                uniq_chars = 0
                break
        if uniq_chars == chunk_len:
            # set complete
            break
    return char_offset + chunk_len

start_of_packet = find_first_uniq_set (data_stream,4)

print ("Part 1: the first start-of-packet marker is after {} character".format(start_of_packet))

start_of_message = find_first_uniq_set (data_stream,14)

print ("Part 2: the first start-of-message marker is after {} character".format(start_of_message))
