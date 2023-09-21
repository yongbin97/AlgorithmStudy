import sys


def is_vps(ps):
    st = []
    for p in ps:
        if p == "(":
            st.append(p)
        else:
            if len(st) == 0:
                return "NO"
            else:
                st.pop()

    return "NO" if len(st) else "YES"

N = int(sys.stdin.readline())

for _ in range(N):
    print(is_vps(sys.stdin.readline().strip()))



