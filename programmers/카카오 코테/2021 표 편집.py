#https://programmers.co.kr/learn/courses/30/lessons/81303
#cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다. = 링크드 리스트 이용

def solution(n, k, cmd):
    #삭제되지 않은 건 1, 삭제된 건 0
    table = {i: [i-1, i+1] for i in range(1, n+1)}
    status = ["O" for _ in range(n)]
    stack = []
    k += 1

    for c in cmd:
        c = c.split()

        if c[0] == "U":
            for _ in range(int(c[1])):
                k = table[k][0]

        elif c[0] == "D":
            for _ in range(int(c[1])):
                k = table[k][1]

        elif c[0] == "C":
            prev, next = table[k]
            stack.append([prev, next, k])
            status[k - 1] = "X"

            #끝이면 바로 전
            if next == n + 1:
                k = table[k][0]
            else:
                k = table[k][1]

            if prev == 0:
                table[next][0] = prev
            elif next == n + 1:
                table[prev][1] = next
            else:
                table[prev][1] = next
                table[next][0] = prev


        elif c[0] == "Z":
            prev, next, now = stack.pop()
            status[now - 1] = 'O'

            if prev == 0:
                table[next][0] = now
            elif next == n + 1:
                table[prev][1] = now
            else:
                table[prev][1] = now
                table[next][0] = now

    return "".join(status)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))