<h2><div id="title">Little Ashish's Huge Donation</h2></div>

##### Severity : Hard

##### Topic : Mathematics

### Problem Statement

<div id="problem_statement">
Little Ashish is doing internship at multiple places. Instead of giving parties to his friends he decided to donate candies to children. He likes solving puzzles and playing games. Hence he plays a small game. Suppose there are N children. The rules of the game are:
<ol>
<li>The i'th child gets i^2  candies (1 <= i^2 <= N).</li>
<li>The child cannot get a candy until and unless all the children before him (1 <= i < y) gets candies according to rule number 1.</li>
</ol>
<br/>
One of his jealous friends, Pipi, asks him "Given X (the number of candies) how many children will you be able to serve?". Little Ashish fears calculations and cannot solve this problem so he leaves this problem to the worthy programmers of the world. Help little Ashish in finding the solution.  
</div>

#### Input format

The first line contains an integer T i.e. the number of test cases.
T lines follow, each line containing an integer X.

#### Constraints

1 <= T <= 10000  
1 <= X <= 10^16

#### Output format

T lines each containing ouptut for the corresponding test case.

#### Sample

_Sample Input 1_:

3  
1  
5  
13  

_Sample Output 1_:

1  
2  
2
