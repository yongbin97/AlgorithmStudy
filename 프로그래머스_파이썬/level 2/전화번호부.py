def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    for idx in range(len(sorted_phone_book) - 1):
        prefix = sorted_phone_book[idx]
        word = sorted_phone_book[idx + 1]
        if word.startswith(prefix):
            return False

    return True