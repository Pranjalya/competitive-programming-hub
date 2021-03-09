for _ in range(int(input())):
    s = input()
    stack = []
    stack.append(int(s[0]))
    for i in range(1,len(s)):
        if stack[-1] == 0:
            if s[i] == '1':
                stack.append(1)
        else:
            if s[i] == '0':
                stack.append(0)
    print(sum(stack))