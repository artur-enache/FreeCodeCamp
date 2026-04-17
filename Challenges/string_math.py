"""String Math
https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-16

What is the input? A string which can contain any number of characters.
What is the output? The result of some math operations performed on digits in the input, according to some rules
How do I turn the input into the output?

There are some rules that apply to the input. As an example, the string below:
3ab10c8

Contains the following relevant substrings

3
ab
10
c
8

The digits on which to perform the math operations are 3, 10 and 8
The math operations are determined by the # of chars separating groups of digits. Even chars: addition; odd chars:
subtraction

So "3 ab 10 c 8" becomes "3 + 10 - 8" which is 5.

The steps I can implement are:
split the input string into two types of substrings
consecutive digits, or consecutive non-digit characters
save the substrings into two different lists
iterate over the lists
apply the operations

But a big limitation for the approach above is that the operations I care about are the ones determined by sequences
of characters between digits (so not the ones at the beginning or end of the string;
take for example the string "a.67,1$lk6ld")

If I use regex, I might eliminate the leading & trailing non-digit characters by saving only the strings that look
like: \d+.+\d+

In code, it means:
pattern = re.compile(r"\d+.+\d+")
result = re.search(pattern, input_string).group()

"a.67,1$lk6ld" becomes '67,1$lk6'
"""



import pytest, re

def do_math(input_string: str) -> int:
    pass

def test_1():
    assert do_math("3ab10c8") == 5

def test_2():
    assert do_math("6MINUS4") == 2

def test_3():
    assert do_math("9plus3") == 12

def test_4():
    assert do_math("5fkwo#10i#%.<>15P=@20!#B/25") == 15

def test_5():
    assert do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt") == 67