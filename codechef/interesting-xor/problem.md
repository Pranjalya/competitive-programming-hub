<h2><div id="title">Interesting XOR!</h2></div>

### Problem Statement

<div id="problem_statement">
You are given an integer C. Let d be the smallest integer such that 2^d is strictly greater than C.

Consider all pairs of non-negative integers (A,B) such that A,B < 2^d and A ⊕ B = C (⊕ denotes the bitwise XOR operation). Find the maximum value of A⋅B over all these pairs.
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains a single integer C.

### Output

For each test case, print a single line containing one integer ― the maximum possible product A⋅B.

### Constraints

- 1≤T≤10^5
- 1≤C≤10^9

#### Sample

2
13
10

__O/P__

70
91

__Explanation__ :

_Example case 1_: The binary representation of 13 is "1101". We can use A=10 ("1010" in binary) and B=7 ("0111" in binary). This gives us the product 70. No other valid pair (A,B) can give us a larger product.

_Example case 2_: The binary representation of 10 is "1010". We can use A=13 ("1101") and B=7 ("0111"). This gives us the maximum product 91.