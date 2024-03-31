import sys

n = int(sys.stdin.readline())
rest_customer_count = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())

answer = n

for cust_count in rest_customer_count:
    if cust_count - a > 0:
        answer += (cust_count - a) // b
        if (cust_count - a) % b > 0:
            answer += 1

print(answer)

