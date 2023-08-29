def solution(s):
    zero = 0
    convert = 0

    while s != "1":
        zero += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        convert += 1

    return [convert, zero]