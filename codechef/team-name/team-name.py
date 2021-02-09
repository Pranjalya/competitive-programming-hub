from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = input().split()

    tails = defaultdict(list)

    for w in s:
        tails[w[1:]].append(w[0])

    keys = list(tails.keys())
    ans = 0

    for i in range(len(tails)):
        for j in range(i+1, len(tails)):
            distinct = len(set(tails[keys[i]] + tails[keys[j]]))
            ans += (distinct - len(tails[keys[i]])) * (distinct - len(tails[keys[j]]))

    print(2 * ans)
