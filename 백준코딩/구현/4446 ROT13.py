#https://www.acmicpc.net/problem/4446
from collections import defaultdict

def change(sentence):
    for char in sentence:
        is_upper = False
        if char.isalpha():
            if char.isupper():
                is_upper = True
                char = char.lower()

            if char in vowel:
                idx = (vowel[char] + 3) % 6
                if is_upper:
                    print(vowel_idx[idx].upper(), end='')
                else:
                    print(vowel_idx[idx], end='')

            else:
                idx = (consonant[char] + 10) % 20
                if is_upper:
                    print(consonant_idx[idx].upper(), end='')
                else:
                    print(consonant_idx[idx], end='')
        else:
            print(char, end='')

vowel = defaultdict(int)
vowel_idx = defaultdict(int)
consonant = defaultdict(int)
consonant_idx = defaultdict(int)

for idx, char in enumerate("aiyeou"):
    vowel[char] = idx
    vowel_idx[idx] = char

for idx, char in enumerate("bkxznhdcwgpvjqtsrlmf"):
    consonant[char] = idx
    consonant_idx[idx] = char

while True:
    try:
        sentence = input()
        change(sentence)
        print()
    except:
        break