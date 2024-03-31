import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
score_table = []

for _ in range(n):
    score_table.append(list(map(int, sys.stdin.readline().split())))


def divide_2groups(level, last_num):
    global n

    if level == n / 2:
        return [[i] for i in range(last_num + 1, n + 1)]

    temp_list = []
    for i in range(last_num + 1, n // 2 + level + 1):
        for ele_list in divide_2groups(level + 1, i):
            ele_list = [i] + ele_list
            temp_list.append(ele_list)

    return temp_list


def get_group_score(group):
    score = 0
    for i in range(len(group) - 1):
        for j in range(i, len(group)):

            score += score_table[group[i] - 1][group[j] - 1] + score_table[group[j] - 1][group[i] - 1]

    return score


groups = divide_2groups(1, 0)
group_list = []
for i in range(len(groups) // 2):
    group_list.append([groups[i], groups[len(groups) - i - 1]])

answer = 100 * n
for group1, group2 in group_list:
    # print(f"group1: {group1} - score: {get_group_score(group1)}")
    # print(f"group2: {group2} - score: {get_group_score(group2)}")
    answer = min(answer, abs(get_group_score(group1) - get_group_score(group2)))

print(answer)
