from collections import defaultdict

def solution(tickets):
    def dfs(curr, remain):
        if len(remain) == 0:
            return [curr]
        
        next_tickets = [ticket for ticket in remain if ticket[0] == curr]
        
        if len(next_tickets) == 0:
            return 
        else:
            result = []
            for next_ticket in next_tickets:
                idx = remain.index(next_ticket)
                next_remain = remain[:idx] + remain[idx+1:]
                res = dfs(next_ticket[1], remain[:idx] + remain[idx+1:])
                if res is not None:
                    result.append([curr] + res)
            if result:
                return sorted(result)[0]
            else:
                return None
        
    return dfs("ICN", tickets)    
