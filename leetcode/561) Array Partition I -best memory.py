class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''내림차순으로 계산하면 홀수번째마다 min인 값이 들어오므로 슬라이상을 사용함'''
        return sum(sorted(nums, reverse = True)[1::2])
                    
        
