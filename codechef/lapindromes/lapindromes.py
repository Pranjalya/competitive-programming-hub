from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    k = 0 if l%2==0 else 1
    print('YES' if Counter(s[:l//2])==Counter(s[l//2+k:]) else 'NO')