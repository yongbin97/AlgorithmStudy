def solution(s):
    stack = []

    for c in s:
        if len(stack) == 0 or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    return 1 if len(stack) == 0 else 0