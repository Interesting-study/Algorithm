#https://programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    answer = 65536

    str1 = str1.lower()
    str2 = str2.lower()

    new_str1 = [str1[i:i+2] for i in range(0, len(str1), 2)]
    new_str2 = [str2[i:i+2] for i in range(0, len(str2), 2)]

    print(new_str1, new_str2)

    return

print(solution("FRANCE", "french"))
print(solution("handshake",	"shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))