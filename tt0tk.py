#!python3

import sys
from sympy.logic.boolalg import to_dnf

__name__ = "TruthTable0 TookKit - v0.1.2"
__desc__ = "A toolkit for TT0 file format"

def get_formulas(filename):
    with open(input_path, "r") as fp:
        addrlen = -1
        vallen = -1
        # Will be set with empty strings once the value length is known
        formulas = [] 
        seenExpr = []

        for line in fp:
            line = line[:-1]
            if len(line) < 3 or line[0] == "#":
                continue
            (addr, val) = line.split(" ")
            print(f"{line}: {addr} -> {val}")

            if len(addr) == 0 or len(val) == 0:
                sys.exit(f"Empty address or value: {line}")
            if addrlen == -1:
                addrlen = len(addr);
            if vallen == -1:
                vallen = len(val);
                formulas = [""]*len(val)
                seenExpr = [False]*len(val)
            if len(addr) != addrlen:
                sys.exit("the address length changed")
            if len(val) != vallen:
                sys.exit("the value length changed")

            for i in range(len(val)):
                if val[i] == "1":
                    if seenExpr[i]:
                        formulas[i] += " | " # Add a `+`
                    seenExpr[i] = True
                    formulas[i] += decode_minterm(addr)

        return formulas

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
        print("  formula <input.tt0>  | Get raw formulas of TT")
        print("  simplify <input.tt0> | Get simplified formulas of TT")
    elif sys.argv[2] == "format":
        print("TT0 format: Truth table description")
        print("  The TT0 format is made to describe a truth table by the most")
        print("    understandable way possible (for me). No bloat, no specific")
        print("    program, only a text file with an extension and with and bits")
        print("    written in it")
        print("  Each line of the file is a line of the truth table.")
        print("  A line can be a comment if it starts with a '#', empty lines")
        print("    Are ignored too")
        print("  A line contains an address and a value (binary, any length,")
        print("    must be the length). The address anv the value are separated")
        print("    by a single space")
        print("  Example: truth table of a (XOR,AND,OR)")
        print("    00 000")
        print("    01 101")
        print("    10 001")
        print("    11 111")
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

    formulas = get_formulas(input_path)
    for i in range(len(formulas)):
        print(f"Q{i} = {formulas[i]}")
elif action == "simplify":
    if len(sys.argv) != 3:
        sys.exit(f"Unexpected number of arguments... See `{program} help`")
    input_path = sys.argv[2]
    # Verify input extension
    if input_path[-4:] != ".tt0":
        sys.exit(f"Bad extension: got {input_path[-4:]}, expected .tt0")

    formulas = get_formulas(input_path)
    for i in range(len(formulas)):
        print(f"Q{i} = {to_dnf(formulas[i], simplify=True)}")
else:
    sys.exit(f"Unknown action {action}, see `{program} help`")
