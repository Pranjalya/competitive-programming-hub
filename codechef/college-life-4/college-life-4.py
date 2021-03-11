def solve(n,e,h,a,b,c):
    # O = 2 E
    # CM = 3 CB
    # CC = 1 E + 1 CB
    # min = min((N E + N CB),(2*N E), (3*N CB))
    pos = 0
    if (e >= n and h >= n): pos += 1
    if (e >= 2*n):  pos += 2
    if (h >= 3*n):  pos += 4
    if pos == 0:    return -1



for _ in range(int(input())):
    n, e, h, a, b, c = map(int, input().split())
    print(solve(n,e,h,a,b,c))