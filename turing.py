#!/user/bin/env python3

X_B = {
("B", "S1"): ('X', "R", "S2"),
("B", "S2"): ('B', "L", "S3"),
("X", "S3"): ('B', "R", "S4"),
("B", "S4"): ("B", "L", "S1"),
}

def simulate(instructions):
    tape, head, state = ["B", "B"], 0, "S1"
    for _ in range(8):
        tape[head], head_dir, state = instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else -1

simulate(X_B)