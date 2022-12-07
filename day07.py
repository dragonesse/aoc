import sys
import utils.inputReaders as ir
import re

print("Day 7: No Space Left On Device");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
listing = ir.read_oneline_records_as_list_entries(puzzle_file)


def find_next_cmd_offset(start_offset, listing):
    cmd_offset = start_offset + 1
    while not listing[cmd_offset].startswith('$'):
        cmd_offset+=1
        if cmd_offset >= len(listing):
            print ("no more commands to process")
            return start_offset
    return cmd_offset

pwd = "/"
filesystem = {'/':[]}
line_num = -1
dir_patt = re.compile(r'^dir\s(.*)$')
file_pat = re.compile(r'^([0-9]+)\s(.*)$')

while line_num < len(listing):
    next_offset = find_next_cmd_offset (line_num,listing)
    if next_offset > line_num:
        cmd = listing[next_offset]
        print ("Executing: {}".format(cmd))
        if "cd" in cmd:
            if '..' in cmd:
                pwd = pwd [:pwd.rindex('/',0,-2)+1]
            elif '/' in cmd:
                pwd = '/'
            else:
                pwd += cmd[5:]+'/'
                if pwd not in filesystem.keys():
                    filesystem[pwd]=[]
            print(pwd)
            line_num = next_offset
        elif "ls" in cmd:
            line_num = next_offset
            next_offset = find_next_cmd_offset(line_num,listing)
            if next_offset==line_num:
                next_offset=len(listing)
            for line in listing[line_num+1:next_offset]:
                print (line)
                if line not in filesystem[pwd]:
                    filesystem[pwd].append(line)
    else:
        print ("There is nothing more we can do for you")
        break

def get_size(path,content):
    #['dir e', '29116 f', '2557 g', '62596 h.lst']
    size = 0
    for item in content:
        if not item.startswith('dir'):
            size += int(re.match(file_pat,item).groups()[0])
        else:
            path_to_sum = path + item[4:] + '/'
            size += get_size(path_to_sum,filesystem[path_to_sum])
    return size

limit = 100000
total = 0
for f in sorted(filesystem.keys()):
    #print ("{}:{}".format(f,filesystem[f]))
    s=get_size(f,filesystem[f])
    print("{}:\t{}".format(f,s))
    if s<=limit:
        total+=s

#s = get_size('/a/',['dir e', '29116 f', '2557 g', '62596 h.lst'])
print("Part 1: sum of directories at most {} is {}".format(limit,total))
