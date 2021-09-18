import copy
def solution(n, k, cmd):
    answer = ''
    worked = []
    returned = 0
    present_locate = k
    
    test = {}
    
    for i in range(n):
        test[str(i)] = "O"
        
    origin = test.copy()
    
    for ex in cmd:
        if ex[0] == "D":
            present_locate += int(ex[-1])
        elif ex[0] == "U":
            present_locate -= int(ex[-1])
        elif ex[0] == "C":
            test_key = list(test.keys())
            delete_key = str(test_key[present_locate])
            del(test[delete_key])
            worked.append(test.copy())
        else:
            if worked[-1] == test:
                worked.pop()
                test = worked[-1].copy()
                worked.pop()
            else:
                test = worked[-1].copy()
                worked.pop()
            #print("test: ", test)
            
    diff = origin.keys() - test.keys()
    for i in diff:
        origin[i] = "X"
    return "".join(origin.values())
