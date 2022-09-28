def solution(s):
    change_count = 0
    removed_zero_count = 0

    while s != "1":
        change_count += 1
        before = len(s)

        s = s.replace("0", "")
        removed_zero_count += (before - len(s))

        s = str(bin(len(s)))[2:]

    return [change_count, removed_zero_count]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))