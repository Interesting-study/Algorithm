
def binary_search(goods, target, start, end):
    while start <= end:
        mid = (start + end) //2

        if goods[mid] == target:
            return True
        elif goods[mid] > target:
            end = mid -1
        else:
            start += 1
    return False

n = int(input())

goods = list(map(int, input().split()))
goods.sort()

m = int(input())

needs = list(map(int, input().split()))

for need in needs:
    result = binary_search(goods, need, 0, n -1)

    if result:
        print("yes", end=" ")
    else:
        print("no", end=" ")