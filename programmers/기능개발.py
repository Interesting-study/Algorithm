from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    
    while progresses[0] < 100 or progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            print(progresses)
