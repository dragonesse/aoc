import sys
import utils.inputReaders as ir
import re
print("Day 18: Operation Order");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

homework = ir.read_oneline_records_as_list_entries(puzzle_file)

def evaluate_result (equation):
    res = 0
    # parse the equation
    while equation.count('(') > 0:
        # print("======collapsing %s" %equation)
        parse_res = re.findall(r"(\([0-9]+[^(,)]+[0-9]+\))",equation)
        for e in parse_res:
           tmp = evaluate_result_simple_ops(e[1:-1])
           # print ("bracket eval res: %s" %str(tmp))
           equation = equation.replace(e,str(tmp))
           # print ("shortened equation: %s" %equation)
    res = evaluate_result_simple_ops(equation)
    return res

def evaluate_result_simple_ops (equation):
    tokens = []
    if ('(' in equation) or (')' in equation):
        print ("not supposed to process nested levels")
        return None

    tokens = equation.split(" ")
    res = int(tokens[0])
    # print ("evaluate_result_simple_ops for %s" %equation)
    for ti in range(1,len(tokens),2):
        # print ("processing token %d result by now: %d" %(ti,res))
        if tokens[ti] == '+':
            res += int(tokens[ti+1])
        elif tokens[ti] == '*':
            res *= int(tokens[ti+1])

    return res

answer = 0
for exercise in homework:
    answer += evaluate_result (exercise)

print ("the answer to the universe is %d" %answer)

