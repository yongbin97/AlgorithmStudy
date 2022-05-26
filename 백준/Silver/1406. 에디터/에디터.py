import sys

st1 = list(sys.stdin.readline().strip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == "L":
        if st1:
            st2.append(st1.pop())

    elif command[0] == "D":
        if st2:
            st1.append(st2.pop())

    elif command[0] == "B":
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))

# import sys
#
# init_str = sys.stdin.readline().strip()
# command_num = int(sys.stdin.readline())
#
# str_list = list(init_str)
# curr_cursor = len(str_list)
#
# for i in range(command_num):
#     command = list(sys.stdin.readline().split())
#     if command[0] == "L":
#         if curr_cursor > 0:
#             curr_cursor -= 1
#
#     elif command[0] == "D":
#         if curr_cursor < len(str_list):
#             curr_cursor += 1
#
#     elif command[0] == "B":
#         if curr_cursor != 0:
#             del str_list[curr_cursor - 1]
#             curr_cursor -= 1
#     else:
#         str_list.insert(curr_cursor, command[1])
#         curr_cursor += 1
#
# print(''.join(str_list))
# 위 방식에서 insert와 del은 O(n)의 시간복잡도를 가진다.
# 최악의 경우 문자열 최대 길이 * 명령어 최대 개수 =>  100,000 * 500,000 만큼의 시간이 필요하다.
