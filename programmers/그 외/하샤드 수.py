def solution(x):
    return x % sum([int(digit) for digit in str(x)]) == 0
    '''
    origin = x
    digits_sum = 0
    while x != 0:
        digits_sum += (x %10)
        x //= 10
    
    if origin % digits_sum == 0:
        return True
    else:
        return False
    '''
