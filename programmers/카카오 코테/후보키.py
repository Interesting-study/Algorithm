#https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    #데이터베이스의 각 튜플의 길이는 동일하므로 가장 첫번째를 잡아도 상관없다.
    #n = 속성의 개수, key_idx = 가능한 키의 인덱스 숫자, 값은 겹칠수도 있으므로 인덱스 숫자로 조합을 고려한다.
    n = len(relation[0])
    key_idx = list(range(n))
    candidates_key = []

    #1~6까지 조합의 갯수로 따진다.
    for i in range(1, n+1):
        for comb in combinations(key_idx, i):
            hist = []
            #후보키 인덱스 조합에 따라 후보키 선정
            for rel in relation:
                current_key = [rel[c] for c in comb]
                #하나라도 중복될 경우는 유일성을 충족하지 못함
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            else:
                for ck in candidates_key:
                    #부분집합일 경우에는 최소성 충족x
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidates_key.append(comb)

    return len(candidates_key)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))