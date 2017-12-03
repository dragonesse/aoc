import hashlib;
import re;
print("Day 5 puzzle: How About a Nice Game of Chess");


door_id     = "uqwqemis";
int_index   = 0;

num_found = 0;

password   = ["","","","","","","",""];

while num_found < 8:
    hash_in = door_id+str(int_index);
    hash_vault = hashlib.md5(str.encode(hash_in));

    if re.match('0{5}[0-7]',hash_vault.hexdigest()):
        print (hash_in);
        print (hash_vault.hexdigest());

        if (password[int(hash_vault.hexdigest()[5])] == ""):
            password [int(hash_vault.hexdigest()[5])] = hash_vault.hexdigest()[6];
            print (password);
            num_found += 1;
        else:
            print ("good beginnig, but index already used");

    int_index += 1;
print ("password is %s" %password);