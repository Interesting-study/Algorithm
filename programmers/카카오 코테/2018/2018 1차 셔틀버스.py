#https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    timetable = [int(tt[:2]) * 60 + int(tt[3:]) for tt in timetable]
    timetable.sort()
    last_time = (60 * 9) + (n - 1) * t

    for i in range(n):
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        if i == n - 1:  # 마지막 배차일 경우
            if timetable[0] <= last_time:  # timetable에 마지막 배차 때 우선순위가 높은 크루가 있다면
                last_time = timetable[m - 1] - 1  # 마지막 탑승자보다 1초 빠르게 한다
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        for j in range(m - 1, -1, -1):  # del로 인한 index 변화에 영향을 주지 않기위해서 거꾸로 반복
            bus_arrive = (60 * 9) + i * t  # 다음 배차 시간 (분단위)
            if timetable[j] <= bus_arrive:  # 다음 배차시간보다 작거나 같은 시간을 가진 timetable 요소를 삭제
                del timetable[j]  # timetable에서 다음 배차를 못하는 크루를 삭제



print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))