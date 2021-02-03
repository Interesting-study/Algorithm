class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        '''
        out = [1, 1, 2, 6]
        if 4일 때, left : 6 = 2*3*1, right : 1(p = 1 -> 1*4 )
        if 3일 때, left : 2 = 1*2, right : 4 (p = 4 * 3 = 12)
        if 2일 때, left : 1 = 1*1, right = 12(p = 24 = 12 * 2)
        if 1일 때, left : 1 = 1*1, right : 24(p = 24)
        '''
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
