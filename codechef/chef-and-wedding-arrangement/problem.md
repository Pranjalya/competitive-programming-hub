<h2><div id="title">Add and Search Word</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
There are N guests (numbered 1 through N) coming to Chef's wedding. Each guest is part of a family; for each valid i, the i-th guest is part of family Fi. You need to help Chef find an optimal seating arrangement.

Chef may buy a number of tables, which are large enough for any number of guests, but the people sitting at each table must have consecutive numbers ― for any two guests i and j (i<j) sitting at the same table, guests i+1,i+2,…,j−1 must also sit at that table. Chef would have liked to seat all guests at a single table; however, he noticed that two guests i and j are likely to get into an argument if Fi=Fj and they are sitting at the same table.

Each table costs K rupees. Chef defines the inefficiency of a seating arrangement as the total cost of tables plus the number of guests who are likely to get into an argument with another guest. Tell Chef the minimum possible inefficiency which he can achieve.
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers N and K.
- The second line contains N space-separated integers F1,F2,…,FN.

### Output

For each test case, print a single line containing one integer ― the smallest possible inefficiency.

### Constraints

- 1≤T≤100
- 1≤N≤1,000
- 1≤K≤1,000
- 1≤Fi≤100 for each valid i
- The sum of N across test cases is ≤ 5,000

#### Sample

3
5 1
5 1 3 3 3
5 14
1 4 2 4 4
5 2
3 5 4 5 1

__O/P__

3
17
4

