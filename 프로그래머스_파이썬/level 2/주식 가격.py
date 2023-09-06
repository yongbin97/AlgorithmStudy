def solution1(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                break
        answer.append(j - i)

    return answer


def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for idx, price in enumerate(prices):
        while stack != [] and stack[-1][1] > price:
            past, _ = stack.pop()
            answer[past] = idx - past
        stack.append([idx, price])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i

    return answer