<h2><div id="title">Ninja's class</div></h2>

<h5>Severity : Medium</h5>

<h3>Problem Statement</h3>
<div id="problem_statement">
There are N students in Ninja’s classroom, including him, numbered from 1 to N. All of them got some amount of money in their pockets ( as all of them saved some amount of their pocket money). Lets money[i] denotes the amount of money the ith student has got (1<= i <=N).  
The monitor of the class can get the money of all students whose number is a factor of monitor’s number. For example, if there are 6 students in class and the 4th student is the monitor of class then he can get the money from 1st and 2nd student.
Note: The money of the monitor remains with him.  
So can you tell the amount of money ith (1<= i <=N) student will have if he became the monitor of the class.
</div>

#### Input format:

The first line of the input will contain T (number of test cases).
The first line of each test case will contain an integer N (number of students of the class).
Next N lines of each test case will have the amount of money the ith student has got.

#### Constraints:

1<=T<=100000  
1<=N<=100000  
1<=money[i]<=10^9  
Sum of N over-all test cases doesn’t exceed 5*10^5  

#### Output format:

For each test case, print N space-separated integers. The i'th (1<= i <=N)  integer will denote that the amount of money ith (1 <= i <= N) student can get if he became the monitor of the class in a new line.

#### Sample 

_Sample Input 1_

1  
4  
1  
2  
3  
4  

_Sample Output 1_:

1 3 4 7 