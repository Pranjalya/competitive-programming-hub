def timechange(t, z):
    h, m = map(int, t.split(':'))
    if h == 12:
        h = 12 if z == 'PM' else 0
    else:
        h = h + 12 if z == 'PM' else h
    print(h, m)
    return int("{:02d}".format(h)+"{:02d}".format(m))

for _ in range(int(input())):
    time = input().split()
    p = timechange(time[0], time[1])
    n = int(input())
    ans = ""
    for _ in range(n):
        times = input().split()
        r = "1" if timechange(times[0], times[1]) <= p <= timechange(times[2], times[3]) else "0"
        ans += r
    print(ans)

# for _ in range(int(input())):
    # time = input().split()
    # p = timechange(time[0], time[1])
    # print(p)