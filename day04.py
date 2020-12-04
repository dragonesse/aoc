import sys
import re

print("Day 4 puzzle: Passport Processing");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

customs_list = []

empty_line = re.compile(r'^$')

#open file
with open(puzzle_file, 'r') as puzzle_in:
    passport_data = ""
    for cur_line in puzzle_in:
        if re.search(empty_line,cur_line.strip()) is None:
            passport_data += ' ' + cur_line.strip()
        else:
            customs_list.append(passport_data[1:].split(" "))
            passport_data = ""
    customs_list.append(passport_data[1:].split(" "))
puzzle_in.close()

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)


def validate_byr(val):
    return int(val) >=1920 and int(val)<=2002

def validate_iyr(val):
    return int(val) >=2010 and int(val)<=2020

def validate_eyr(val):
    return int(val) >=2020 and int(val)<=2030

def validate_hgt (val):
    return  check_cm(val) or check_in(val)

def validate_hcl (val):
    return re.match(r'#[0-9,a-f]{6}$',val) is not None

def validate_ecl (val):
    return val in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]

def validate_pid (val):
    return re.match(r'[0-9]{9}$',val) is not None

def check_hght (hgt, minh, maxh):
    return hgt>=minh and hgt<=maxh

def check_cm (val):
    test_res = re.match(r'1[5-9][0-9]cm', val)
    if test_res is not None:
        return  check_hght (int(val[0:3]),150,193)
    else:
        return  False

def check_in (val):
    test_res    = re.match(r'[5-7][0-9]in',val)
    if test_res is not None:
        return  check_hght (int(val[0:2]),59,76)
    else:
        return  False

validation_checks = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
}
mand_values = validation_checks.keys()

number_of_valid_p = 0
number_of_valid_p2 = 0

for psp in customs_list:
    num_val = 0
    num_val2 = 0
    for metric in psp:
        [m_name,m_value] = metric.split(":")
        if m_name in mand_values:
            num_val +=1
            if validation_checks[m_name ](m_value):
                num_val2 +=1
    if num_val == 7:
        number_of_valid_p +=1
    if num_val2 ==7:
        number_of_valid_p2  +=1

print  ("number of valid passports #1: %d" %number_of_valid_p  )
print  ("number of valid passports #2: %d" %number_of_valid_p2  )