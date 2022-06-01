import sys
from collections import deque

input_str = sys.stdin.readline().strip()
tag_flag = 0
stk = deque()
answ = ""

for word in input_str:
    if word == "<":
        if len(stk) != 0:
            answ += ''.join(stk)
            stk.clear()
        answ += word
        tag_flag = 1

    elif word == ">":
        answ += word
        tag_flag = 0

    elif tag_flag != 0:
        answ += word

    elif word == " ":
        answ += ''.join(stk) + ' '
        stk.clear()

    else:
        stk.appendleft(word)

if len(stk) != 0:
    answ += ''.join(stk)

print(answ)
