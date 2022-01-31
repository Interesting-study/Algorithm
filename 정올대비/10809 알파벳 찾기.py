import sys
vocab = sys.stdin.readline().strip()
alpha = [-1 for _ in range(26)]
for idx, c in enumerate(vocab):
    if alpha[ord(c) - ord('a')] == -1:
        alpha[ord(c) - ord('a')] = idx
print(*alpha)