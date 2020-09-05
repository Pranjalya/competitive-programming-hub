Indraneel has to sort the books in his library. His library has one long shelf. His books are numbered 1 through N and he wants to rearrange the books so that they appear in the sequence 1,2,...,N

.

He intends to do this by a sequence of moves. In each move he can pick up any book from the shelf and insert it at a different place in the shelf. Suppose Indraneel has 5

books and they are initially arranged in the order

21453

Indraneel will rearrange this in ascending order by first moving book 1

to the beginning of the shelf to get

12453

Then, moving book 3
to position 3

, he gets

12345

Your task is to write a program to help Indraneel determine the minimum number of moves that are necessary to sort his book shelf.
Input:

The first line of the input will contain a single integer N
indicating the number of books in Indraneel's library. This is followed by a line containing a permutation of 1,2,...,N

indicating the intial state of Indraneel's book-shelf.
Output:

A single integer indicating the minimum number of moves necessary to sort Indraneel's book-shelf.
Constraints:

    1≤N≤200000

.
You may also assume that in 50%
of the inputs, 1≤N≤5000

    .

Sample Input

5
2 1 4 5 3 

Sample Output

2
