#https://www.acmicpc.net/problem/4673
nums_set = set(range(1, 10001))
generator = set()
for i in range(1, 10001):
    generator.add(sum(list(map(int, list(str(i))))) + i)

self_number = sorted(nums_set - generator)
for i in self_number:
    print(i)