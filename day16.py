import sys
import utils.locationHelpers as lh

print("Day 16 puzzle: Ticket Translation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
rules ={}
my_ticket = []
nearby_tickets = []

with open(puzzle_file, 'r') as puzzle_in:
    # 1 for rules, 2 my ticket, 3 nearby tickets
    data_type = 1
    for cur_line in puzzle_in:
        if cur_line.strip() == "":
            data_type = 0
        if data_type == 1:
            [rname, rrange] = cur_line.strip().split(':')
            rrange = [int(x) for x in rrange[1:].replace(" or ", "-").split('-')]
            rules[rname] = rrange
        elif data_type == 2:
            my_ticket = [int(x) for x in cur_line.strip().split(',')]
        elif data_type == 3:
            nearby_tickets.append([int(x) for x in cur_line.strip().split(',')])
        if cur_line.strip() == "your ticket:":
            data_type = 2
        elif cur_line.strip() == "nearby tickets:":
            data_type = 3

puzzle_in.close()

# print (rules)
# print (my_ticket)
# print (nearby_tickets)

def is_field_compliant(field, crit):
    if (field >= crit[0] and field<=crit[1]) \
        or (field >= crit[2] and field <= crit[3]):
        return True
    else:
        return False

scan_error_rate = 0
for tn in nearby_tickets:
    # check all rules:
    for field in tn:
        valid_rules = 0
        for crit in rules.values():
            if is_field_compliant(field,crit):
                valid_rules += 1
                break
        if valid_rules ==0:
            # print ("value %d in ticket " %field, tn," does not match any rule" )
            scan_error_rate += field
            break

print ("part 1: scanning error rate: %d" %scan_error_rate)