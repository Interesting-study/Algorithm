#https://programmers.co.kr/learn/courses/30/lessons/86048
from collections import defaultdict, deque


def solution(enter, leave):
    answer = defaultdict(int)
    current_room = []
    enter = deque(enter)
    leave = deque(leave)
    meet_check = defaultdict(int)

    while enter:
        entered_person = enter.popleft()

        for now in current_room:
            meet_check[now] += 1

        # 지금 들어온 사람은 현재 있는 방에 있는 사람과 전부 만난다.
        meet_check[entered_person] = len(current_room)
        current_room.append(entered_person)

        for _ in range(len(current_room)):
            # 퇴실명부에 있으면 퇴실처리
            if leave[0] in current_room:
                current_room.remove(leave.popleft())
            else:
                break

    return [meet_check[idx] for idx in sorted(meet_check.keys(), key=lambda x: x)]