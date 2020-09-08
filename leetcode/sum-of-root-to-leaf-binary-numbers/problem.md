<h2><div id="title">Sum of Root To Leaf Binary Numbers</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.
</div>

#### Sample

Input: [1,0,1,0,1,0,1]  

Output: 22

Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22