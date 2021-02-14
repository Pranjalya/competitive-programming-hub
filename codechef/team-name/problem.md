<h2><div id="title">Team Name</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
Сhef has assembled a football team! Now he needs to choose a name for his team. There are N words in English that Chef considers funny. These words are s1,s2,…,sN.

Chef thinks that a good team name should consist of two words such that they are not funny, but if we swap the first letters in them, the resulting words are funny. Note that under the given constraints, this means that a word is a non-empty string containing only lowercase English letters.

Can you tell Chef how many good team names there are?
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T
test cases follows.
- The first line of each test case contains a single integer N.
- The second line contains N space-separated strings s1,s2,…,sN.

### Output

For each test case, print a single line containing one integer — the number of ways to choose a good team name.

### Constraints

- 1≤T≤100
- 2≤N≤2*10^4
- 2 ≤ |si| ≤ 20 for each valid i
- s1,s2,…,sN contain only lowercase English letters
- s1,s2,…,sN are pairwise distinct
- The sum of N over all test cases does not exceed 2*10^4

#### Sample

3
2
suf mas
3
good game guys
4
hell bell best test

__O/P__

2
0
2