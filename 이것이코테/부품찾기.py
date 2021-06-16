n = int(input())

goods = list(map(int, input().split()))
goods.sort()

m = int(input())

needs = list(map(int, input().split()))

for need in needs:
    if need in goods:
        print("yes", end=" ")
    else:
        print("no", end=" ")