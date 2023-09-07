import heapq


def solution(jobs):
    answer, time = 0, 0
    total_jobs = len(jobs)
    while len(jobs) > 0:
        ready_queue = sorted([job for job in jobs if job[0] <= time], key=lambda x: x[1])
        if len(ready_queue) == 0:
            time += 1
            continue

        job = ready_queue[0]
        time += job[1]
        answer += time - job[0]
        jobs.remove(job)

    return answer // total_jobs