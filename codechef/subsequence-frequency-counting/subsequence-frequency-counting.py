from collections import Counter, defaultdict
from itertools import combinations
mod = 10**9+7
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = defaultdict(lambda : 0)
    for i in range(1, N+1):
        for perm in combinations(A, i):
            v = Counter(perm).most_common(1)[0][0]
            ans[v] = (ans[v]%mod + 1)%mod
    for i in range(1, N+1):
        print(ans[i], end=' ')
    print()
    count = Counter(A)