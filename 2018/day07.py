import sys
import re

print("Day 7 puzzle: The Sum of Its Parts")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!")
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
ikea_booklet = {}
split_pattern = re.compile(r'\b([A-Z]{1})\b.*\b([A-Z]{1})\b')

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        [_, parent, child, _] = re.split(split_pattern,cur_line)
        if parent not in ikea_booklet.keys():
            ikea_booklet[parent] = child
        else:
            ikea_booklet[parent] = ikea_booklet[parent] + child

puzzle_in.close()

for i in ikea_booklet.keys():
    print ("parent %s children %s" %(i,ikea_booklet[i]))

def can_execute_step (step, instructions):
    # we can proceed with a step, if its children are on list of values only once
    # print ("-----validating step %s " %(step))
    num_hits = 0
    for v in instructions.values():
       # print ("checking value %s for presence of %s" %(v,step))
       if v.count(step) > 0 :
            num_hits += 1

    return num_hits == 0

def find_independent_steps (instructions):
    step_list = []
    for s in instructions.keys():
        if can_execute_step(s,instructions):
            step_list.append(s)
    print ("following steps are independent: %s" %(step_list))
    return step_list

def execute_step (step,instructions):
    if step in instructions.keys():
        return instructions.pop(step)
    else:
        return None

def build_sleight (steps, instructions):
    sequence = ""
    followers = steps
    while followers is not None:
        # if len(steps) < 1:
        #     break
        print ("building sleight from available steps: ",steps)

        for s in sorted(steps):
            if can_execute_step(s,instructions):
                print ("%s analysis, removing the step %s from global set" %(steps,s))

                followers = execute_step(s,instructions)
                print ("steps unblocked by %s: " %(s),[followers])
                if s not in sequence:
                    sequence += s
                # if followers is not None:
                print ("we try hard with next round")
                sequence += build_sleight(followers,instructions)
                # else:
                #     break
            else:
                print ("it's not time for %s yet" %(s))
                steps = find_independent_steps(instructions)
                break

    return sequence

i = {'F':'E'}
build_sequence = build_sleight(find_independent_steps(i),i)

build_sequence = build_sleight(find_independent_steps(ikea_booklet), ikea_booklet)

print ("The order of tasks is: ", build_sequence)

