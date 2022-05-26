import sys

n = int(sys.stdin.readline())

input_list = list()
st = list()
answ = list()
pop_push_list = ""

for i in range(n):
    ele = int(sys.stdin.readline())
    input_list.append(ele)

target_idx = 0

for i in range(n):
    st.append(i + 1)
    pop_push_list += "+\n"

    while st[-1] == input_list[target_idx]:
        target = st.pop()
        pop_push_list += "-\n"
        answ.append(target)
        target_idx += 1
        if len(st) == 0:
            break

if answ == input_list:
    print(pop_push_list)
else:
    print("NO")
