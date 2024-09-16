import sys


# 피사노 주기
n = int(sys.stdin.readline())
mod = 1000000
p = 15 * mod // 10

fibo_list = [0, 1]
for i in range(2, p):
    fibo_list.append((fibo_list[i - 1] + fibo_list[i - 2]) % mod)

print(fibo_list[n % p])
