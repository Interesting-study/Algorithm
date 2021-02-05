# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q : List = []
            
        if not head: #헤드에 아무것도 없을 때
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            
        return True

#파이썬으로 linked list 구현을 해봐야겠다.
