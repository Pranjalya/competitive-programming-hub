import string
import random

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # We have n+1 string
    ans = ''.join(random.choices(string.ascii_lowercase, k = max(a)+5))
    print(ans)
    for i in range(n):
        if a[i]==0:
            ans = ''.join(random.choices(string.ascii_lowercase, k = max(a)+5))
        else:
            ans = ans[:a[i]]+str(''.join(random.choices(string.ascii_lowercase, k = max(a)+5)))
        print(ans)
