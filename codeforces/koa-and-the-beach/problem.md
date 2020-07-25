 The only difference between easy and hard versions is on constraints. In this version constraints are lower. You can make hacks only if all versions of the problem are solved.

Koa the Koala is at the beach!

The beach consists (from left to right) of a shore, n+1
meters of sea and an island at n+1

meters from the shore.

She measured the depth of the sea at 1,2,…,n
meters from the shore and saved them in array d. di denotes the depth of the sea at i meters from the shore for 1≤i≤n

.

Like any beach this one has tide, the intensity of the tide is measured by parameter k
and affects all depths from the beginning at time t=0

in the following way:

    For a total of k

seconds, each second, tide increases all depths by 1
.

Then, for a total of k
seconds, each second, tide decreases all depths by 1
.

This process repeats again and again (ie. depths increase for k
seconds then decrease for k seconds and so on ...).

Formally, let's define 0
-indexed array p=[0,1,2,…,k−2,k−1,k,k−1,k−2,…,2,1] of length 2k. At time t (0≤t) depth at i meters from the shore equals di+p[tmod2k] (tmod2k denotes the remainder of the division of t by 2k

    ). Note that the changes occur instantaneously after each second, see the notes for better understanding. 

At time t=0
Koa is standing at the shore and wants to get to the island. Suppose that at some time t (0≤t) she is at x (0≤x≤n

) meters from the shore:

    In one second Koa can swim 1

meter further from the shore (x changes to x+1) or not swim at all (x stays the same), in both cases t changes to t+1
.

As Koa is a bad swimmer, the depth of the sea at the point where she is can't exceed l
at integer points of time (or she will drown). More formally, if Koa is at x (1≤x≤n) meters from the shore at the moment t (for some integer t≥0), the depth of the sea at this point  — dx+p[tmod2k]  — can't exceed l. In other words, dx+p[tmod2k]≤l
must hold always.

Once Koa reaches the island at n+1

    meters from the shore, she stops and can rest.

    Note that while Koa swims tide doesn't have effect on her (ie. she can't drown while swimming). Note that Koa can choose to stay on the shore for as long as she needs and neither the shore or the island are affected by the tide (they are solid ground and she won't drown there). 

Koa wants to know whether she can go from the shore to the island. Help her!
Input

The first line of the input contains one integer t
(1≤t≤100

)  — the number of test cases. Description of the test cases follows.

The first line of each test case contains three integers n
, k and l (1≤n≤100;1≤k≤100;1≤l≤100) — the number of meters of sea Koa measured and parameters k and l

.

The second line of each test case contains n
integers d1,d2,…,dn (0≤di≤100

)  — the depths of each meter of sea Koa measured.

It is guaranteed that the sum of n
over all test cases does not exceed 100

.
Output

For each test case:

Print Yes if Koa can get from the shore to the island, and No otherwise.

You may print each letter in any case (upper or lower).
Example
Input
Copy

7
2 1 1
1 0
5 2 3
1 2 3 2 2
4 3 4
0 2 4 3
2 3 5
3 0
7 2 3
3 0 2 1 3 0 1
7 1 4
4 4 3 0 2 4 2
5 2 3
1 2 3 2 2

Output
Copy

Yes
No
Yes
Yes
Yes
No
No

Note

In the following s
denotes the shore, i denotes the island, x denotes distance from Koa to the shore, the underline denotes the position of Koa, and values in the array below denote current depths, affected by tide, at 1,2,…,n

meters from the shore.

In test case 1
we have n=2,k=1,l=1,p=[0,1]

.

Koa wants to go from shore (at x=0
) to the island (at x=3

). Let's describe a possible solution:

    Initially at t=0

the beach looks like this: [s–,1,0,i]
.
At t=0
if Koa would decide to swim to x=1, beach would look like: [s,2–,1,i] at t=1, since 2>1 she would drown. So Koa waits 1 second instead and beach looks like [s–,2,1,i] at t=1
.
At t=1
Koa swims to x=1, beach looks like [s,1–,0,i] at t=2. Koa doesn't drown because 1≤1
.
At t=2
Koa swims to x=2, beach looks like [s,2,1–,i] at t=3. Koa doesn't drown because 1≤1
.
At t=3
Koa swims to x=3, beach looks like [s,1,0,i–] at t=4
.
At t=4
Koa is at x=3

    and she made it! 

We can show that in test case 2
Koa can't get to the island.