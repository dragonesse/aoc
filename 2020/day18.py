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
        parse_res = re.findall(r"(\([0-9]+[^(,)]+[0-9]+\))",equation)
        for e in parse_res:
           tmp = evaluate_result_simple_ops(e[1:-1])
           equation = equation.replace(e,str(tmp))
    res = evaluate_result_simple_ops(equation)
    return res


def evaluate_result_simple_ops (equation):
    tokens = []
    if ('(' in equation) or (')' in equation):
        print ("not supposed to process nested levels")
        return None

    tokens = equation.split(" ")
    # process operations from left to right
    res = int(tokens[0])
    for ti in range(1,len(tokens),2):
        if tokens[ti] == '+':
            res += int(tokens[ti+1])
        elif tokens[ti] == '*':
            res *= int(tokens[ti+1])

    return res

answer = 0
for exercise in homework:
    answer += evaluate_result (exercise)

print ("Part 1: the answer to the universe is %d" %answer)

def evaluate_result_simple_ops_add_precedence (equation):
    tokens = []
    if ('(' in equation) or (')' in equation):
        print ("not supposed to process nested levels")
        return None

    tokens = equation.split(" ")

    # resolve all addition at first
    while '+' in tokens:
        for ti in range(1,len(tokens),2):
            if tokens[ti] == '+':
                res = int(tokens[ti+1])+int(tokens[ti-1])
                tokens[ti-1] = str(res)
                del tokens [ti+1]
                del tokens [ti]
                break

    # process multiplication
    res = int(tokens[0])
    for ti in range(1,len(tokens),2):
        if tokens[ti] == '*':
            res *= int(tokens[ti+1])

    return res

def evaluate_result_new_rules (equation):
    res = 0
    # parse the equation
    while equation.count('(') > 0:
        parse_res = re.findall(r"(\([0-9]+[^(,)]+[0-9]+\))",equation)
        for e in parse_res:
           tmp = evaluate_result_simple_ops_add_precedence (e[1:-1])
           equation = equation.replace(e,str(tmp))
    res = evaluate_result_simple_ops_add_precedence (equation)
    return res

answer = 0
for exercise in homework:
    answer += evaluate_result_new_rules  (exercise)

print ("Part 2: the answer to the universe is %d" %answer)
