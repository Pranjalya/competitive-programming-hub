A time is a string in the format "HH:MM AM" or "HH:MM PM" (without quotes), where HH and MM are always two-digit numbers. A day starts at 12:00 AM and ends at 11:59 PM. You may refer here for understanding the 12-hour clock format.

Chef has scheduled a meeting with his friends at a time P
. He has N friends (numbered 1 through N); for each valid i, the i-th friend is available from a time Li to a time Ri (both inclusive). For each friend, can you help Chef find out if this friend will be able to attend the meeting? More formally, check if Li≤P≤Ri for each valid i



Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T
test cases follows.

The first line of each test case contains a single time P. The second line contains a single integer N. N lines follow. For each valid i, the i-th of these lines contains two space-separated times Li and Ri.



Output

For each test case, print a single line containing one string with length N.

For each valid i, the i-th character of this string should be '1' if i-th friend will be able to attend the meeting or '0' otherwise.



Constraints

- 1≤T≤500
- 1≤N≤500 each time is valid in the 12-hour clock format for each valid i, the time Ri is greater or equal to Li