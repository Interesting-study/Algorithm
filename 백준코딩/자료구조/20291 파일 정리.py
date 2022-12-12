from collections import defaultdict

n = int(input())
extension = defaultdict(int)

for _ in range(n):
    file_name, extension_name = input().split(".")
    extension[extension_name] += 1

for val in sorted(extension.items(), key=lambda x: x[0]):
    print(val[0], val[1])
