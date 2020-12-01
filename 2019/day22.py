import sys
import re
print("Day 22 puzzle: Slam Shuffle");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
shuffle_order = []
pattern =  re.compile(r'^([a-z,\s]+)([-,0-9]*)$')
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        shuffle_order.append( list(re.match(pattern,cur_line).groups()) )
puzzle_in.close()

def cut_cards(deck, amount):
    if amount > 0:
        bottom = deck[:amount]
        del deck[:amount]
        deck += bottom
    elif amount < 0:
        top = deck[amount:]
        del deck [amount:]
        deck = top + deck
    print ("==== cut_cards")
    return deck

def deal_with_inc(deck, amount):
    table = [0] * len(deck)
    table_pos = 0
    table [table_pos] = deck [0]
    for i in range(1,len(deck)):
        table_pos = calc_next_pos(table_pos,amount,len(deck))
        table [table_pos] = deck[i]
    print ("==== deal_with_inc")
    return table

def calc_next_pos (cur_pos, offset, deck_size):
    if offset >= deck_size:
        raise NotImplementedError
    if cur_pos + offset < deck_size - 1:
        return cur_pos + offset
    else:
        return (cur_pos + offset) - deck_size

def deal_new_stack (deck):
    print ("==== deal_new_stack")
    return list(reversed(deck))

factory_deck = []
deck_size = 10007

for i in range (deck_size):
    factory_deck += [i]

test_deck = [0,1,2,3,4,5,6,7,8,9]
# deck = test_deck
deck = factory_deck

# process instrunctions
for step in shuffle_order:
    # print ("step: ", step[0], " arg: ", step[1])
    if "cut" in step [0]:
        deck = cut_cards(deck,int(step[1]))
    elif "increment" in step [0]:
        deck = deal_with_inc(deck, int(step[1]))
    elif "new" in step [0]:
        deck = deal_new_stack(deck)

print ("card 2019 is on position:", deck.index(2019))