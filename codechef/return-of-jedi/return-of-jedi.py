T = int(input())
for _ in range(T):
    H, P = map(int, input().split())
    dead = True
    while(H>0):
        H -= P
        P = P//2
        if H<=0:
            dead=True
            break
        if P<=0:
            print(0)
            dead = False
            break
    if(dead):
        print(1)
