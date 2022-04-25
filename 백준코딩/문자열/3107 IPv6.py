#https://www.acmicpc.net/problem/3107
from collections import deque

ipv6_addr = deque(input().split(':'))
answer = []

if len(ipv6_addr) == 8: #생략된 부분이 없을 때
    for val in ipv6_addr:
        val = (4 - len(val))*'0' + val
        answer.append(val)
else: #생략된 부분이 있을 때
    omitted_cnt = 8 - len(ipv6_addr) + ipv6_addr.count('')
    omitted = ['0000'] * omitted_cnt

    is_omitted = False
    while ipv6_addr:
        now = ipv6_addr.popleft()

        if now == '':
            if not is_omitted:
                is_omitted = True
                answer.extend(omitted)

        else:
            val = (4 - len(now)) * '0' + now
            answer.append(val)

print(':'.join(answer))