import collections
from typing import Deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        q: Deque = collections.deque()
        
        '''
        리스트 대신에 데크를 사용하려는 이유는
        리스트는 동적 배열이라 맨앞의 값을 가져오면 모든 값이 쉬프팅 되므로
        시간 복잡도 O(N)이 발생한다. 그래서 데크를 이용할 생각이다.
        '''
        
        if not head:
            return True
        #아무것도 없으면 펠린드롬
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True
    
    #Runtime : 72ms, Memory : 24 MB 
