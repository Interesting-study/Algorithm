def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
        
    return True

#https://programmers.co.kr/learn/courses/30/lessons/42577
