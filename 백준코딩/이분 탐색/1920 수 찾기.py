n = input()
n_list = set(map(int, input().split()))

m = input()
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)
