def solve(a, n):
    ans = 0
    i, k = a[0], a[-1]
    for j in a:
        ans = max(ans, abs(i-j)+abs(j-k)+abs(k-i))
    return ans

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(sorted(a), n))