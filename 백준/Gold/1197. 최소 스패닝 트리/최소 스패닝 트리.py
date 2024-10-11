import sys


# Solution
def build_tree():
    global total_weight
    tree_edges = []

    for edge in edges:
        u, v, w = edge

        u_root = find_root(u)
        v_root = find_root(v)

        if u_root == v_root:
            continue
        else:
            union_tree(u_root, v_root)
            tree_edges.append(edge)
            total_weight += w

        if len(tree_edges) == V - 1:
            break


def find_root(x):
    if parent[x] == 0 or parent[x] == x:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]


def union_tree(a_root, b_root):
    parent[b_root] = a_root
    parent[a_root] = a_root


# Main
V, E = map(int, sys.stdin.readline().split())
edges = []
parent = [0] * (V + 1)
total_weight = 0
v_cnt = 0

# get edges
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append([u, v, w])

edges.sort(key=lambda x: x[2])
build_tree()
print(total_weight)
