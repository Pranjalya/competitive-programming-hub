<h2><div id="title">No Time To Wait</h2></div>

### Problem Statement

<div id="problem_statement">
Only x hours are left for the March Long Challenge and Chef is only left with the last problem unsolved. However, he is sure that he cannot solve the problem in the remaining time. From experience, he figures out that he needs exactly H hours to solve the problem.

Now Chef finally decides to use his special power which he has gained through years of intense yoga. He can travel back in time when he concentrates. Specifically, his power allows him to travel to N different time zones, which are T1,T2,…,TN hours respectively behind his current time.

Find out whether Chef can use one of the available time zones to solve the problem and submit it before the contest ends.
</div>

### Input

- The first line of the input contains three space-separated integers N, H and x
- The second line contains N space-separated integers T1,T2,…,TN.

### Output

Print a single line containing the string "YES" if Chef can solve the problem on time or "NO" if he cannot.

### Constraints

- 1≤N≤100
- 1≤x<H≤100
- 1≤Ti≤100 for each valid i

#### Sample

2 5 3
1 2

__O/P__

Yes

__Explanation__

Chef already has 3 hours left. He can go to the 2-nd time zone, which is 2 hours back in time. Then he has a total of 3+2=5 hours, which is sufficient to solve the problem.