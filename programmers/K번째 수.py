def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        sel = commands[i][-1] - 1 
        
        prog = array[start:end]
        prog.sort()
        
        answer.append(prog[sel]) 
    return answer
