#!/user/bin/env python3

X_B = {
("B", "S1"): ('X', "R", "S2"),
("B", "S2"): ('B', "L", "S3"),
("X", "S3"): ('B', "R", "S4"),
("B", "S4"): ("B", "L", "S1"),
}

ADDER = {
    ("B", "S1"): ("(", "R", "S2"),
    ("B", "S2"): ("1", "R", "S3"),
    ("B", "S3"): ("1", "R", "S4"),
    ("B", "S4"): ("+", "R", "S5"),
    ("B", "S5"): ("1", "R", "S6"),
    ("B", "S6"): ("1", "R", "S7"),
    ("B", "S7"): ("1", "R", "S7B"),
    ("B", "S7B"): ("1", "R", "S8"),
    ("B", "S8"): (")", "R", "S9"),

    ("B", "S9"): ("B", "L", "S9"),
    (")", "S9"): (")", "L", "S9"),
    ("1", "S9"): ("1", "L", "S9"),
    ("+", "S9"): ("1", "RL", "S10"),

    ("1", "S10"): ("1", "R", "S10"),
    (")", "S10"): ("B", "L", "S11"),

    ("1", "S11"): (")", "R", "S12"),

    ("B", "S12"): ("B", "R", "S12")
}

def simulate(instructions):
    tape, head, state = ["B"] * 16, 0, "S1"

    for _ in range(32):
        print(state.rjust(4) + ": " + "".join(tape))
        print("      " + " " * head + "^")
        tape[head], head_dir, state = instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else -1

simulate(ADDER)
