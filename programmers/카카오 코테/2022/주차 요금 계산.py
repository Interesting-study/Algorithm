from collections import defaultdict
LAST_TIME = 23*60 + 59

def exchange_mins(rec_time):
    hour, mins = map(int, rec_time.split(':'))
    return hour*60 + mins

def solution(fees, records):
    answer = []
    in_time = defaultdict(int)

    for record in records:
        rec_split = record.split() #시간, 차번호, 입출차
        car = int(rec_split[1])

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))