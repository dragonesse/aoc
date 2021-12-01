import sys;
import utils.inputReaders as ir

print("Day 1 puzzle: Report Repair");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
expenses = ir.read_int_records_as_list_entries(puzzle_file)

#level 1 solution
for i in (range(len(expenses)-1)):
    for j in range(i+1,len(expenses)) :
        if expenses[i] + expenses[j] ==2020:
            print ("part 1: found the numbers %d %d the multiplication %d" %(expenses[i],expenses[j],expenses[i]*expenses[j]))
            break

# level 2 solution
have_my_number = False
for i in (range(len(expenses)-1)):
    for j in range(i+1,len(expenses)) :
        if have_my_number:
            break
        if expenses[i] + expenses[j] < 2020:
            # want to exlude items we currently process under i or j
            index_to_check = list(range (i+1,j))+list(range(j+1,len(expenses)))
            for k in index_to_check:
                if expenses[i] + expenses[j] +expenses[k] ==2020:
                    have_my_number = True
                    print ("part 2: found the numbers %d %d %d the multiplication %d" %(expenses[i],expenses[j],expenses[k],expenses[i]*expenses[j]*expenses[k]))
                    break