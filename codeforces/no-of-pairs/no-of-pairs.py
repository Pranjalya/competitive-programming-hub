from math import gcd

f = lambda a, b, c, d: c*a*b/gcd(a,b) - d*gcd(a,b)

for _ in range(int(input())):
	c, d, x = map(int, input().split())

