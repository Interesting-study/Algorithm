#https://programmers.co.kr/learn/courses/30/lessons/62048
def get_gcd(w, h):
    x, y = max(w, h), min(w, h)

    while True:
        r = x % y

        if r == 0:
            return y

        x = y
        y = r


def solution(w,h):
    total_rect = w*h
    gcd = get_gcd(w, h)

    return total_rect - (w+h - gcd)

print(solution(8, 12))