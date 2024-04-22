def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    for idx, genre in enumerate(genres):
        if genre_dict.get(genre) is None:
            genre_dict[genre] = {
                "count": plays[idx],
                "details": {idx: plays[idx]}
            }
        else:
            genre_dict[genre]["count"] += plays[idx]
            genre_dict[genre]["details"][idx] = plays[idx]
            
    for details_info in sorted(genre_dict.values(), key=lambda x: x["count"], reverse=True):
        idx_info = sorted(details_info["details"].items(), key=lambda x: x[1], reverse=True)
        for idx, count in sorted(details_info["details"].items(), key=lambda x: x[1], reverse=True)[:2]:
            answer.append(idx)
    
    return answer

# 장르별 2개씩
# 우선순위
# 1. 많이 재생된 장르
# 2. 많이 재생된 노래
# 3. 고유 번호 낮은 순