import re

def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"": 1, "*": 2, "#": -1}

    pattern = re.compile('(\d+)([SDT])([*#]?)')
    dart = pattern.findall(dartResult)

    for i in range(len(dart)):
        #처음으로 나온 스타상이 아닐때
        if dart[i][2] == "*"  and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

"""
정규표현식 
() : 그룹화
\d : 정수
+ : 0회이상 반복
[~]:~ 중 하나
? : 0회 또는 1회 반복
"""