import sys
import re

print("Day 7 puzzle: Handy Haversacks");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
packed_bag_regex=re.compile(r'^([a-z]+\s[a-z]+).*contain\s[0-9]+')
inside_bag_regex=re.compile(r'[0-9]+\s([a-z]+\s[a-z]+)')
empty_bag_regex=re.compile(r'^([a-z]+\s[a-z]+)\sbags\scontain\sno\sother.*')

luggage_policies ={}

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # print ("entry: %s" %cur_line)
        split_result = re.match(packed_bag_regex,cur_line)
        if split_result is not None:
            bag_key = split_result.groups()[0]
            bag_content = re.findall(inside_bag_regex,cur_line)
            # print(list(split_result.groups()))
            # print(bag_content)
        else:
            # print("bag is empty")
            bag_key = re.match(empty_bag_regex,cur_line).groups()[0]
            bag_content = ["empty"]
        if bag_key not in luggage_policies:
            luggage_policies[bag_key]=bag_content
        else:
            luggage_policies[bag_key]=luggage_policies[bag_key].append(bag_content)

puzzle_in.close()

# for b in luggage_policies.keys():
#     print(b,luggage_policies[b])

my_bag = "shiny gold"
# my_bag = ["muted yellow","bright white"]
# my_bag = ["light red"]

def find_bag_containers (bag):
    print ("processing bag %s" %bag)
    single_bag_res = []
    for out_bag, content in luggage_policies.items():
        # print("checking in:",content)
        if bag in content:
            single_bag_res.append(out_bag)

    print ("bag: %s is stored in: " %(bag),single_bag_res)
    return single_bag_res

all_paths=[]

bags_to_check = find_bag_containers(my_bag)
# ap_list = [my_bag +":"+ btc for btc in bags_to_check]
# print (ap_list)
# all_paths += [my_bag +":"+ btc for btc in bags_to_check]
all_paths+=bags_to_check


while len(bags_to_check) > 0:
    next_round = []
    for bag in bags_to_check:
        bags_to_check = find_bag_containers(bag)
        next_round += bags_to_check
        # all_paths+= [bag +":"+ btc for btc in bags_to_check]
        all_paths+=bags_to_check
    bags_to_check = next_round

print (len(set(all_paths)))