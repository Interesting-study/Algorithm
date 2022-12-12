from collections import deque

n = int(input())
words = [input().lower() for _ in range(n)]

for word in words:
    new_word = list(word)

    for idx in range((len(new_word)//2) + 1):

        if new_word[idx] != new_word[len(new_word) - idx -1]:
            print('NO')
            break
    else:
        print('YES')