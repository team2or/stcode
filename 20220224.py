#전화번호 목록
def solution(phone_book):
    if len(phone_book)==1:
        return True
    phone_book.sort()
    for number in phone_book:
        for i in phone_book:
            if number==i:
                pass
            elif len(number)<len(i):
                if i[:len(number)] ==number:
                    return False
    return True 
    
#효율성 3,4
 

      
import heapq

def solution(phone_book):
    heapq.heapify(phone_book)
    f_number=heapq.heappop(phone_book)
    while phone_book:
        if f_number==phone_book[0][:len(f_number)]:
             return False
        f_number=heapq.heappop(phone_book)
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True 