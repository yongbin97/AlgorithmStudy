def solution(book_time):
    room = []
    
    for start, end in sorted(book_time):
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        start_time = start_h * 60 + start_m
        end_time = end_h * 60 + end_m + 10
        
        room.sort()
        if len(room) == 0 or room[0] > start_time:
            room.append(end_time)
        else:
            room[0] = end_time
    return len(room)