def find_repeat(s: str):
    print("func : ", s)
    repeat_index = 0
    repeat_word = s[repeat_index]

    while s.count(repeat_word) > 1:
        repeat_index += 1
        repeat_word += s[repeat_index]
        print(repeat_word)
    #return repeat_word[:-1], repeat_index+1
    
def solution(s):
    word_queue = []
    check_point = 0
    zip_s = []

    repeat_word, check_point = find_repeat(s)
    new_s = s.split(repeat_word)
    zip_s.append(str(s.count('')) + repeat_word)
    '''
    if repeat_word == '':
        return len(s) - len(repeat_word)
    
    new_s = s.split(repeat_word)
    new_s = str(new_s.count('')) + repeat_word +''.join(new_s)
    print(new_s, len(new_s))
'''
