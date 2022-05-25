import sys

T = int(input())

for i in range(T):
    case = sys.stdin.readline()
    stack = []
    flag = 1
    for element in case:
        if element == "(":
            stack.append(element)
        if element == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                flag = 0
                break
    if len(stack) != 0:
        flag = 0

    if flag == 0:
        print("NO")
    else:
        print("YES")