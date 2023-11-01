import sys

while True:
    edges = list(map(int, sys.stdin.readline().split()))

    if all(edge == 0 for edge in edges):
        break

    edges.sort(reverse=True)

    if edges[0] >= edges[1] + edges[2]:
        print("Invalid")

    elif edges[0] == edges[2]:
        print("Equilateral")

    elif edges[0] == edges[1] or edges[1] == edges[2]:
        print("Isosceles")

    else:
        print("Scalene")



