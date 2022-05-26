import sys

T = int(sys.stdin.readline())

for i in range(T):
    test_case = sys.stdin.readline().split()
    answ = ""

    for j in test_case:
        word_list = list(j)
        word_list.reverse()
        reverse_word = ''.join(word_list)
        answ += reverse_word + " "

    print(answ)


