class Solution:
    def longestPalindrome(self, s: str) -> str:
        #중앙을 중심으로 확장하는 알고리즘, 이부분은 곰꼼히 다시 보자.
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        
        for i in range(len(s) - 1):
            result = max(result, 
                         expand(i, i +1),
                         expand(i, i+ 2),
                         key = len)
        return result
    
    #이해가 안 되는 부분의 문제들 다시 한번 체크 필요

#https://leetcode.com/problems/longest-palindromic-substring/
