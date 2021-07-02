def find_first_index(n):
    first_index = [9]
    square = 2

    while True:
        digit_index = (((10 ** square) - 1) - (10 ** (square - 1)) + 1) * square
        if sum(first_index) + digit_index >= n:
            break
        first_index.append(digit_index)
        square += 1

    if len(first_index) >= 2:
        sum_index = sum(first_index[:square - 1])
    else:
        sum_index = first_index[0]
    return sum_index, square, (10 ** (square -1)) - 1

n = int(input())

count = 9
add_num = 1

if n < 10:
    print(n)
else:
    count, square, new_num = find_first_index(n)

    while True:
           count += square
           if count < n:
                add_num += 1
           elif count >= n:
                new_num += add_num
                answer = list(str(new_num))
                answer_index = ((n - count) % square) - 1
                print(answer[answer_index])
                break