#https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product

def solution(word):
    vowels = list('AEIOU')
    word_dict = []

    for i in range(1, 6):
        word_dict.extend([''.join(w) for w in list(product(vowels, repeat=i))])

    word_dict.sort()

    return word_dict.index(word) + 1