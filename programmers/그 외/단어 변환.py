#https://programmers.co.kr/learn/courses/30/lessons/43163
def dfs(visited, begin, target, words):
    answer = 0
    stack = [begin]

    while stack:

        now = stack.pop()

        if now == target:
            return answer

        for w in range(len(words)):
            cnt = 0
            for idx in range(len(words[w])):
                if words[w][idx] != now[idx]:
                    cnt += 1

            if cnt == 1:
                if not visited[w]:
                    visited[w] = True
                    stack.append(words[w])

        answer += 1



def solution(begin, target, words):
    visited = [False] * len(words)

    if target not in words:
        return 0


    return dfs(visited, begin, target, words)




print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))