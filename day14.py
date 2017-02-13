import hashlib;
import re;
print("Day 14 puzzle: One-Time Pad");

if(len(sys.argv) == 1):
    print ("Please provide salt as argument!");
    sys.exit();
else:
    salt = sys.argv[1];

int_index   = 0;

num_found = 0;
max_num_keys = 64;

def generate_md5 (input):
    hash_vault = hashlib.md5(str.encode(input));
    return hash_vault.hexdigest();

keys_found = [];
hash_queue = [][];
while len(keys_found) < max_num_keys:


    # if hash queue is empty, calculate new hash

    cur_md5 = generate_md5(salt+str(int_index));

     # if not

    if re.match('[0-9]{3}',hash_vault.hexdigest()):
        print (hash_in);
        print (hash_vault.hexdigest());
        # test for next 1000 hashes

        # calculate i+1 hash
        # check for triple (we'll have to do that anyway)
        # if matchess, store triple and i
        # check for sequence of five
        # if matches, increase num of hashes in 1000
        # if not, increase i


    int_index += 1;
print ("password is %s" %password);