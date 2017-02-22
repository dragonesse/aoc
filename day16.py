import re;
import sys;
print("Day 16 puzzle: Dragon Checksum");

if(len(sys.argv) == 1):
    print ("Please provide initial state as argument!");
    sys.exit();
else:
    ini = sys.argv[1];

disk_size   = 35651584;

random_data = "";

# calculate random data
while len(random_data) < disk_size:

    if len(random_data):
        a = random_data;
    else:
        a = ini;

    # copy
    b = a;
    # reverse b
    rev_b = b[::-1];
    # change 1 to 0 znad 0s to 1s
    tmp_b = rev_b.replace("0","A");
    b = tmp_b.replace("1", "0");
    b = b.replace("A","1");
    random_data = a + "0" + b;

# trim the input
random_data = random_data[:disk_size];

print ("random data %s" %random_data);

# calculate checksum:
checksum = "";
pair_same = re.compile(r'([0,1])\1');

checksum_in = random_data;
while not(len(checksum) % 2):

    i = 0;
    checksum = "";
    while i < (len(checksum_in) -1):
        if re.match(pair_same, checksum_in[i:i+2]):
            checksum += "1";
        else:
            checksum += "0";

        i += 2;
    checksum_in = checksum;

print ("calculated checksum for %d size is %s" %(disk_size,checksum));