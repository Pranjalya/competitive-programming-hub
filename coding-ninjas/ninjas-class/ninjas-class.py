t = int(input())


def findFactors(num):
    """
    Function returning a set of all factors of a number
    """
    val = set(
        f for i in range(1, int(num ** 0.5) + 1) if num % i == 0 for f in (i, num // i)
    )
    return val


for _ in range(t):

    N = int(input())
    money = []

    # Get the money by all the studnets
    for __ in range(N):
        v = int(input())
        money.append(v)

    # Find factos and append money accordingly
    for roll in range(N):
        factors = findFactors(roll + 1)
        a = 0
        for f in factors:
            a += money[f - 1]
        print(a, end=" ")
    print()
