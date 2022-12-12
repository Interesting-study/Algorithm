import string
def solution(s):
    word_dict = {"zero" : '0', "one" : '1', "two": '2',
                 "three" : '3', "four" : '4', "five" :'5',
                 "six": '6', "seven" : '7', "eight" : '8',
                 "nine" : '9'}
    if s.isdigit():
        return int(s)
    
    #s에 모두 숫자가 들어가있으면, 굳이 바꿔줄 필요가 없으므로 바로 return 
    
    new_s = list(s)
    dict_value = list(word_dict.values())
    dict_key = list(word_dict.keys())
    
    change = ""
    answer = ""
    
    #우선 하나씩 쪼갠 후에, 글자 : 숫자로 매핑한 딕셔너리에서 숫자가 아닌 것만 모은 후에, 딕셔너리에 들어간 단어인지 체크함
    
    for value in new_s:
        if value.isalpha():
            change += value
        else:
            answer += value
            
        if change in dict_key:
            answer += word_dict[change]
            change = ""
            
        #모인 워드마다 글자 : 숫자로 매핑되는치 체크함
        
    return int(answer)
