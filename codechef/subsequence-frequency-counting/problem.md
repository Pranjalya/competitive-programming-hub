<h2><div id="title">Add and Search Word</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
Chef has a sequence of integers A1,A2,…,AN. He takes a sheet of paper and for each non-empty subsequence B of this sequence, he does the following:
1. For each integer which appears in B, count its number of occurrences in the sequence B.
2. Choose the integer with the largest number of occurrences. If there are several options, choose the smallest one.
3. Finally, write down the chosen integer (an element of B) on the sheet of paper.  

For each integer between 1 and N inclusive, find out how many times it appears on Chef's sheet of paper. Since these numbers may be very large, compute them modulo 1,000,000,007 (10^9+7).
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N.
- The second line contains N space-separated integers A1,A2,…,AN.

### Output

For each test case, print a single line containing N space-separated integers. For each valid i, the i-th of these integers should be the number of occurrences of i on Chef's sheet of paper.

### Constraints

- 1≤T≤100
- 1≤Ai≤N for each valid i
- the sum of N over all test cases does not exceed 500,000

#### Sample

3
3
2 2 3
2
1 2
3
1 2 2

__O/P__

0 6 1
2 1
3 4 0