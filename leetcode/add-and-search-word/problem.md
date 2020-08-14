<h2><div id="title">Add and Search Word</h2></div>

##### Topic : Data Structure

### Problem Statement

<div id="problem_statement">
Design a data structure that supports the following two operations:  
```
void addWord(word)
bool search(word)
```  
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
</div>

#### Sample

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true