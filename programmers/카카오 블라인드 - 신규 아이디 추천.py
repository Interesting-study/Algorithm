import string
def solution(new_id):
    new_id = new_id.lower() 
    must_include = string.ascii_lowercase + string.digits + '-' + '_'+ '.'
    recom_id = ''
    
    for i in new_id:
        if i in must_include:
            recom_id += i
            
    #1단계와 2단계 
          
    while '..' in recom_id:
        recom_id = recom_id.replace('..', '.')
        
    #계속 while loop로 돌리게 되면 나중에는 .밖에 남지 않는다
        
    #3단계
    if recom_id[0] == '.' and len(recom_id) > 1:
        recom_id = recom_id[1:]
        
    if recom_id[-1] == '.':
        recom_id = recom_id[:-1]
        
    if recom_id == '':
        recom_id += 'a'
        
    #4단계, 5단계    
        
    if len(recom_id) >= 16:
        recom_id  = recom_id[:15]
        if recom_id[-1] == '.':
            recom_id  = recom_id[:-1]
    
    #6단계
        
    if len(recom_id) <= 2:
        recom_id = recom_id + recom_id[-1] * (3- len(recom_id))
    
    #7단계
    
    return recom_id
