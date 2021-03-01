# Ruler of the Zoo

After realizing that Zookeeper is just a duck, the animals have overthrown Zookeeper. They now have to decide a new ruler among themselves through a fighting tournament of the following format:

- Initially, animal[0] is king, while everyone else queues up with animal[1] at the front of the queue and animal[n−1] at the back.
- The animal at the front of the queue will challenge the king to a fight, and the animal with greater strength will win the fight.
- The winner will become king, while the loser joins the back of the queue.

An animal who wins 3 times consecutively will be crowned ruler for the whole zoo. The strength of each animal depends on how many consecutive fights he won. Animal[i] has strength A[i] with 0 consecutive win, B[i] with 1 consecutive win, and C[i] with 2 consecutive wins. Initially, everyone has 0 consecutive win.

For all animals, Ai>Bi and Ci>Bi. Also, the values of Ai, Bi, Ci are distinct (all 3n values are pairwise different).

In other words, an animal who is not a king has strength Ai. A king usually has a strength of Bi or Ci. The exception is on the first turn, the first king (animal 0) has strength Ai.

Who is the new ruler, and after how many fights? Or will it end up that animals fight forever with no one ending up as ruler?

## Input

The first line contains one integer n (4≤n≤6000) — number of the animals.

i-th of the next n lines contains 3 integers Ai, Bi and Ci (0≤Ai,Bi,Ci≤109).

It is guaranteed that Ai>Bi and Ci>Bi, and that all values of Ai, Bi and Ci are distinct.

## Output

Output two integers in a single line. The first is the index of the animal that will become ruler, and the second is the number of fights passed until some animal becomes the ruler.

If the animals will fight for infinitely long, output -1 -1 instead.

## Example

- Input

4
5 1 2
10 8 11
9 0 3
7 4 6

- Output

-1 -1

- Input

5
11 7 12
8 6 14
2 1 10
13 0 9
5 3 4

- Output

1 7