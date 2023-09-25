import sys


exp = sys.stdin.readline().strip()
answer = set()

def dfs(idx, stack, expression):
    # end condition
    if idx >= len(exp):
        if expression != exp:
            answer.add(expression)
        return

    curr = exp[idx]

    if curr == "(":
        # ( 제외
        stack_1 = stack + [False]
        dfs(idx+1, stack_1, expression)

        # ( 포함
        stack_2 = stack + [True]
        expression += curr
        dfs(idx+1, stack_2, expression)

    else:
        if curr == ")":
            if stack.pop():
                expression += curr

        else:
            expression += curr

        dfs(idx+1, stack, expression)


dfs(0, [], "")
for e in sorted(answer):
    print(e)
