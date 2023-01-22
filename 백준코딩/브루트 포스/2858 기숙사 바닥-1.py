def get_divisor(n):
    divisors = []
    divisore_reverse = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if (i != (n // i)):
                divisore_reverse.append(n // i)

    return divisors + divisore_reverse[::-1]

red, brown = map(int, input().split())
area = red + brown
candidate = get_divisor(area)

for i in range(0, len(candidate)//2 + 1):
    l, w = candidate[i], candidate[len(candidate) - i - 1]
    if l * 2 + (w - 2) * 2 == red and (l - 2) * (w - 2) == brown:
        break

if w > l:
    l, w = w, l

print(l, w)
