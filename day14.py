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

def extract_bits_with_val (mask, val):
    offset =0
    bits = []
    while offset < 36:
        pos = mask.find(val,offset)
        if pos  != -1:
            bits.append (pos)
            offset = pos + 1
        else:
            break
    return bits

def extract_floating_bits(mask):
    return extract_bits_with_val (mask, 'X')


def update_val_by_bitmask (value, bits2replace):
    bin_string_val = list(format(value, '036b'))
    for repl in bits2replace:
        bin_string_val[repl[0]]=repl[1]
    return int(''.join(bin_string_val),2)


for command in program  :
    if command.startswith("mask"):
        mask = command.split(' ')[2]
        edit_list = extract_bits_to_replace (mask )
    else:
        mem_ind = int(command.split('[')[1].split(']')[0])
        mem_val_dec = int(command.split(' ')[2])

        memory [mem_ind] = update_val_by_bitmask(mem_val_dec,edit_list)

mem_sum =0
for m in memory.keys():
    mem_sum += memory  [m]

print  ("part 1: sum of memory cells is: %d" %mem_sum )

def update_val_by_bitmask_rule2 (value, bits2replace):
    bin_string_val = list(format(value, '036b'))
    for repl in bits2replace:
        bin_string_val[repl]= '1'
    return int(''.join(bin_string_val),2)

def extract_mask_from_base(value, bits2ignore):
    bin_string_val = list(format(value, '036b'))
    for ign_ind in bits2ignore:
        bin_string_val[ign_ind]= '0'
    return ''.join(bin_string_val)

def calculate_base_wo_mask (value, bits2ignore ):
    bin_string_val = extract_mask_from_base(value,bits2ignore)
    base_val = int(bin_string_val,2)
    return  base_val

def generate_addr_at_float_ind (base_addr, float_mask_ind):
    return [base_addr +2**(35-float_mask_ind) ,base_addr ]

def generate_heap (base_addr_list, float_mask_list ):
    res =[]
    fi = float_mask_list.pop(0)

    for ba in base_addr_list:
        res+=generate_addr_at_float_ind (ba, fi)

    if len(float_mask_list ) > 0:
        return generate_heap (res, float_mask_list)
    return res

memory = {}
for command in program  :
    if command.startswith("mask"):
        mask = command.split(' ')[2]
        edit_list = extract_bits_with_val (mask,'1' )
    else:
        float_list = extract_floating_bits(mask)

        mem_ind = int(command.split('[')[1].split(']')[0])
        mem_val_dec = int(command.split(' ')[2])

        mem_addr_upd = update_val_by_bitmask_rule2(mem_ind,edit_list)
        mem_addr_base = calculate_base_wo_mask (mem_addr_upd,float_list)

        heap = generate_heap ([mem_addr_base], float_list)
        for h in heap :
            memory [h] = mem_val_dec

mem_sum =0
for m in memory.keys():
    mem_sum += memory  [m]

print  ("part 2: sum of memory cells is: %d" %mem_sum)