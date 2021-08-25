from itertools import combinations
import string

L, C = map(int, input().split())
alphabet = input().split()
alphabet.sort()
alpha_index = list(range(C))
vowels = set("aeiou")
consonants = set(string.ascii_lowercase) - vowels

for comb in combinations(alpha_index, L):
    now = set()
    for idx in comb:
        now.add(alphabet[idx])

    if len(vowels.intersection(now)) > 0 and len(consonants.intersection(now)) >= 2:
        print("".join(sorted(list(now))))