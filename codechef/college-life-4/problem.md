<h2><div id="title">College Life 4</h2></div>

### Problem Statement

<div id="problem_statement">
Chef and N−1 more of his friends go to the night canteen. The canteen serves only three items (well, they serve more, but only these three are edible!), which are omelette, chocolate milkshake, and chocolate cake. Their prices are A, B and C respectively.

However, the canteen is about to run out of some ingredients. In particular, they only have E eggs and H chocolate bars left. They need:
- 2 eggs to make an omelette
- 3 chocolate bars for a chocolate milkshake
- 1 egg and 1 chocolate bar for a chocolate cake

Each of the N friends wants to order one item. They can only place an order if the canteen has enough ingredients to prepare all the ordered items. Find the smallest possible total price they have to pay or determine that it is impossible to prepare N items.
</div>

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T
test cases follows.
- The first and only line of each test case contains six space-separated integers N, E, H, A, B and C.

### Output

For each test case, print a single line containing one integer ― the minimum cost of N items, or −1 if it is impossible to prepare N items.

### Constraints

- 1≤T≤2⋅105
- 1≤N≤106
- 0≤E,H≤106
- 1≤A,B,C≤106
- the sum of N over all test cases does not exceed 10^6

#### Sample

3
5 4 4 2 2 2
4 5 5 1 2 3
4 5 5 3 2 1

__O/P__

-1
7
4

__Explanation__ :

- _Example case 1_: The maximum number of items that can be produced using 4 eggs and 4 chocolates is 4, so the answer is −1.
- _Example case 2_: In the optimal solution, the friends should order 2 omelettes, 1 chocolate milkshake and 1 chocolate cake, with cost 1⋅2 + 2⋅1 + 3⋅1 = 7
- _Example case 3_: In the optimal solution, the friends should order 4 chocolate cakes, with cost 1⋅4 = 4.