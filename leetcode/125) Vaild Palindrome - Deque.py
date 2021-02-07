import collections
from typing import Deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_s: Deque = collections.deque() #declare refined_s 
        
        for char in s: #s is examples' sentences excepted 
            if char.isalnum():
                refined_s.append(char.lower())

        while len(refined_s) > 1:
            if refined_s.popleft() != refined_s.pop():
                return False
            
        return True
    
#Runtime : 56ms, Memory: 19.4MB, 여태까지 중에 가장 빠른 방법
