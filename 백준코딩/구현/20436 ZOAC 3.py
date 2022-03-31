#https://www.acmicpc.net/problem/20436
keyboard_char = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
keyboard_pos = {}

consonant = 'qwertasdfgzxcv' #자음쪽 자판
vowel = 'yuiophjklbnm' #모음쪽 영어자판

for i, word in enumerate(keyboard_char):
    for j, char in enumerate(word):
        keyboard_pos[char] = (i, j)

left, right = input().split()
strings = input()
answer = 0


for char in strings:
    if char in consonant: #자음을 입력할 때, 왼손으로 입력한다
        nx, ny = keyboard_pos[char]
        lx, ly = keyboard_pos[left]

        answer += (1 + (abs(nx-lx) + abs(ny-ly)))
        left = char

    else: #모음을 입력할 때 오른손으로 입력한다
        nx, ny = keyboard_pos[char]
        rx, ry = keyboard_pos[right]

        answer += (1 + (abs(nx-rx) + abs(ny-ry)))
        right = char

print(answer)

