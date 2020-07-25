<h2><div id="title">Elixir for Life</h2></div>

### Problem Statement

<div id="problem_statement">
<p>
Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden. The garden consists of various plants represented by a string str where each letter represents a different plant. 
But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring) in the beginning of the forest (prefix), the end of the forest (suffix) and will also be the most frequent sequence present in the entire forest.</p>
<p>Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest.</p>
</div>

#### Input

The first line of input contains the number of test cases T. For each test case, there will be one line of input containing string str.

#### Output

Print the frequency of the substring of plants required to make the elixir.

#### Constraints 

1 ≤ T ≤ 100  
1 ≤ |str| ≤ 105  
str contains lower case alphabets only 

#### Example

__Input__

3  
ababaaaab  
aaaa  
abcdef  

__Output__

3  
4  
1  

##### Explanation 
Test Case 1: substring "ab" is a prefix, a suffix and appears 3 times.  
Test Case 2: substring "aaaa" occurs 1 time, substring "aaa" occurs 2 times, substring "aa" occurs 3 times, substring "a" occurs 4 times. All of them are proper prefixes and suffixes. But, "a" has the maximum frequency.  
Test Case 3: "abcdef" is the only substring that is a prefix and suffix. It appears 1 time.  
