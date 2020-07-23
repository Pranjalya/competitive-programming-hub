T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # Since 1111...N times = (10^N-1)/9
    # Using inbuilt function of python
    no = pow(10, N, 9*M)-1
    print(no//9 % M)