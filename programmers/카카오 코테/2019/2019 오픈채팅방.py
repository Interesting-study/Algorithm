def solution(record):
    answer = []
    split_record = []
    message = {'Enter': ' 들어왔습니다.', 'Leave': ' 나갔습니다.'}
    named = {}
    length = len(record)

    for i in range(length):
        split_record.append(record[i].split())

        if split_record[i][0] in ['Enter', 'Change']:
            named[split_record[i][1]] = split_record[i][2] + '님이'


    for rec in split_record:
        if rec[0] in message.keys():
            answer.append(''.join([named[rec[1]], message[rec[0]] ] ) )

    return answer
