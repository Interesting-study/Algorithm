# 입력 받기
n, l = map(int, input().split())
data = list(map(int, input().split()))

# 물이 새는 곳 오름차순으로 정렬
data.sort()
# 테이프를 처음 붙이는 시작지점
start = data[0]
#필요한 테이프의 개수
count = 1

# 물이 새는 곳을 차례대로 검사하기
for location in data[1:]:
    #테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면?
    if location in range(start, start+l):
        continue # 기존 테이프 사용
    else:
        start = location
        count += 1

print(count)
