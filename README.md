# TruthTable0 ToolKit

## A truth table tool for CLI and File enthousiastes

_TT0TK_ or _TruthTable0 ToolKit_ is a python3 program made to simplify working
with truth tables and linear algebra. It offers a simple interface and works
with the `tt0` format, which is a text format with some details we'll se below.

## Quick start

First things first, you must have _python3_ installed

``` shell
> python3 --version
Python 3.9.6
```

After that, you'll need to install _sympy_ with (or anything else, if it works,
it works!)

``` shell
> python3 -m pip install sympy
```

Finally, you can run `TT0TK`:

``` shell
> python3 tt0tk.py help
TruthTable0 TookKit - v0.1.1
A toolkit for TT0 file format

Usage: tt0tk.py <command> [args]
Commands:
  help [format]        | Prints help (duh)
  formula <input.tt0>  | Get raw formulas of TT
  simplify <input.tt0> | Get simplified formulas of TT
```

You can run the example if ou want to..

``` shell
> python3 tt0tk.py formula examples/ADR3_XOR-AND-OR.tt0
Q0 = (~a & ~b & c) | (~a & b & ~c) | (a & ~b & ~c) | (a & b & c)
Q1 = (a & b & c)
Q2 = (~a & ~b & c) | (~a & b & ~c) | (~a & b & c) | (a & ~b & ~c) | (a & ~b & c) | (a & b & ~c) | (a & b & c)
> python3 tt0tk.py simplify examples/ADR3_XOR-AND-OR.tt0
Q0 = (a & b & c) | (a & ~b & ~c) | (b & ~a & ~c) | (c & ~a & ~b)
Q1 = a & b & c
Q2 = a | b | c
```

As you can see, the `AND` and `OR` have been correctly simplified. The XOR is
still pretty much the same because there are not support for `XOR` operator for
the moment.

## TT0 format

The TT0 format is made to describe a truth table by the most understandable way 
possible (at least for me). 

No bloat, no specific program to handle the file, only a text file with an 
extension and bits written in it. Each line of the file is a line of the 
truth table. A line contains an address and a value (binary, any length, must 
be the same length), separated by a single space.

Example: truth table of a (XOR3, AND3, OR3)

``` tt0
000 000
001 101
010 101
011 001
100 101
101 001
110 001
111 111
```

You can change the order of the lines in the file, it doesn't matter. For
duplicats, the formula minterms will get duplicated.

``` tt0
011 001
110 001
000 000
010 101
111 111
001 101
100 101
101 001
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
  formula <input.tt0>  | Get raw formulas of TT
  simplify <input.tt0> | Get simplified formulas of TT
```

Notice that you can also make the program executable on Linux and MacOS, so you
can directly run `./tt0tk.py help`

## Development

I'll probably stop development of this tool really fast, so be free to fork the
repository and make you own changes. You can still submit issues and PRs but I
might have already quit the project since then!

