def find_gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def find_lcm(x, y):
    return x*y // find_gcd(x, y)

def solution(n, m):
    return [find_gcd(n, m), find_lcm(n, m)]

print(solution(3, 12))
print(solution(2, 5))