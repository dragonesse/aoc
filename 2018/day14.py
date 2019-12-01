import sys

print("Day 14 puzzle: Chocolate Charts");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
num_recipes = 0

with open(puzzle_file, 'r') as puzzle_in:

    num_recipes = int(puzzle_in.readline().strip("\n"))
puzzle_in.close()

class Elve:
    def __init__(scoreboard_index):
        self.index = scoreboard_index

scoreboard = [3, 7]

elve1_index = 0
elve2_index = 1

def create_receipes (rec1,rec2):
    return list(str(rec1 + rec2))

def add_receipes (new_recipes,scoreboard):
    [scoreboard.append(int(r)) for r in new_recipes]
    return

def pick_new_receipe (cur_recipe_index, scoreboard):
    num_steps = scoreboard[cur_recipe_index] + 1
    next_index = -1
    num_recipes = len(scoreboard)
    if cur_recipe_index + num_steps < num_recipes - 1:
        next_index = cur_recipe_index + num_steps
    else:
        next_index = (num_steps - (num_recipes  - cur_recipe_index)) % num_recipes

    return next_index


# num_recipes = 2018

receipes_ready = len(scoreboard)
while receipes_ready < num_recipes + 10:
    new_rec = create_receipes (scoreboard[elve1_index], scoreboard[elve2_index])

    add_receipes(new_rec,scoreboard)
    receipes_ready = len(scoreboard)
    if receipes_ready == num_recipes:
        print ("------counting 10 receipes from here")
    elve1_index = pick_new_receipe(elve1_index,scoreboard)
    elve2_index = pick_new_receipe(elve2_index,scoreboard)
    # print (scoreboard)
    # print ("Elve 1 position %d" %(elve1_index))
    # print ("Elve 2 position %d \n" %(elve2_index))

final_score = ''.join([str(x) for x in scoreboard[num_recipes:num_recipes+10]])
print ("The final scoreboard is: %s" %(final_score))