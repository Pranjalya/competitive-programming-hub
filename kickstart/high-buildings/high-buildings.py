t = int(input())

def getResult(N,A,B,C):
    array = []
    if not (1 <= C <= N) or (C <= A <= N) or (C <= B <= N):
        return 'IMPOSSIBLE'
    else:
        if (A==B):
            array.append(N)
            array.insert(array.index(N)-1,N)
            array.insert(0,N-1)
            array.insert(len(array),N-2)
            array.insert(0,N-3)
        elif (A>B):
            array.append(N)
            array.insert(array.index(N)-1,N)
            array.insert(0,N-1)
            array.insert(len(array),N-2)
            array.insert(0, N-3)
    return ' '.join(array)

for _ in range(t):
    n, a, b, c = map(int, input().split())
    print('Case #' + str(_ + 1) +': ' +  getResult(n,a,b,c))