#https://www.acmicpc.net/problem/1244
def find_symmetric(get):
    start, end = get - 1, get + 1
    min_index, max_index = get, get

    while start > 0 and end < len(switch):
        if switch[start] == switch[end]:
            min_index, max_index = start, end
            start -= 1
            end += 1
        else:
            break
    return max(get - min_index, max_index - get)


n = int(input())
switch = list(map(int, input().split()))
stu_num = int(input())
switch.insert(0, -1)

for _ in range(stu_num):
    gender, get = map(int, input().split())

    if gender == 1:
        for i in range(1, len(switch)):
            if i % get == 0:
                switch[i] = (switch[i] + 1) % 2
    elif gender == 2:
        width = find_symmetric(get)
        temp = switch[get - width : get + width + 1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 2
        switch[get - width : get + width + 1] = temp

#*list 를 하면 value value 이런 형식으로 나옴
for i in range(1, len(switch), 20):
    print(*switch[i:i+20])
