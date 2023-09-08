def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    return dfs(begin, target, words, 0)

def get_next_words(curr, words):
    next_words = []
    for word in words:
        count = 0
        for i in range(len(curr)):
            if word[i] != curr[i]:
                count += 1
        if count == 1:
            next_words.append(word)
            
    return next_words

def dfs(curr, target, words, count):
    # end
    if curr == target:
        return count
    
    # action
    next_words = get_next_words(curr, words)
    
    # next
    min_count = 50
    for next_word in next_words:
        new_words = [word for word in words if word != next_word]
        res_count = dfs(next_word, target, new_words, count+1)
        min_count = min(res_count, min_count)
        
    return min_count