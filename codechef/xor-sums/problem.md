<h2><div id="title">XOR Sums</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
You are given a sequence of positive integers `A1,A2,…,AN`. You should answer `Q` queries. In each query:

- You are given a positive integer M
- Consider all non-empty subsequences of A with length ≤ M
- Recall that a subsequence is any sequence that can be created by deleting zero or more elements without changing the order of the remaining elements.
- For each of these subsequences, compute the bitwise XOR of its elements.

Your task is to determine the sum of these values. Since this sum can be very large, compute it modulo 998,244,353.
</div>

### Input

- The first line of the input contains a single integer N
- The second line contains N space-separated integers A1,A2,…,AN
- The third line contains a single integer Q
- Q lines follow. Each of these lines contains a single integer M describing a query.

### Output

For each query, print a single line containing one integer ― the sum of bitwise XORs for all subsequences of A with length ≤ M, modulo 998,244,353.

### Constraints

- 1 ≤ N,Q ≤ 2 * 10^5
- 1 ≤ Ai < 2^30 for each valid i
- 1 ≤ M ≤ N

#### Sample

4
1 3 5 2
2
1
2

__O/P__

11
34