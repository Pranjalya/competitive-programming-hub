<h2><div id="title">Consecutive Adding</h2></div>

### Problem Statement

<div id="problem_statement">
You are given two matrices A and B, each with R rows (numbered 1 through R) and C columns (numbered 1 through C). Let's denote an element of A or B in row i and column j by A(i,j) or B(i,j) respectively.

You are also given an integer X. You may perform the following operation on A any number of times:
- Choose an integer v.
- Choose X consecutive elements of A, either in the same row or in the same column.
- Add v to each of the chosen elements of A

Determine whether it is possible to change A to B in a finite number of operations.
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T
test cases follows.
- The first line of each test case contains three space-separated integers R, C and X
- R lines follow. For each valid i, the i-th of these lines contains C space-separated integers Ai,1,Ai,2,…,Ai,C.
- R more lines follow. For each valid i, the i-th of these lines contains C space-separated integers Bi,1,Bi,2,…,Bi,C.

### Output

For each test case, print a single line containing the string "Yes" if there is a sequence of operations that changes the matrix A to B, or "No" if such a sequence of operations does not exist.

### Constraints

- 1≤T≤10^3
- 2≤R,C≤10^3
- 2≤X≤min(R,C)
- |Ai,j|,|Bi,j|≤10^9 for each valid i,j the sum of R over all test cases does not exceed 10^3
- the sum of C over all test cases does not exceed 10^3

#### Sample

3
2 2 2
1 2
0 1
0 0
0 0
2 2 2
1 2
0 1
0 0
-1 0
3 2 2
1 1
2 2
3 3
1 0
2 0
3 0

__O/P__

Yes
No
No

__Explanation__ :

- _Example case 1_: We can add −1 to both elements in row 1 and add −1 to both elements in column 2.
- _Example case 2_: After any operation, the sum of elements of A remains even. However, the sum of elements of B is odd, so A cannot be changed to B.