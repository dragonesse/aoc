import sys;
import utils.inputReaders as ir

print("Day 2: Rock Paper Scissors");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
secret_book = ir.read_oneline_records_as_list_entries(puzzle_file)

print (secret_book)

supply_list = []

def translate_rule (single_round):
    # A for Rock, B for Paper, and C for Scissors.
    # X for Rock, Y for Paper, and Z for Scissors

    rule_mapping = {
        "A X" : "R R",
        "B X" : "P R",
        "C X" : "S R",
        "A Y" : "R P",
        "B Y" : "P P",
        "C Y" : "S P",
        "A Z" : "R S",
        "B Z" : "P S",
        "C Z" : "S S"
    }

    return rule_mapping [single_round]



def determine_game_outcome (decoded_round):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # (1 for Rock, 2 for Paper, and 3 for Scissors)
    # plus (0 if you lost, 3 if the round was a draw, and 6 if you won).
    scoring = {
        "R R" : 3 + 1,
        "P R" : 0 + 1,
        "S R" : 6 + 1,
        "R P" : 6 + 2,
        "P P" : 3 + 2,
        "S P" : 0 + 2,
        "R S" : 0 + 3,
        "P S" : 6 + 3,
        "S S" : 3 + 3
    }
    return scoring [decoded_round]

score = 0
for game in secret_book:
    score += determine_game_outcome(translate_rule(game))


print ("Part 1: your score is: {}".format(score))

sys.exit(0)
top3 = sorted(supply_list)[-3:]
print ("Part 2: the sum of calories for top 3 equipped elves is: {}".format(sum(top3)))
