from collections import Counter

def solution(topping):
    answer = 0
    # 동일한 가짓수의 토핑이 올라가게
    g1, g2 = Counter(topping), set()
    for top in topping:
        g1[top] -= 1
        g2.add(top)
        
        if g1[top] == 0:
            del g1[top]
        if len(g1) == len(g2):
            answer += 1
    
    return answer