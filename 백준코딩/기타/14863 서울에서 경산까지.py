#https://www.acmicpc.net/problem/14863
n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (k+1) for _ in range(n)]
#dp[i][j] -> i번째 경로에서 k시간 만큼

def go(idx, time):
    if time < 0:
        return -9876543210

    if idx == n:
        return 0

    if dp[idx][time] != -1:
        return dp[idx][time]

    dp[idx][time] = max(go(idx + 1, time - info[idx][0]) + info[idx][1],
                        go(idx + 1, time - info[idx][2]) + info[idx][3])

    return dp[idx][time]

print(go(0, k))