<h2><div id="title">Escape The Forbidden Forest</h2></div>

### Problem Statement

<div id="problem_statement">
<p>
Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them. But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety. The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. </p>
<p>Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges that Penelope can build and save everyone from the Devil</p>
<p>Note: Each tree in the forest belongs to one of the 3 categories represented by * or # or @</p>

#### Input

First line of input contains number of testcases, T. For each testcase, there will be a single line containing two space separated strings str1 and str2 representing the trees on either side of the river. 

#### Output
For each test case, print the maximum number of bridges that Penelope can build. 

#### Constraints

1 <= T <= 100  
1 <= N, M <= 100  

##### Example

__Sample Input__

2  
*@#* *#  
*** ##  

__Sample Output__

2  
0  

__Explanation__

Testcase 1: str1 = "*@#*" and str2 = "*#"  
Two bridges can be built between the banks of the river in the following manner.  
```
* @ # *
|      |
*     #
```