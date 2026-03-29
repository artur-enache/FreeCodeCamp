# ANALYSIS/BRAIN DUMP

## What is the input?
A string that follows a certain pattern

## What is the expected output?
True if the input is valid, False if the input is invalid

## How can I transform the input into the expected output?
I need to understand the rules of how an ISBN-10 is formed.

---

According to the specs:
The string can have a number of hyphens (how many? do their positions matter? can there be any number of digits between two hyphens?)
After removing the hyphens, I am left with 10 characters.
The first 9 must be digits, and the last one can be either an X or a digit.

After a web search, it seems like an ISBN-10 has 4 groups of digits, separated by a hyphen. In which case there would be three hyphens. However, maybe it's best to stick to the info I have in the challenge description. It also gave me a list of test cases:

```python
is_valid_isbn10("0-306-40615-2") should return True.
is_valid_isbn10("0-6822-2589-4") should return True.
is_valid_isbn10("0-8044-2957-X") should return True.
is_valid_isbn10("0-306-40615-1") should return False.
is_valid_isbn10("X-306-40615-2") should return False.
```

Based on this, I can say with certainty that:
- there are 13 total characters in the input string (which means that I don't need to validate the length of the input)
- there are 3 hyphens that separate 4 groups of chars (which means that I can use a regex pattern)
- X is always upper case (which means that I don't need to transform the input string case)

Re-reading the challenge description, I realize that I don't even need to use a complicated regex.
I can simply strip the hyphens out of the input directly, then obtain a list of characters.
Then, I can check if the list contains X and if it does, if it's on the last position.

But these are extra calculations. Using a regex right when I receive the input would save resources (I think? I am not sure about this one). I think that the approach does not matter: the calculation takes place only once per input in either case.

So, let's try some pseudocode:

```
CREATE regex pattern
GET input
COMPARE input to regex pattern
IF FALSE, return
ELIF TRUE, loop over the list
multiply each digit with its position, store it in a variable
if the digit == X, multiply 10 with its position, add it to the same variable
IF variable % 11 == 0 THEN return True
ELSE return False
```

It works, but it is not covering a whole lot of edge cases. However, these edge cases were not specified in the exercise, so I am assuming they are out of scope for this.
