from collections import deque


def solution(plans):
    answer = []
    
    plans = deque(sorted(plans, key=lambda x: time_str2int(x[1])))
    pause_plans = deque()
    curr_time = time_str2int(plans[0][1])
    curr_plan = plans.popleft()
    
    while curr_plan:
        if plans:
            next_plan = plans.popleft()
            next_start_time = time_str2int(next_plan[1])
            # 완료 가능
            if curr_time + int(curr_plan[2]) <= next_start_time:
                answer.append(curr_plan[0])
                curr_time = curr_time + int(curr_plan[2])
                # 멈춰둔 과제 재시작
                if curr_time < next_start_time and pause_plans:
                    curr_plan = pause_plans.pop()
                    plans.appendleft(next_plan)
                # 다음 과제 시작
                else:
                    curr_time = next_start_time
                    curr_plan = next_plan
            # 완료 불가능 - 기존 과제 중지, 새로운 과제 시작
            else:
                curr_plan[2] = str(int(curr_plan[2]) - next_start_time + curr_time)
                pause_plans.append(curr_plan)
                curr_time = next_start_time
                curr_plan = next_plan
                
        else:
            answer.append(curr_plan[0])
            if pause_plans:
                curr_plan = pause_plans.pop()
            else:
                curr_plan = None
    return answer


def time_str2int(time):
    hh_mm = time.split(":")
    return int(hh_mm[0]) * 60 + int(hh_mm[1])