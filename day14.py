import hashlib;
import re;
import sys;
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

def check_sequence (num_chars, md5_in, char = None):
    rep_char = None;
    groups = re.findall(r"(?=([0-9,a-f])\1{"+str(num_chars-1)+"})", md5_in);

    if len(groups) > 0:
        if char is None:
            rep_char = groups[0];
        else:
            for tmp_char in groups:
                if tmp_char == char:
                    rep_char = tmp_char;
    return rep_char;

def stretch_key (md5_in, num_times):
   for i in range(num_times):
        md5_in = generate_md5(md5_in);
   return md5_in;

keys_found = 0;
# index, stretched hash
hash_queue = {};
key_stretch = 0;
while keys_found < max_num_keys:

    cur_md5 = "";
    # if hash queue is empty, or hash for given index not present; calculate new hash
    if (len(hash_queue.keys()) == 0) or (hash_queue.get(int_index) == None):
        print ("generating new md5");
        cur_md5 = generate_md5(salt+str(int_index));

        # stretch the hash
        cur_md5 = stretch_key(cur_md5, 2016);
    else:
        cur_md5 = hash_queue[int_index];
        del hash_queue[int_index];

    # check, if there are 3 characters in a row
    rep_char = check_sequence (3, cur_md5);
    # if so, search five of a kind characters in next 1000 hashes
    if rep_char:
        num_rep = 1;

        while num_rep <= 1000:
            # calculate i+1 hash
            if (hash_queue.get(int_index + num_rep) == None):
                next_md5 = generate_md5(salt+str(int_index + num_rep));

                # stretch the hash
                stretch = stretch_key(next_md5, 2016);
                hash_queue[int_index + num_rep] = stretch;
            else:
                next_md5 = hash_queue[int_index + num_rep];

            if check_sequence (5, next_md5, rep_char):
                print ("index %d hash %s is a valid key" %( int_index, cur_md5));
                print ("%s at index %d is the hash that matches five-in-row restriction" %(next_md5, num_rep + int_index));
                keys_found += 1;
                break;
            num_rep += 1;

    int_index += 1;
print ("keys found %d" %keys_found);