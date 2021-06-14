def solution(words, queries):
    length = len(words)
    word_len = {}
    new_query = []
    answer = []

    #단어 - 단어길이 매핑 딕셔너리
    for word in words:
        word_len[word] = len(word)

    #와일드 카드랑 일반 단어랑 쪼갬
    for query in queries:
        new_query.append(query.split('?'))

    q_length = len(new_query)

    for i in range(q_length):
        count = 0
        for j in range(length):
            if new_query[i][0] != '':
                if words[j].startswith(new_query[i][0]) and word_len[words[j]] == len(queries[i]):
                    count += 1
            else:
                if words[j].endswith(new_query[i][-1]) and word_len[words[j]] == len(queries[i]):
                    count += 1
        answer.append(count)

    return answer

(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
          ["fro??", "????o", "fr???", "fro???", "pro?"]))