class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_index = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[s_index - i] = s[s_index - i], s[i]
       # s.reverse()
        
