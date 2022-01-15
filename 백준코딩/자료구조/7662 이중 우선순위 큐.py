#https://www.acmicpc.net/problem/7662
from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

def sync(q):
    while q and not sync_data[q[0][1]]:
        heapq.heappop(q)

T = int(input())
for _ in range(T):
    number_of_data = int(input())

    min_heap = []
    max_heap = []
    sync_data = defaultdict(bool)

    for i in range(number_of_data):
        cmd, num = input().split()

        if cmd == 'I':
            #삽입
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            sync_data[i] = True
        elif num == '1':
            sync(max_heap)

            if max_heap:
                sync_data[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        else:
            sync(min_heap)

            if min_heap:
                sync_data[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    sync(min_heap)
    sync(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")

'''
1
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
'''