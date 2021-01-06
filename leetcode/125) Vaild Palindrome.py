class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_s = []
        for char in s:
            if char.isalnum():
                refined_s.append(char.lower())
        print(refined_s)
        while len(refined_s) > 1:
            if refined_s[0] != refined_s.pop():
                return False
            else:
                del refined_s[0]
        return True

#https://leetcode.com/problems/valid-palindrome/
