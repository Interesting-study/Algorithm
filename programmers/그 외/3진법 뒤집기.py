def change(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return rev_base


def solution(n):
    return int(change(n), 3)