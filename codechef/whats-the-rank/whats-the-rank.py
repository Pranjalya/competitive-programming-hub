n = int(input())
pos = []
for _ in range(n):
    a = int(input())
    v = len(pos)
    for i in range(len(pos)):
        if a>pos[i]:
            v=i+1
            pos.insert(i, a)
            break
    if v==0:
        pos.append(a)
        print(len(pos))
    elif v==len(pos):
        pos.append(a)
        print(len(pos))
    else:
        print(v)