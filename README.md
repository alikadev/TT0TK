# TruthTable0 ToolKit

## A truth table tool for CLI and File enthousiastes

_TT0TK_ or _TruthTable0 ToolKit_ is a python3 program made to simplify working
with truth tables and linear algebra. It offers a simple interface and works
with the `tt0` format, which is a text format with some details we'll se below.

## TT0 format

The TT0 format is made to describe a truth table by the most understandable way 
possible (at least for me). 

No bloat, no specific program to handle the file, only a text file with an 
extension and bits written in it. Each line of the file is a line of the 
truth table. A line contains an address (binary, any length, must be the
same length) and a bit (0 or 1).

Example: truth table of a XOR 3

``` tt0
000 0
001 1
010 1 
011 0
100 1
101 0
110 0
111 1
```

You can change the order of the lines in the file, it doesn't matter. For
duplicats, the formula minterms will get duplicated.

``` tt0
101 0
100 1
001 1
010 1 
001 1
001 1
110 0
111 1
111 1
011 0
001 1
000 0
```

## TT0 TookKit

This python3 program should be able to run anywere if you have installed all
the dependencies:

- sympy (used for sympy.logic.boolalg)

After that, you'll be able to run the program. 

``` shell
> python3 tt0tk.py help
TruthTable0 TookKit - v0.1.0
A toolkit for TT0 file format

Usage: tt0tk.py <command> [args]
Commands:
  help [format]        | Prints help (duh)
  formula <input.tt0>  | Get raw formula of TT
  simplify <input.tt0> | Get simplified formula of TT
```

Notice that you can also make the program executable on Linux and MacOS, so you
can directly run `./tt0tk.py help`

## Development

I'll probably stop development of this tool really fast, so be free to fork the
repository and make you own changes. You can still submit issues and PRs but I
might have already quit the project since then!

