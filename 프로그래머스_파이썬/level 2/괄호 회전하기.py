from collections import deque


def solution(s):
    if len(s) % 2 == 1:
        return 0

    answer = 0
    dq = deque(s)
    dq_length = len(dq)

    for _ in range(dq_length):
        stack = []
        flag = True

        for c in dq:
            if c in ["(", "{", "["]:
                stack.append(c)

            else:
                if len(stack) == 0:
                    flag = False
                    break

                peek = stack.pop()
                if not (
                        peek == "(" and c == ")"
                        or peek == "{" and c == "}"
                        or peek == "[" and c == "]"
                ):
                    flag = False
                    break

        if flag:
            answer += 1
        dq.append(dq.popleft())
    return answer
