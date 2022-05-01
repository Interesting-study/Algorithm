#https://www.acmicpc.net/problem/20181
#범위가 100,000 일경우 이분탐색과 투포인터를 동시에 사용할 수 있다
N, K = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * N # dp[i]: i번쨰 까지의 최대 탈피 에너지
lmax, ans = 0, 0 # lmax : # 애벌레가 먹기 시작하는 구간에서 지금까지 얻었던 최대 탈피 에너지
tmp = 0 # 현재 만족도
left, right = 0, 0 # 투 포인터
while True:
    if tmp >= K:
        lmax = 0 if left == 0 else max(lmax, dp[left - 1])
        dp[right - 1] = max(dp[right - 1], lmax + tmp - K)
        tmp -= arr[left]
        left += 1
    elif right == N: break
    else:
        tmp += arr[right]
        right += 1
for i in range(N):
    ans = max(ans, dp[i])

print(ans)

'''
3 5
3 4 5

9 6
1 5 4 4 2 3 10 3 5
'''