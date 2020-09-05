t = int(input())

def longestArithSeqLength(a):
    ans, temp = 2, 2
    d = a[1]-a[0]
    for i in range(2, len(a)):
        if(a[i]-a[i-1]==d):
            temp+=1
        else: 
            d = a[i]-a[i-1]
            ans = max(ans, temp)
            temp = 2
    return max(ans, temp)

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print('Case #' + str(_ + 1) +': ' +  str(longestArithSeqLength(a)))