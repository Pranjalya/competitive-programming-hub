from math import log2
for _ in range(int(input())):
    c = int(input())
    d = int(log2(c)) + 1
    ans = -1
    for i in range(1, 2**(d-1)+1):
        if (c^i < 2**d) and (i * (c^i) > ans):
            ans = i * (c^i)
    print(ans)