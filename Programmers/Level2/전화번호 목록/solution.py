def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for index in range(len(phone_book) - 1):
        if phone_book[index] == phone_book[index + 1][:len(phone_book[index])]:
            return False
    return answer