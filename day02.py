import sys
import re

print("Day 2 puzzle: Password Philosophy");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file

constraints = []
passwords = []

# sample input: 1-11 h: hhhhchhhhjhph
policy_regex=re.compile(r'^([0-9]+)-([0-9]+)\s([a-z]):\s([a-z]+)$')
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        split_result = list(re.match(policy_regex,cur_line).groups())
        constraints.append(split_result[0:3])
        passwords.append(split_result[3])

puzzle_in.close()


def is_password_compliant (policy,passwd):
    letter = policy[2]
    min_val = int(policy[0])
    max_val = int(policy[1])
    validation_res = passwd.count(letter)
    if validation_res <=max_val and validation_res>=min_val:
        return True
    else:
        return False

def is_password_compliant_policy2 (policy,passwd):
    letter = policy[2]
    index_1 = int(policy[0]) - 1 #to make 0-based
    index_2 = int(policy[1]) - 1
    if (passwd[index_1] == letter and passwd[index_2] != letter) or\
       (passwd[index_2] == letter and passwd[index_1] != letter):
        return True
    else:
        return False

password_counter = 0
password_counter_2 = 0
for i in range(len(constraints)):
    if is_password_compliant(constraints[i],passwords[i]):
        password_counter += 1

    if is_password_compliant_policy2(constraints[i],passwords[i]):
        password_counter_2 += 1


print ("Number of compliant passwords policy #1: %d" %password_counter)
print ("Number of compliant passwords policy #2: %d" %password_counter_2)
