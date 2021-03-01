mod = 998244353

n = int(input())
a = list(map(int, input().split()))
q = int(input())

def solve(m):
    bits = 0
    for i in range(n):
        bits |= a[i]
    return bits * pow(2, m-1, mod)

for _ in range(q):
    print(solve(int(input())))