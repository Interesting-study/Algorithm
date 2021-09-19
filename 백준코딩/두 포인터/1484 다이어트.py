#https://www.acmicpc.net/problem/1484수
#g =  현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것
def get_divisor(n):
    divisors = []
    divisore_reverse = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if (i != (n // i)):
                divisore_reverse.append(n // i)

    return divisors + divisore_reverse[::-1]

g = int(input())

g_divisor = get_divisor(g)
length = len(g_divisor)
start, end = 0, 0

candidates = []

#어차피 뒤에서부터 계산하면 g_divisor는 약수의 조합이므로, 항상 g가 나온다.
"""
(x2 - y2) = g
(x+y)(x-y) = g

x= 현재 몸무게, y = 기억하는 몸무게
(더 쪗다고 했으므로 x가 항상 현재 몸무게가 된다.), 이것들의 후보는 g의 약수

(x+y) + (x-y) = 2x 가 항상 짝수여야만 한다. 
"""
while start < length:
    now = g_divisor[start] * g_divisor[end]

    if now < g:
        end += 1
    elif now > g:
        end -= 1
    elif now == g:
      #  print("곱셈 : ", now, ", (x+y): ", g_divisor[end], ", (x-y): ", g_divisor[start])
        not_satisfied = (g_divisor[end] + g_divisor[start]) % 2

      #  print("현재 : ", present_weight, ", 기억나는 : ", remembered_weight, ", 홀수여부 : ", odd_present, odd_remembered)

        #자연수가 되려면 둘 다 짝수거나 둘 다 홀수
        if not not_satisfied and g_divisor[end] != g_divisor[start] and g_divisor[end] > g_divisor[start]:
            candidate = (g_divisor[end] + g_divisor[start]) // 2
            candidates.append(candidate)

        start += 1
        end = start


if len(candidates) == 0:
    print(-1)
else:
    candidates.sort()
    for c in candidates:
        print(c)

"""
투 포인터 

start, end = 0, 0

지금 == 타겟 : start += 1
지금 < 타겟 : end += 1
지금 > 타겟 : start -= 1
"""