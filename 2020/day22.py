import sys
import utils.locationHelpers as lh

print("Day 22 puzzle: Crab Combat");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
player1_deck =[]
player2_deck = []


with open(puzzle_file, 'r') as puzzle_in:
    deck = 0
    for cur_line in puzzle_in:
        if cur_line.strip() == "":
            deck = 0
        if deck == 1:
            player1_deck.append(int(cur_line.strip()))
        elif deck == 2:
            player2_deck.append(int(cur_line.strip()))
        if cur_line.strip() == "Player 1:":
            deck = 1
        elif cur_line.strip() == "Player 2:":
            deck = 2

puzzle_in.close()

deck1_len = len(player1_deck)
deck2_len = len(player2_deck)
double_deck = deck1_len * 2
deck1_index = 0
deck2_index = 0


# print (player1_deck,player2_deck)

def get_winner (card1,card2):
    return 1 if card1>card2 else 2

def get_score (winner_deck):
    winner_score = 0
    for i in range(1,len(winner_deck)+1):
        winner_score += i*winner_deck[-i]
    return winner_score

def update_winner_deck(winner_deck, card1, card2):
    winner_deck = winner_deck[1:]
    c1 = card1 if card1>card2 else card2
    c2 = card2 if card1>card2 else card1
    winner_deck.append(c1)
    winner_deck.append(c2)
    return winner_deck

def update_looser_deck(looser_deck):
    looser_deck = looser_deck[1:]
    return looser_deck

rnd_cntr = 0
while deck1_len * deck2_len != 0:
    #play
    rnd_cntr += 1
    print ("deck 1 %d deck 2 %d" %(deck1_len, deck2_len))
    c1 = player1_deck[0]
    c2 = player2_deck[0]
    winner = get_winner(c1,c2)
    if winner == 1:
        player1_deck = update_winner_deck(player1_deck,c1,c2)
        player2_deck = update_looser_deck(player2_deck)
        deck1_len +=1
        deck2_len -=1

    elif winner == 2:
        player2_deck = update_winner_deck(player2_deck,c1,c2)
        player1_deck = update_looser_deck(player1_deck)

        deck2_len +=1
        deck1_len -=1

    print ("round %d winner is player %d" %(rnd_cntr, winner))
    print (player1_deck, deck1_len)
    print (player2_deck, deck2_len)

ws = 0
if len(player1_deck)>0:
    print ("player 1 wins")
    ws = get_score (player1_deck)
else:
    print ("player 2 wins")
    ws = get_score (player2_deck)

print ("part 1: winner score is: %d" %(ws))
