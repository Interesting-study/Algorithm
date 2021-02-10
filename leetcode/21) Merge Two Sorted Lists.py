# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Runtime : 36ms, Memory:14,4MB, 그림으로 그려서 이해하는 과정 필요
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
            
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
        

