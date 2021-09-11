#https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    camera = -30001
    print(routes)

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))