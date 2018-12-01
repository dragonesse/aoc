import sys;
import re;

print("Day 25 puzzle: The Halting Problem");

class Turing:
    max_steps = 12667664
    tape_size = 6001
    def __init__(self):
        self.iterations = 0
        self.tape = [0]*self.tape_size;
        self.checksum = 0;

    def state_a (self, pos):
        new_state = ""
        new_pos = -1
        # If the current value is 0:
        if self.tape[pos] == 0:
            #   - Write the value 1.
            #   - Move one slot to the right.
            #   - Continue with state B.
            self.tape[pos] = 1
            self.checksum += 1
            new_pos = pos + 1
            new_state = "b"
        # If the current value is 1:
        else:
            #   - Write the value 0.
            self.tape[pos] = 0
            self.checksum -= 1
            #   - Move one slot to the left.
            #   - Continue with state C.
            new_pos = pos - 1
            new_state = "c"
        self.iterations += 1
        return [new_pos, new_state]

    def state_b(self, pos):
        new_state = ""
        new_pos = -1
        # In state B:
        #   If the current value is 0:
        if self.tape[pos] == 0:
            #     - Write the value 1.
            self.tape[pos] = 1
            self.checksum += 1
            #     - Move one slot to the left.
            #     - Continue with state A.
            new_pos = pos - 1
            new_state = "a"
        #   If the current value is 1:
        else:
            #     - Write the value 1.
            # tape[pos] = 1 - nothing changes
            #     - Move one slot to the right.
            #     - Continue with state D.
            new_pos = pos + 1
            new_state = "d"
        self.iterations += 1
        return [new_pos, new_state]

    def state_c(self, pos):
        # In state C:
        #   If the current value is 0:
        if self.tape [pos] == 0:
            #     - Write the value 0.
            # tape[pos] = 0 - nothing changes
            #     - Move one slot to the left.
            #     - Continue with state B.
            new_pos = pos - 1
            new_state = "b"
        #   If the current value is 1:
        else:
            #     - Write the value 0.
            self.tape[pos] = 0
            self.checksum -= 1;
            #     - Move one slot to the left.
            #     - Continue with state E.
            new_pos = pos - 1
            new_state = "e"
        self.iterations += 1
        return [new_pos, new_state]

    def state_d(self, pos):
        new_state = ""
        new_pos = -1
        # In state D:
        #   If the current value is 0:
        if self.tape[pos] == 0:
            #     - Write the value 1.
            self.tape[pos] = 1
            self.checksum += 1
            #     - Move one slot to the right.
            #     - Continue with state A.
            new_pos = pos + 1
            new_state = "a"
        #   If the current value is 1:
        else:
            #     - Write the value 0.
            self.tape[pos] = 0
            self.checksum -= 1
            #     - Move one slot to the right.
            #     - Continue with state B.
            new_pos = pos + 1
            new_state = "b"
        self.iterations += 1
        return [new_pos, new_state]

    def state_e(self, pos):
        new_state = ""
        new_pos = -1
        # In state E:
        #   If the current value is 0:
        if self.tape [pos] == 0:
            #     - Write the value 1.
            self.tape [pos] = 1
            self.checksum += 1
            #     - Move one slot to the left.
            #     - Continue with state F.
            new_pos = pos - 1
            new_state = "f"
        #   If the current value is 1:
        else:
            #     - Write the value 1.
            # tape[pos] = 1 - nothing changes
            #     - Move one slot to the left.
            #     - Continue with state C.
            new_pos = pos - 1
            new_state = "c"
        self.iterations += 1
        return [new_pos, new_state]

    def state_f(self, pos):
        new_state = ""
        new_pos = -1
        # In state F:
        #   If the current value is 0:
        if self.tape [pos] == 0:
            #     - Write the value 1.
            self.tape[pos] = 1
            self.checksum += 1
            #     - Move one slot to the right.
            #     - Continue with state D.
            new_pos = pos + 1
            new_state = "d"
        #   If the current value is 1:
        else:
            #     - Write the value 1.
            # tape[pos] = 1 - nothing changes
            #     - Move one slot to the right.
            #     - Continue with state A.
            new_pos = pos + 1
            new_state = "a"
        self.iterations += 1
        return [new_pos,new_state]

    def calc_checksum(self):
        states = {
            "a" : self.state_a,
            "b" : self.state_b,
            "c" : self.state_c,
            "d" : self.state_d,
            "e" : self.state_e,
            "f" : self.state_f
        }

        pos = (self.tape_size//2 + 1)
        stat = "a"
        while self.iterations < self.max_steps:
            [pos,stat] = states[stat](pos)
        return

turing_test = Turing()
turing_test.calc_checksum()

print ("the diagnostic checksum is %d " %(turing_test.checksum))