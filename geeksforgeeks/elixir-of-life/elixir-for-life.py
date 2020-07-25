def maxFrequency(Str):
    i = 1
    values = []
    while(1):
        if(Str[:i]==Str[-1*i:]):
            values.append(i)
            break
        i += 1
    if(values[0]==len(Str)):
        return 1
    return max([Str.count(Str[:v]) for v in values])

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        Str = input()
        print(maxFrequency(Str))