# ANALYSIS / BRAIN DUMP
This document contains my thought process. It is messy, as I did not intend for it to be read by anyone after writing down my ideas (not even myself), but I would like to keep it as a record.

## "What is the input?"
The input is not the triangle, but only n

## "What is the expected output?"
Return the n-th row in the triangle; this row is an array that is built according to some specific rules

## "How can I transform the input into the expected output?"
First, I need to understand how to express the rules for building the triangle. After I understand it, then I can:

- A) build a triangle according to the rules, then extract the n-th row, OR
- B) build the n-th row directly

---

Rows are numbered starting from 1

`row[0] == row[-1] == 1`

## What does an "interior" value mean?
It must be any value between `row[0]` and `row[-1]`, excluding these two

```
    1 - 1
   1 1 - 1; None; 1
  1 2 1 - 1; row(n-3)[0] + row(n-2)[1]; 1
 1 3 3 1 - 1; row(n-2)[0] + row(n-2)[1]; row(n-2)[1] + row(n-2)[2]; 1
1 4 6 4 1 - 1; row(n-1)[0] + row(n-1)[1]; row(n-1)[1] + row(n-1)[2]; row(n-1)[2] + row(n-1)[3]; 1
```

The length of each row is n; `len(fifth row) = 5`
Each row contains `len - 2` interior values

---

I spotted a pattern: to build row n, take the n-1 row, and split it in pairs of 2.
Ex. row 4: `(1, 3), (3, 3), (3, 1)`; afterwards, row 5 is: first element 1, followed by the sum of the first tuple's elements, followed by the second's sum, etc., followed by 1 at the end

But going by this approach, I would have to calculate each n-1 row in order to obtain n. Inefficient. What if I write the triangle in a different way?

```
0        0 0
1       0 1 0
2      0 1 1 0
3     0 1 2 1 0
4    0 1 3 3 1 0
5   0 1 4 6 4 1 0
6 0 1 5 10|10 5 1 0 0
```

Another pattern: when the row n has an odd number of elements, max is in position `len(n)/2 + 1`
When it has an even number of elements, max is in position `len(n)/2`
Technically, each "inner" element's value already "encodes" two other elements in it - in order for an inner element to exist, it must be a sum of two existing elements.

Written as an array then, the triangle is:

```
[
    1,
    1, 1,
    1, 2, 1,
    1, 3, 3, 1,
    1, 4, 6, 4, 1,
    1, 5, 10, 10, 5, 1,
    1, 8, 28, 56, 70, 56, 28, 8, 1
]
```

The most obvious solution is to create this array row by row, but it would be very inefficient. What if I build it row by row, but discard the previous row when I am done with it?

So let's assume the input is "4". I build:

```
row_B = [0, 1]
row_A = [ sum of two (0+1) ] = [1]
row_B = [ sum of two (0+1), sum of two  (1+0) ] = [1, 1]
row_A = [ sum of two (0+1), sum of two (1+1), sum of two (1+0) ] = [1, 2, 1]
row_B = [ sum of two (0+1), sum(1+2), sum(2+1), sum(1+0) ] = [1, 3, 3, 1]
```

Basically:

```
sum(row[0], row[1]), sum(row[1], row[2]), sum(row[2], row[3]), ..., sum(row[n-3], row[n-2]), sum(row[n-2], row[n-1])
```

I start with an array of `[0, 1]` representing `n=0`
`n=1` is `sum(row[0], row[1])` (`[1]`)
`n=2` is `sum(row[0], row[1]), sum(row[1], row[2])` (`[1, 1]`)

But it doesn't make sense, because the arrays don't have enough elements in order to be able to calculate the sum

### Possible solution

- Start with array `A [0, 1]` that represents line `n=0`
- Iterate over it enough times to reach the highest value of line n+1: `for i in range(0, (n // 2) + (n % 2) + 1)`
- New element is `A[i] + A[i+1]`; save them in array `B`
- At the end of the iteration, overwrite `A` with `B`
- At the end of the loop, the output array is `B + reversed(B)[n%2:-1]`

But the problem is the same: I need to iterate over array `A`, which after the first iteration will have only 1 element, which is insufficient.

---

What if instead, I build a long string containing all lines? Then I can access the n-th line by extracting the elements in the range starting at `list[n-1]` for an interval of `[n]` elements

Maybe even simpler. Assuming n is 4, I can do this:

```
list = [1, 0, 0, 1] (I know that the final list will always contain 1 as the first & last element)
Then iterate n times, and build each line by replacing elements inside this list
[1, 1, 0, 1]
[1, 2, 1, 1]
[1, 3, 3, 1]
```

But I have a problem: `n = 1` will return `[1, 1]`, not `[1]`; so I have to treat that separately
