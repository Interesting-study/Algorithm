import heapq

INF = int(1e9)
def FIFO(pay, amount):
    total = 0
    while amount >= 0:
        rec = heapq.heappop(pay)[1]
        price, quantity = rec[0], rec[1]

        if quantity >= amount:
            total += (price * amount)
            return total
        else:
            total += (price * quantity)
            amount -= quantity

def FILO(pay, amount, total):
    while amount > 0:
        rec = heapq.heappop(pay)
        idx = rec[0]
        price, quantity = rec[1][0], rec[1][1]

        if quantity <= amount:
            total += (price * quantity)
            amount -= quantity
        else:
            total += (price * amount)
            quantity -= amount
            amount = 0
            heapq.heappush(pay, (idx, [price, quantity]))

    return pay, total



def solution(record):
    FIFO_pay = []
    FILO_pay = []

    sell = []
    sell_amount = 0

    FILO_total = 0
    length = len(record)

    for idx in range(len(record)):
        new_rec = record[idx].split()

        if new_rec[0] == 'P':
            heapq.heappush(FIFO_pay, (idx, list(map(int, new_rec[1:]))))
            heapq.heappush(FILO_pay, (-idx, list(map(int, new_rec[1:]))))
        elif new_rec[0] == 'S':
            heapq.heappush(sell, (idx, list(map(int, new_rec[1:]))))
            sell_amount += int(new_rec[-1])
            FILO_pay, FILO_total = FILO(FILO_pay, int(new_rec[-1]), FILO_total)

    answer = []
    answer.append(FIFO(FIFO_pay, sell_amount))
    answer.append(FILO_total)

    return answer

print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]))
print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]))
print(solution(["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]))

'''
개인 피드백 : 다 구해놓고, 복잡하게 생각함. 
후입선출 그대로 판매가 이뤄질때마다 계산하면 됐었음. 문제 그대로 해석하고 구현하도록 할 것
'''