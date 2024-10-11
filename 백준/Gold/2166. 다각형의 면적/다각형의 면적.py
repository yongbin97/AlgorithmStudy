import sys


# solution
def get_area():
    total = 0
    for i in range(N):
        if i == N - 1:
            total += (x_list[i] * y_list[0] - x_list[0] * y_list[i])
        else:
            total += (x_list[i] * y_list[i + 1] - x_list[i + 1] * y_list[i])

    return abs(total) / 2


# main
N = int(sys.stdin.readline().strip())

x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

print(get_area())
