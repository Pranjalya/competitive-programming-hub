t = int(input())

sum_sq = lambda n : n*(n+1)*(2*n+1)/6

for _ in range(t):
    X = int(input())
    start, end = 1, X
    mid_prev, mid = end, start

    # Binary search for the value
    while(mid_prev!=mid or (mid<X<mid_prev) or (mid>X>mid_prev)):
        if(X==sum_sq(mid)):
            break
        if(X<sum_sq(mid)):
            mid_prev = mid
            end = mid
            mid = (start+end)//2
        elif(X>sum_sq(mid)):
            mid_prev = mid
            start = mid
            mid = (start+end)//2
    print(mid)
