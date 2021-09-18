#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ""
    not_num = ""

    for i in s:
        if i.isalpha():
            not_num += i

            if not_num in num_dict.keys():
                answer += num_dict[not_num]
                not_num = ""

        elif i.isdigit():
            answer += i

    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))