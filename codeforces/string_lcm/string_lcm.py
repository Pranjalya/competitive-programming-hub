from math import gcd

def find_lcm(s, t):
    if t * (len(s)//len(t)) == s:
        return s
    factor_t = [t[:i] for i in range(1, len(t)//2+1) if t[:i] * (len(t)//(i)) == t]
    factor_s = [s[:i] for i in range(1, len(s)//2+1) if s[:i] * (len(s)//(i)) == s]
    try:
        common = max(list(set(factor_t).intersection(factor_s)), key=len)
    except:
        return -1
    no_t, no_s = len(t)//len(common), len(s)//len(common)
    lcm = (no_t*no_s)//gcd(no_t, no_s)
    return common * lcm

for _ in range(int(input())):
    first = input()
    second = input()
    s, t = (first, second) if len(first) >= len(second) else (second, first)
    print(find_lcm(s, t))