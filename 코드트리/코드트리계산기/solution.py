"""
STEP 1: 준비
N개의 채점기
초기 url: u0
url = domain/problemId (alpha + .)
1 <= problemId <= 10억
N개의 채점기: 1 ~ N번
0초에 우선순위 1인 u0 채점 요청 -> 대기 큐에 들어감


STEP 2: 채점 요청
t초 - 우선순위 p, url: u 채점 요청
=> 대기큐 삽입

if u in 대기 큐  => pass

STEP 3: 채점 시도
t초 -> 대기 큐에서 '채점 가능한 문제' 중 우선순위 가장 높은 task pop
<채점 불가능 조건>
- task 도메인이 진행 중인 도메인 중 하나라면 불가능
- 해당 도메인의 마지막 채점 시작 시간: start, 종료시간: start + gap
    => if t < start + 3 * gap => 불가능

<채점 가능 한 문제 우선순위>
- p가 작을수록
- 대기 큐에 들어온 시간이 빠를수록

t초에 채점 가능한 task가 하나라도 있으면 채점기 중 가장 작은 번호를 가진 채점기에
가장 높은 task에 넣음


STEP 4: 채점 종료
t초 - J_i 채점 종료
    J_i에 채점 중이던 일감이 끝났음을 의미
    => J_i 쉬는 상태

STEP 5: 대기큐 조회
t 초에 채점 대기 큐에 있는 채점 task수 출력
"""
import sys
import heapq
import time
from collections import OrderedDict, defaultdict
from typing import Optional


class Task:
    def __init__(self, t, p, url):
        self.domain = url.split("/")[0]
        self.id = url.split("/")[1]
        self.p = p
        self.t = t

    def __lt__(self, other):
        if self.p != other.p:
            return self.p < other.p
        return self.t < other.t

    def __repr__(self):
        return f"{self.domain}/{self.id}"


# 채점기 정보 {J_id: Task}
J_dict = OrderedDict()
# 대기 큐 Priority Queue (Task) dict
domain_wait_q = defaultdict(list)
# 대기 큐 안에 있는 url dict {url: T/F}
wait_q_url_dict = defaultdict(bool)
# 도메인 시간 정보 {domain: {start: int, end: int}}
domain_time_dict = defaultdict(dict)
# 현재 채점 중인 도메인 리스트 {domain: T/F}
domain_judging_dict = defaultdict(bool)


def set_j(input_data):
    """
    Step 1
    input_data: [N, u0]
    채점기 세팅
    u0 wait Q에 넣기
    """
    N = int(input_data[0])
    u = input_data[1]
    for i in range(1, N + 1):
        J_dict[i] = None
    heapq.heappush(domain_wait_q[u.split("/")[0]], Task(0, 1, u))
    # domain_time_dict[u.split("/")[0]] = {"start": 0, "gap": 0}
    wait_q_url_dict[u] = True


def insert_task_wait_q(input_data):
    """
    step 2
    input_data = [t, p ,u]
    waitQ에 새로운 task 넣기
    """
    t, p = map(int, input_data[:2])
    u = input_data[2]
    if not wait_q_url_dict[u]:
        heapq.heappush(domain_wait_q[u.split("/")[0]], Task(t, p, u))
        # domain_time_dict[u.split("/")[0]] = {"start": 0, "gap": 0}
        wait_q_url_dict[u] = True
        # print(f"new_task insert: {u}")


def pop_task_wait_q(t) -> Optional[Task]:
    task_tmp_list = []

    for domain, pq in domain_wait_q.items():
        if not domain_judging_dict[domain] and domain_wait_q[domain]:
            curr_domain_time = domain_time_dict.get(domain, {"start": 0, "gap": 0})
            if curr_domain_time["start"] + 3 * curr_domain_time["gap"] <= t:
                heapq.heappush(task_tmp_list, heapq.heappop(domain_wait_q[domain]))

    if task_tmp_list:
        task = heapq.heappop(task_tmp_list)
        for tmp in task_tmp_list:
            heapq.heappush(domain_wait_q[tmp.domain], tmp)
        return task
    else:
        return None


def try_task(input_data):
    """
    step 3
    input_data = [t]
    """
    t = int(input_data[0])

    j_id = None
    for i, v in J_dict.items():
        if v is None:
            j_id = i
            break

    if j_id is not None:
        task: Optional[Task] = pop_task_wait_q(t)
        if task is not None:
            J_dict[j_id] = task
            domain_judging_dict[task.domain] = True
            domain_time_dict[task.domain]["start"] = t
            wait_q_url_dict[f"{task.domain}/{task.id}"] = False
            # print(f"{task.domain}/{task.id} start")


def end_task(input_data):
    """
    step 4
    input_data = [t J_id]
    """
    t, j_id = map(int, input_data)
    if J_dict[j_id] is not None:
        task = J_dict[j_id]
        J_dict[j_id] = None
        domain_judging_dict[task.domain] = False
        domain_time_dict[task.domain]["gap"] = t - domain_time_dict[task.domain]["start"]
        # print(f"{task.domain}/{task.id} done")


def print_wait_q():
    """
    step5
    """
    answer = 0
    for v in domain_wait_q.values():
        answer += len(v)
    print(answer)



sys.stdin = open("/Users/yongbin/Desktop/developer/Algorithm_Study/코드트리/코드트리계산기/input2.txt", "r")
start = time.time()
Q = int(sys.stdin.readline())
for _ in range(Q):
    query, *data = sys.stdin.readline().split()
    # print(query, data)

    # 100 N u0
    if int(query) == 100:
        set_j(data)

    # 200 t p u
    elif int(query) == 200:
        insert_task_wait_q(data)

    # 300 t
    elif int(query) == 300:
        try_task(data)

    # 400 t J_id
    elif int(query) == 400:
        end_task(data)

    else:
        # 500 t
        print_wait_q()
        # print(sum(len(domain_wait_q.values())))
    # print(f"J_dict: {J_dict}, wait_q: {wait_q}")
    # print(domain_wait_q)
print(f"time: {time.time()-start}")