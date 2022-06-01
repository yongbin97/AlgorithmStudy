import sys
from collections import deque

input_data = sys.stdin.readline()
raser_flag = 0
stick_dq = deque()

answ = 0
for i in input_data:
    if i == "(":
        raser_flag = 1
        stick_dq.append(0) #stick 현재 상황표기

    elif i == ")":
        # raser
        if raser_flag == 1:
            stick_dq.pop()
            answ += len(stick_dq)
        # end of stick
        else:
            answ += stick_dq.pop() + 1
        raser_flag = 0

print(answ)