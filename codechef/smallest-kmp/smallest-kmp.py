from collections import Counter
T = int(input())
for _ in range(T):
    S = input()
    P = input()
    SC, PC = Counter(S), Counter(P)
    sub = SC-PC
    sleft, sright = "", ""
    for letter in sorted(sub.keys()):
        if(letter <= P[0]):
            sleft += letter*sub[letter]
        elif(letter > P[0]):
            sright += letter*sub[letter]
    ans = sleft+P+sright
    sleft, sright = "", ""
    for letter in sorted(sub.keys()):
        if(letter < P[0]):
            sleft += letter*sub[letter]
        elif(letter >= P[0]):
            sright += letter*sub[letter]
    ans2 = sleft+P+sright
    print(min(ans, ans2))