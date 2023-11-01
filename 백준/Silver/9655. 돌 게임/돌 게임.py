import sys

N = int(sys.stdin.readline())

x = N // 3
remain = N % 3

if x % 2 == 0:
    if remain % 2 == 0:
        print("CY")
    else:
        print("SK")

else:
    if remain % 2 == 0:
        print("SK")
    else:
        print("CY")
