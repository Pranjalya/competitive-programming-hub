n, h, x = map(int, input().split())
t = list(map(int, input().split()))

def solve(h, x, t):
    if h <= x:
        return "YES"
    for ti in t:
        if ti + x >= h:
            return "YES"
    return "NO"

print(solve(h, x, t))