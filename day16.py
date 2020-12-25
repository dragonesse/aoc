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

def is_field_compliant(field, crit):
    if (field >= crit[0] and field<=crit[1]) \
        or (field >= crit[2] and field <= crit[3]):
        return True
    else:
        return False

scan_error_rate = 0
valid_tickets = []
for tn in nearby_tickets:
    # check all rules:
    valid_rules = 0
    for field in tn:
        has_valid_rule = False

        for crit in rules.values():
            if is_field_compliant(field,crit):
                has_valid_rule = True
                valid_rules +=1
                break
        if not has_valid_rule:
            scan_error_rate += field
            break
        elif valid_rules == len (tn):
            valid_tickets.append(tn)

print ("Part 1: scanning error rate: %d" %scan_error_rate)

index_to_search = []
for i in range(len(rules)):
    index_to_search.append(i)

while len(index_to_search) > 0:
    for field_name in rules.keys():
        if len(rules[field_name])==4:
            crit = rules[field_name]
        else:
            # skip processing as we already assigned this rule
            continue
        choices = {}
        for field_ind in index_to_search:
            compliant_at_ind = 0

            for tn in valid_tickets:
                if is_field_compliant(tn[field_ind],crit):
                    compliant_at_ind+=1

            if compliant_at_ind == len(valid_tickets):
                if field_name in choices:
                    choices[field_name].append(field_ind)
                else:
                    choices[field_name] = [field_ind]

        for field_name in choices.keys():
            #only fields that have one possibility can be identified
            # and the index is excluded from further searches
            if len(choices[field_name]) == 1:
                rules[field_name].append(choices[field_name][0])
                index_to_search.remove (choices[field_name][0])

score = 1
for field_name in rules.keys():
    if field_name.startswith("departure"):
        score *= my_ticket[rules[field_name][4]]
print ("Part 2: departure rules score: %d" %score)
