from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
wanted = list(map(int, input().split()))
answer = []

cards_counter = Counter(cards)

for val in wanted:
    print(cards_counter[val], end=" ")

'''
{10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1}
dict -> 해시, 맵(hash, map)

1. 무언가를 찾을 때 굉장히 빨리 찾을 수 있다
2. 중복으로는 값을 넣을 수 없다

Counter는 dict 형태로 보여준다

O(1) <- 무언가를 찾을 때 가장 시간 소요가 작다
O(N) <- 평범한 찾기
'''