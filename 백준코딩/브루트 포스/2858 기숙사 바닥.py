red, brown = map(int, input().split())

height, width = 0, 0

for i in range(3, 3000):
    for j in range(3, 3000):
        if i*2 + (j-2)*2 == red and (i-2)*(j-2) == brown:
            height, width = i, j
            break

    if height != 0:
        break

if width > height:
    height, width = width, height

print(height, width)
