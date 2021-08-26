answer = []

def dfs(parents, earn, index):
    global answer

    if parents[index] == index or earn // 10 == 0:
        answer[index] += earn
        return

    send = earn // 10
    mine = earn - send
    answer[index] += mine

    dfs(parents, send, parents[index])

    return

def solution(enroll, referral, seller, amount):
    global answer
    length = len(enroll)
    name_index = {}
    answer = [0] * (length + 1)
    parents = [i for i in range(length + 1)]

    # 멤버별 받는 돈 초기화, 아래에서부터 올라가는 dfs 구현
    for i in range(length):
        name_index[enroll[i]] = i + 1

    # 추천인 입력 (부모노드 입력), 0이 민호
    for i in range(length):
        if referral[i] == '-':
            parents[i + 1] = 0
        else:
            parents[i + 1] = name_index[referral[i]]

    for i in range(len(seller)):
        dfs(parents, amount[i] * 100, name_index[seller[i]])

    return answer[1:]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]), end='\n\n')

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))