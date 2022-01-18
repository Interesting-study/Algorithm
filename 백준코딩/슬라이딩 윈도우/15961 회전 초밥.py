#https://www.acmicpc.net/problem/15961
#접시의 수 n, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]
sushi.extend(sushi) # 원형 이어줌

max_kind = 0
left, right = 0, 0
eating = defaultdict(int)
eating[c] += 1 #보너스는 무조건 먹어야 가짓수가 올라감

for right in range(len(sushi)):
    eating[sushi[right]] += 1

    if right >= k-1:
        max_kind = max(max_kind, len(eating))
        eating[sushi[left]] -= 1
        if eating[sushi[left]] == 0:
            del eating[sushi[left]]
        left += 1

print(max_kind)

'''
슬라이딩 윈도우는 결과를 저장하면서 시간을 줄인다. 딕셔너리를 고려해서 풀이할 것
원형은 리스트를 이어본다
'''