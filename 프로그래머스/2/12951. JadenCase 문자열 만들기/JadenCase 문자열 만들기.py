def solution(s):
    answer = ""
    
    for i in range(len(s)):
        if answer and answer[-1].isalnum():
            answer += s[i].lower()
        else:
            answer += s[i].upper()
    
    
    return answer