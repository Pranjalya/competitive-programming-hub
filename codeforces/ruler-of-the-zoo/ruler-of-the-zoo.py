n = int(input())
s = {}
s[0], s[1], s[2] = [], [], []
for i in range(n):
    i, j, k = map(input().split())
    s[0].append(i)
    s[1].append(j)
    s[2].append(k)

q = list(range(n))
k = q[0]
c = 0

def solve(n, A, B, C):
    st = s[c][q[0]]
    if st > s[0][q[1]]:
        c += 1
        p = q.pop(1)
        q.append(p)
        st = s[c][q[1]]
        if st > s[0][q[2]]:
            c += 1
            p = q.pop(1)
            q.append(p)




print(solve(n,A,B,C))