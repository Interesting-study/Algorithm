class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
    
'''
Runtime : 32ms, Memory : 14.2MB
stack에 괄호를 하나씩 저장해둔 후, 매핑 테이블에 있는 key-value 와 계속 대조한다.

key를 닫는 괄호로 한 이유는 우선 첫번째 여는 괄호를 stack에 저장하고, 마지막 닫는 괄호가 첫번째 여는 괄호와 짝지어진 것이 맞는지만 체크하면 되기 때문이다. 
'''
