def solution(s):
    s = s.split(' ')
    new_s =[]
    for i, word in enumerate(s):
        change_word = []
        for j, char in enumerate(word):
            if j % 2 == 0:
                change_word.append(s[i][j].upper())
            else:
                change_word.append(s[i][j].lower())
        new_s.append(''.join(change_word))
    return ' '.join(new_s)

#파이썬의 str은 immutal 이므로 값을 바꿔 넣을 수 없다
#리스트 컴프리헨션은 코드가 복잡해보여서 일단 쓰지 않았다
#https://programmers.co.kr/learn/courses/30/lessons/12930
