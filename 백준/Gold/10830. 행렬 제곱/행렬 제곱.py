import sys


def print_arrangement(arr):
    for row in arr:
        print(*row)


def multiply(base, arr):
    new_base = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_base[i][j] = (new_base[i][j] + base[i][k] * arr[k][j]) % 1000

    return new_base


def square(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    tmp = square(A, B//2)
    if B % 2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(tmp, tmp), A)


N, B = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

answer = square(A, B)
print_arrangement(answer)
