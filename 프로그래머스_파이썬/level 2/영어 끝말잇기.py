def solution(n, words):
    word_list = []
    end = -1
    for idx, word in enumerate(words):
        # 종료 조건 1: 한 글자
        if len(word) == 1:
            end = idx
            break

        # 종료 조건 2: 중복 단어
        if word in word_list:
            end = idx
            break

        # 종료 조건 3: 끝말잇기 X
        if idx > 0 and words[idx - 1][-1] != word[0]:
            end = idx
            break

        word_list.append(word)

    return [0, 0] if end == -1 else [idx % n + 1, idx // n + 1]