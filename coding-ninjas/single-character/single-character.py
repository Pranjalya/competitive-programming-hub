from collections import Counter

t = int(input())

for _ in range(t):
    string = input()

    # Create a counter dictionary of strings
    count = Counter(string)
    count = dict(count)

    # Get the maximum item
    maxim = max(count.items(), key=lambda x: x[1])
    all = list()

    # Get all the keys with the same count as that of maximum
    for key, value in count.items():
        if value == maxim[1] and key <= maxim[0]:
            all.append(key)

    # Lexographically sort the list
    all = sorted(all)

    # Print the answer
    print(all[0] * count[all[0]])
