n = list(map(int, str(int(input()))))
check = len(n) // 2

if sum(n[:check]) == sum(n[check:]):
    print("LUCKY")
else:
    print("READY")
