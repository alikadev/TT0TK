#!python3

import sys
from sympy.logic.boolalg import to_dnf

__name__ = "TruthTable0 TookKit - v0.1.0"
__desc__ = "A toolkit for TT0 file format"

def get_formula(filename):
    with open(input_path, "r") as fp:
        addrlen = -1
        formula = ""
        seenExpr = False

        for line in fp:
            (addr, val) = line[:-1].split(" ")

            if addrlen == -1:
                addrlen = len(addr);
            if len(addr) != addrlen:
                sys.exit("the address length changed")

            if val == "1":
                if seenExpr:
                    formula += " | " # Add a `+`
                seenExpr = True
                formula += decode_minterm(addr)

        return formula

def decode_minterm(addr):
    formula = "("
    for i in range(len(addr)):
        if i != 0:
            formula += " & "
        if addr[i] == "0":
            formula += "~"
        formula += chr(i + ord("a"))
    formula += ")"
    return formula

def do_help():
    print(__name__)
    print(__desc__)
    print()
    if len(sys.argv) == 2:
        print(f"Usage: {program} <command> [args]")
        print("Commands:")
        print("  help [format]        | Prints help (duh)")
        print("  formula <input.tt0>  | Get raw formula of TT")
        print("  simplify <input.tt0> | Get simplified formula of TT")
    elif sys.argv[2] == "format":
        print("TT0 format: Truth table description")
        print("  The TT0 format is made to describe a truth table by the most")
        print("   understandable way possible (for me). No bloat, no specific")
        print("   program, only a text file with an extension and with and bits")
        print("   written in it")
        print("  Each line of the file is a line of the truth table.")
        print("  A line contains an address (binary, any length, must be the")
        print("   same length) and a bit (0 or 1).")
        print("  Example: truth table of a XOR")
        print("   01 1")
        print("   10 0")
        print("   00 0")
        print("   11 1")
    else:
        sys.exit(f"Unknown help page {sys.argv[2]}")


# === Verify args === #
# Has action
program = sys.argv[0]
if len(sys.argv) < 2:
    sys.exit(f"No action, see `{program} help`")
action = sys.argv[1]

if action == "help":
    do_help()
    sys.exit()
elif action == "formula":
    if len(sys.argv) != 3:
        sys.exit(f"Unexpected number of arguments... See `{program} help`")
    input_path = sys.argv[2]
    # Verify input extension
    if input_path[-4:] != ".tt0":
        sys.exit(f"Bad extension: got {input_path[-4:]}, expected .tt0")

    print(get_formula(input_path))
elif action == "simplify":
    if len(sys.argv) != 3:
        sys.exit(f"Unexpected number of arguments... See `{program} help`")
    input_path = sys.argv[2]
    # Verify input extension
    if input_path[-4:] != ".tt0":
        sys.exit(f"Bad extension: got {input_path[-4:]}, expected .tt0")

    print(to_dnf(get_formula(input_path), simplify=True))
else:
    sys.exit(f"Unknown action {action}, see `{program} help`")
