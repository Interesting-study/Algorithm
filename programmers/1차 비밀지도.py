def solution(n, arr1, arr2):
    arr1_bin = []
    arr2_bin = []
    answer = []
    arr_answer = []
    count_zero = 0
    
    for i in range(len(arr1)):
        arr1_bin.append(bin(arr1[i]))
        count_zero = n - len(arr1_bin[i][(arr1_bin[i].index('b') + 1):])
        arr1_bin[i] = '0'*count_zero + arr1_bin[i][(arr1_bin[i].index('b') + 1):]
        
        
    for i in range(len(arr2)):
        arr2_bin.append(bin(arr2[i]))
        count_zero = n - len(arr2_bin[i][(arr2_bin[i].index('b') + 1):])
        arr2_bin[i] = '0'*count_zero + arr2_bin[i][(arr2_bin[i].index('b') + 1):]
        
    for i in range(n):
        for j in range(n):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j] == '1':
                arr_answer.append('#')
            else:
                arr_answer.append(' ')
        answer.append(''.join(arr_answer))
        arr_answer = []
                
    return answer


#def solution(n, arr1, arr2):
#    answer = []
#   for i,j in zip(arr1,arr2):
#        a12 = str(bin(i|j)[2:])
#        a12=a12.rjust(n,'0')
#        a12=a12.replace('1','#')
#        a12=a12.replace('0',' ')
#        answer.append(a12)
#    return answer
