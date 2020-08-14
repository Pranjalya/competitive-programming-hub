T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    points = list(map(lambda x: K//x if K/x==K//x else -1 , P))
    if max(points)==-1:
        print(-1)
    else: 
        value, position = min(((b,a) for a,b in enumerate(points) if b>0), default=(None,None))
        print(P[position])