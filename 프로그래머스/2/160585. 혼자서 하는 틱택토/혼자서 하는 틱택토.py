def is_success(OX_list):
    if len(OX_list) < 3:
        return False
    
    row_count = [0, 0, 0]
    col_count = [0, 0, 0]
    diag_count = [0, 0]
    
    for r, c in OX_list:
        row_count[r] += 1
        col_count[c] += 1
        if r == c:
            diag_count[0] += 1
        if r + c == 2:
            diag_count[1] += 1
    
    if 3 in row_count or 3 in col_count or 3 in diag_count:
        return True
    else:
        return False
    

def solution(board):
    O_list = []
    X_list = []
    for r_idx, row in enumerate(board):
        for c_idx, col in enumerate(row.strip()):
            if col == "O":
                O_list.append([r_idx, c_idx])
            elif col == "X":
                X_list.append([r_idx, c_idx])
                
    if len(O_list) - len(X_list) not in [0, 1]:
        return 0
    else:
        if (
            is_success(O_list) and len(O_list) - 1 != len(X_list)
            or is_success(X_list) and len(O_list) != len(X_list)
        ):
            return 0
    return 1
    