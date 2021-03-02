n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(q):
    t, l = map(int, input().split())
    if t == 1:
        a[l-1] = 1-a[l-1]
    else:
        print(sorted(a, reverse=True)[l-1])