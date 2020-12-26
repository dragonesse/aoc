import sys
import utils.inputReaders as ir
print("Day 14: Docking Data");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

program = ir.read_oneline_records_as_list_entries(puzzle_file)

memory ={}
mask = ''
def extract_bits_to_replace(mask):
    offset =0
    bits = []
    while offset < 36:
        pos = mask.find('0',offset)
        if pos  != -1:
            bits.append ([pos,'0'])
            offset = pos + 1
        else:
            break
    offset =0
    while offset < 36:
        pos = mask.find('1',offset)
        if pos  != -1:
            bits.append ([pos,'1'])
            offset = pos + 1
        else:
            break
    return bits

def update_val_by_bitmask (value, bits2replace):
    bin_string_val = list(format(value, '036b'))
    for repl in bits2replace:
        bin_string_val[repl[0]]=repl[1]
    return int(''.join(bin_string_val),2)


for command in program  :
    print ("processing command: %s" %command )
    if command.startswith("mask"):
        mask = command.split(' ')[2]
        edit_list = extract_bits_to_replace (mask )
    else:
        mem_ind = int(command.split('[')[1].split(']')[0])
        mem_val_dec = int(command.split(' ')[2])
        print (mask)
        print (format(mem_val_dec, '036b'))

        memory [mem_ind] = update_val_by_bitmask(mem_val_dec,edit_list)
        print (format(memory[mem_ind],'036b'))

mem_sum =0
for m in memory.keys():
    mem_sum += memory  [m]

print  ("part 1: sum of memory cells is: %d" %mem_sum   )

