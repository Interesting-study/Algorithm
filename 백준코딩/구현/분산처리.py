T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
        continue
    elif a == 1 or a == 5 or a == 6 or b == 1:
        print(a)
        continue

    repeat = []
    value = 1
    for i in range(1, b+1):
        value *= a
        value %= 10

        if not value in repeat:
            repeat.append(value)
        else:
            break
    print(repeat[b % len(repeat) - 1])