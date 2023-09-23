import sys


def solution(p_list):
    stack = []
    for p in p_list:
        if p in ["(", "["]:
            stack.append(p)

        elif stack and p in [")", "]"]:
            v = 0
            
            last = stack.pop()
            while stack and isinstance(last, int):
                v += last
                last = stack.pop()

            v = 1 if v == 0 else v
            if p == ")" and last == "(":
                stack.append(2 * v)
            elif p == "]" and last == "[":
                stack.append(3 * v)
            else:
                return 0

        else:
            return 0

    if all(isinstance(s, int) for s in stack):
        return sum(stack)
    else:
        return 0



parentheses = sys.stdin.readline().strip()
print(solution(parentheses))

