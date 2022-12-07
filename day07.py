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
            print ("No more commands to process")
            return start_offset
    return cmd_offset

pwd = "/"
filesystem = {'/':[]}
line_num = -1
file_pat = re.compile(r'^([0-9]+)\s(.*)$')

# process input data and create directory tree
while line_num < len(listing):
    next_offset = find_next_cmd_offset (line_num,listing)
    # there are still commands to process on the list
    if next_offset > line_num:
        cmd = listing[next_offset]
        if "cd" in cmd:
            if '..' in cmd:
                # strip the current directory from the path
                pwd = pwd [:pwd.rindex('/',0,-2)+1]
            elif '/' in cmd:
                pwd = '/'
            else:
                # add the directory to current working path
                pwd += cmd[5:]+'/'
                if pwd not in filesystem.keys():
                    filesystem[pwd]=[]
            line_num = next_offset
        elif "ls" in cmd:
            line_num = next_offset
            next_offset = find_next_cmd_offset(line_num,listing)
            if next_offset==line_num:
                # ls was the last command, we just need to read the output
                next_offset=len(listing)
            for line in listing[line_num+1:next_offset]:
                # fill info about parent dir
                if line not in filesystem[pwd]:
                    filesystem[pwd].append(line)
    else:
        print ("This was the last command, there is nothing more we can do for you")
        break

def get_size(path,content):
    # sample listing for the path
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
du = {}
for f in sorted(filesystem.keys()):
    s=get_size(f,filesystem[f])
    if s<=limit:
        total+=s
    else:
        du [f] = s

print("Part 1: sum of directories of size at most {} is {}".format(limit,total))

total_space = 70000000
required_space = 30000000
free_space = total_space - du['/']
lack_of_space = required_space-free_space
print ("Available space is {} need to free {}".format(free_space,lack_of_space))

to_delete=[]
for d in du.keys():
    if du[d] >=lack_of_space:
        to_delete.append(du[d])

print ("Part 2: smallest dir to delete is: {}".format(min(to_delete)))


