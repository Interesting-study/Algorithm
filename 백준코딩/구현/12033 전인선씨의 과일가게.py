T = int(input())

for i in range(T):
    n = int(input())
    all_price = list(map(int,input().split()))

    sales_price = list()

    while all_price:
        now_price = all_price.pop()*3//4
        sales_price.append(now_price)
        all_price.remove(now_price)

    sales_price.sort()
    print(sales_price)